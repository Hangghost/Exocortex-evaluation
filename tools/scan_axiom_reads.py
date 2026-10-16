#!/usr/bin/env python3
"""Stage 1 — axiom read-frequency scanner. Pure grep, no LLM.

Answers one question per axiom: **did this rule ever reach the agent?**

This is deliberately a weaker claim than the compliance scanner
(`scan_axiom_usage.py`) makes. Compliance measures whether behaviour matched a
rule, which conflates the rule with every other thing that could have produced
that behaviour — the a09 pilot scored 88.7% compliance while the axiom itself
was read in 0 of 926 sessions, because the enforcing text lived in a slash
command's prose instead. Read-frequency claims no causality; it reports
presence in context, which is cheap to measure honestly and is the precondition
for any causal claim at all.

The two scanners are complementary, not substitutes:

    read-freq high + compliance high → the rule is plausibly doing work
    read-freq zero + compliance high → the effect comes from elsewhere;
                                       the axiom text is a retirement candidate
    read-freq zero + no other source → the rule is dead weight

Coverage is every file in `rules/axioms/` with zero per-axiom configuration,
because "was this file opened" needs no bespoke grep pattern — unlike
compliance, which is only expressible for command-shaped axioms.

Stage 1 only: no LLM call, therefore no Stage 2 human gate (that gate exists to
stop Stage 3 from burning tokens on unreviewed candidates).
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from transcript_source import (
    TranscriptEnvironmentError,
    describe_dirs,
    enumerate_transcript_dirs,
)

# Matches a path reference to an individual axiom file inside a tool_use input.
AXIOM_PATH_RE = re.compile(r"rules/axioms/([A-Za-z0-9_]+\.md)")

# Tool calls that put file content into the session context via a structured
# path argument.
CONTEXT_LOADING_TOOLS = {"Read", "Grep", "Glob"}

# Bash is counted too, but only through `bash_axiom_reads` below: the CLAUDE.md
# boot sequence loads axioms with a shell for-loop `cat`, which a tools-only
# scan misses (measured 2026-10-16: INDEX read in 522/570 CLI sessions, only
# 221 of them via Read/Grep/Glob). A blanket "any Bash mentioning axioms/"
# count would swing the other way — `ls`, `wc -l`, `grep -l` are the agent
# looking *around* the registry, not loading it — so a Bash command counts only
# when it *prints file content*.
#
# Known blind spot: rules loaded by path-scoped triggers (Claude Code `paths:`
# rule frontmatter) enter context without any tool call, so this scanner cannot
# see them. Read-frequency for such axioms is a lower bound.

# Verbs whose output is the file's content. grep/ls/wc/find are deliberately
# absent: they search or list, they do not load.
PRINT_VERBS = {"cat", "head", "sed", "tail", "less", "bat", "nl", "awk", "more"}

# Entrypoints of unattended pipelines (observer / reflector / digest jobs run
# through the SDK). Their reads reflect what the pipeline was told to load, not
# whether an interactive agent met the rule, so they are tallied separately and
# kept out of the headline per-axiom numbers.
PIPELINE_ENTRYPOINTS = frozenset({"sdk-cli", "sdk-ts", "sdk-py"})
UNKNOWN_ENTRYPOINT = "unknown"

# A glob expanding to more than this many axiom files is a directory scan, not
# a deliberate read of those files.
MAX_GLOB_EXPANSION = 3

_NAME_RE = re.compile(r"rules/axioms/([A-Za-z0-9_*?\[\]]+(?:\.md)?)")
_WRITE_RE = re.compile(
    r"(>\s*\S*rules/axioms/|\btee\b[^|;]*rules/axioms/|sed\s+-i[^|;]*rules/axioms/)"
)
_WRITE_TARGET_RE = re.compile(r">\s*\S*rules/axioms/([A-Za-z0-9_]+\.md)")
_FOR_LOOP_RE = re.compile(r"for\s+(\w+)\s+in\s+(.*?);\s*do\b(.*?)\bdone", re.S)
_CD_AXIOMS_RE = re.compile(r"cd\s+\S*rules/axioms")

INDEX_FILENAME = "INDEX.md"


def _axiom_names(text: str, known: list[str], relative_ok: bool) -> set[str]:
    """Axiom files named in `text`: explicit paths, small globs, cd-relative names."""
    out: set[str] = set()
    for m in _NAME_RE.finditer(text):
        pat = m.group(1)
        if any(c in pat for c in "*?["):
            glob = pat if pat.endswith(".md") else pat + "*"
            hit = [a for a in known if fnmatch.fnmatch(a, glob)]
            if len(hit) <= MAX_GLOB_EXPANSION:
                out.update(hit)
        elif pat in known:
            out.add(pat)
    if relative_ok:
        out.update(a for a in known if re.search(r"(?<![\w/])" + re.escape(a), text))
    return out


def bash_axiom_reads(command: str, known: list[str]) -> set[str]:
    """Axiom filenames whose content a shell command prints into the session.

    Counts (a) `for f in <axiom files>; do cat $f; done`-style loops whose body
    runs a print verb on the loop variable, and (b) command segments whose
    *first pipeline stage* is a print verb (`cat rules/axioms/INDEX.md | head`).
    Does not count `ls`/`wc`/`grep`/`find` over the directory, globs expanding
    to more than `MAX_GLOB_EXPANSION` files, or files the command writes to.

    `known` is every axiom filename including INDEX.md (needed to expand globs
    and resolve names after `cd rules/axioms`).
    """
    if "axioms" not in command:
        return set()
    relative_ok = bool(_CD_AXIOMS_RE.search(command))
    found: set[str] = set()
    verbs = "|".join(sorted(PRINT_VERBS))
    for m in _FOR_LOOP_RE.finditer(command):
        var, file_list, body = m.groups()
        if re.search(rf"\b({verbs})\b[^;|&]*\${{?{var}\b", body):
            found |= _axiom_names(file_list, known, relative_ok)
    for segment in re.split(r";|&&|\|\||\n", command):
        first_stage = segment.split("|")[0].strip()
        words = first_stage.split()
        if words and os.path.basename(words[0]) in PRINT_VERBS:
            found |= _axiom_names(first_stage, known, relative_ok)
    if _WRITE_RE.search(command):
        # A command that writes into the registry is editing it; the print verb
        # in it is usually echoing the edit, not loading the rule.
        found -= set(_WRITE_TARGET_RE.findall(command))
    return found


def scan_transcript(
    path: Path, known: list[str] | None = None
) -> tuple[Counter, bool, str]:
    """Return (per-axiom read counts, whether INDEX was read, entrypoint).

    `known` is the axiom filename universe (including INDEX.md) used to resolve
    Bash globs and cd-relative names; explicit paths resolve without it.
    """
    hits: Counter = Counter()
    read_index = False
    entrypoint = UNKNOWN_ENTRYPOINT
    known = known or []
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if entrypoint == UNKNOWN_ENTRYPOINT and '"entrypoint"' in line:
                    try:
                        entrypoint = json.loads(line).get("entrypoint") or entrypoint
                    except json.JSONDecodeError:
                        pass
                # Cheap pre-filter: the overwhelming majority of transcript
                # lines cannot possibly reference an axiom.
                if "axioms" not in line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                message = record.get("message") or {}
                content = message.get("content")
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") != "tool_use":
                        continue
                    name = block.get("name")
                    if name in CONTEXT_LOADING_TOOLS:
                        payload = json.dumps(block.get("input") or {}, ensure_ascii=False)
                        filenames = [m.group(1) for m in AXIOM_PATH_RE.finditer(payload)]
                    elif name == "Bash":
                        command = str((block.get("input") or {}).get("command", ""))
                        filenames = sorted(bash_axiom_reads(command, known))
                    else:
                        continue
                    for filename in filenames:
                        if filename == INDEX_FILENAME:
                            read_index = True
                        else:
                            hits[filename] += 1
    except OSError as e:
        print(f"warn: cannot read {path}: {e}", file=sys.stderr)
    return hits, read_index, entrypoint


def list_axiom_files(exocortex_root: Path) -> list[str]:
    """All axiom filenames in the registry, excluding the index itself."""
    axioms_dir = Path(exocortex_root) / "rules" / "axioms"
    if not axioms_dir.is_dir():
        raise TranscriptEnvironmentError(
            f"axiom registry not found: {axioms_dir}\n"
            "  --exocortex-root does not look like an Exocortex-personal repo."
        )
    return sorted(
        p.name for p in axioms_dir.glob("*.md") if p.name != INDEX_FILENAME
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Stage 1 axiom read-frequency scanner")
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument(
        "--exocortex-root",
        type=Path,
        required=True,
        help="absolute path to the Exocortex-personal repo root",
    )
    ap.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    ap.add_argument("--date", help="override scan label date (default: today)")
    args = ap.parse_args()

    # Fail loud rather than writing an empty result: see transcript_source.
    try:
        tdirs = enumerate_transcript_dirs(args.exocortex_root)
        all_axioms = list_axiom_files(args.exocortex_root)
    except TranscriptEnvironmentError as e:
        print(f"error: {e}", file=sys.stderr)
        return 3

    # The window is defined by session-file mtime (last activity), so the unit
    # of analysis is the session — which is what the headline ratio
    # "N of M sessions saw an axiom" needs. Reads inside an in-window session
    # are all counted, regardless of individual record timestamps.
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    sessions_total = 0
    sessions_touching = 0
    sessions_reading_index = 0
    by_entrypoint: defaultdict[str, Counter] = defaultdict(Counter)
    per_axiom: Counter = Counter()  # interactive sessions only
    per_axiom_sessions: defaultdict[str, set] = defaultdict(set)
    per_axiom_pipeline: Counter = Counter()
    per_axiom_sessions_pipeline: defaultdict[str, set] = defaultdict(set)
    known = [*all_axioms, INDEX_FILENAME]

    for tdir in tdirs:
        for path in sorted(tdir.glob("*.jsonl")):
            try:
                mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
            except OSError:
                continue
            if mtime < cutoff:
                continue
            hits, read_index, entrypoint = scan_transcript(path, known)
            sessions_total += 1
            ep = by_entrypoint[entrypoint]
            ep["sessions_total"] += 1
            if hits or read_index:
                sessions_touching += 1
                ep["sessions_touching_axioms"] += 1
            if read_index:
                sessions_reading_index += 1
                ep["sessions_reading_index"] += 1
            pipeline = entrypoint in PIPELINE_ENTRYPOINTS
            counts = per_axiom_pipeline if pipeline else per_axiom
            sessions = per_axiom_sessions_pipeline if pipeline else per_axiom_sessions
            for filename, count in hits.items():
                counts[filename] += count
                sessions[filename].add(path.stem)

    # "Never read" is judged on interactive sessions: an axiom only a pipeline
    # opens has still never met an interactive agent.
    never_read = [name for name in all_axioms if name not in per_axiom]

    label = args.date or datetime.now().strftime("%Y-%m-%d")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / f"{label}_read_frequency.json"
    payload = {
        "scan_date": label,
        "window_days": args.days,
        "window_basis": "session file mtime",
        "scanned_dirs": describe_dirs(tdirs),
        "sessions_total": sessions_total,
        "sessions_touching_axioms": sessions_touching,
        "sessions_reading_index": sessions_reading_index,
        "counting": {
            "tools": sorted(CONTEXT_LOADING_TOOLS) + ["Bash (print-verb reads only)"],
            "pipeline_entrypoints": sorted(PIPELINE_ENTRYPOINTS),
            "sessions_*": "all entrypoints; see by_entrypoint for the split",
            "per_axiom/never_read": "interactive entrypoints only",
            "blind_spot": "path-scoped rule loads involve no tool call and are not seen",
        },
        "by_entrypoint": {
            name: {
                "kind": "pipeline" if name in PIPELINE_ENTRYPOINTS else "interactive",
                **dict(counter),
            }
            for name, counter in sorted(by_entrypoint.items())
        },
        "axioms_total": len(all_axioms),
        "per_axiom": dict(sorted(per_axiom.items(), key=lambda kv: (-kv[1], kv[0]))),
        "per_axiom_sessions": {
            name: len(sessions) for name, sessions in sorted(per_axiom_sessions.items())
        },
        "per_axiom_pipeline": dict(
            sorted(per_axiom_pipeline.items(), key=lambda kv: (-kv[1], kv[0]))
        ),
        "per_axiom_sessions_pipeline": {
            name: len(sessions)
            for name, sessions in sorted(per_axiom_sessions_pipeline.items())
        },
        "never_read": never_read,
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    ratio = (sessions_touching / sessions_total * 100) if sessions_total else 0.0
    print(
        f"wrote {out} ({sessions_touching}/{sessions_total} sessions "
        f"({ratio:.1f}%) touched an axiom over {args.days}d; "
        f"{len(never_read)}/{len(all_axioms)} axioms never read interactively)"
    )
    for name, counter in sorted(by_entrypoint.items()):
        print(
            f"  [{name}] index read in {counter['sessions_reading_index']}"
            f"/{counter['sessions_total']} sessions"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
