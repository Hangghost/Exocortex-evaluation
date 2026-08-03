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
import json
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

# Tool calls that put file content into the session context. Bash is excluded
# on purpose: `grep axioms/` in a shell pipeline is usually the agent looking
# for something else, and counting it would inflate the metric this scanner
# exists to keep honest.
CONTEXT_LOADING_TOOLS = {"Read", "Grep", "Glob"}

INDEX_FILENAME = "INDEX.md"


def scan_transcript(path: Path) -> tuple[Counter, bool]:
    """Return (per-axiom read counts, whether the axiom INDEX was read)."""
    hits: Counter = Counter()
    read_index = False
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
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
                    if block.get("name") not in CONTEXT_LOADING_TOOLS:
                        continue
                    payload = json.dumps(block.get("input") or {}, ensure_ascii=False)
                    for match in AXIOM_PATH_RE.finditer(payload):
                        filename = match.group(1)
                        if filename == INDEX_FILENAME:
                            read_index = True
                        else:
                            hits[filename] += 1
    except OSError as e:
        print(f"warn: cannot read {path}: {e}", file=sys.stderr)
    return hits, read_index


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
    per_axiom: Counter = Counter()
    per_axiom_sessions: defaultdict[str, set] = defaultdict(set)

    for tdir in tdirs:
        for path in sorted(tdir.glob("*.jsonl")):
            try:
                mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
            except OSError:
                continue
            if mtime < cutoff:
                continue
            sessions_total += 1
            hits, read_index = scan_transcript(path)
            if hits or read_index:
                sessions_touching += 1
            if read_index:
                sessions_reading_index += 1
            for filename, count in hits.items():
                per_axiom[filename] += count
                per_axiom_sessions[filename].add(path.stem)

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
        "axioms_total": len(all_axioms),
        "per_axiom": dict(sorted(per_axiom.items(), key=lambda kv: (-kv[1], kv[0]))),
        "per_axiom_sessions": {
            name: len(sessions) for name, sessions in sorted(per_axiom_sessions.items())
        },
        "never_read": never_read,
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    ratio = (sessions_touching / sessions_total * 100) if sessions_total else 0.0
    print(
        f"wrote {out} ({sessions_touching}/{sessions_total} sessions "
        f"({ratio:.1f}%) touched an axiom over {args.days}d; "
        f"{len(never_read)}/{len(all_axioms)} axioms never read)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
