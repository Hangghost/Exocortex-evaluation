#!/usr/bin/env python3
"""Stage 1 — pure grep, no LLM. Scan Claude Code transcripts for axiom-related commands.

Currently supports: a09 (explicit-branch-base) — looks for `git checkout -b` / `git branch <name>` Bash tool_use calls.

Note on evidence source: the original spec described scanning
`<exocortex-root>/inbox/captured/cc_events/<session>/raw_signals/` for Bash tool_use payloads,
but the cc-hooks-capture spec only fires PostToolUseFailure for Bash (errors only).
Successful Bash tool_use payloads live in transcript JSONLs at
`~/.claude/projects/<encoded-cwd>/<session>.jsonl`. We scan those directly.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

# axiom a09 only fires on branch-CREATION commands:
#   git checkout -b <name> [<base>]
#   git branch <name> [<base>]    (NOT -d/-D/-m/--show-current/etc)
# Flags-as-first-arg (e.g. `git branch --show-current`) are listing/maintenance,
# not creation, so the first positional arg MUST NOT start with `-`.
# Base ref name must start with a word char (refs cannot start with `-`, and
# shell separators like `&&`, `||`, `;`, `|`, `>` must not be captured as base).
_NAME = r"[A-Za-z0-9_][A-Za-z0-9_./\-]*"
CHECKOUT_PATTERNS = [
    re.compile(rf"\bgit\s+checkout\s+-b\s+({_NAME})(?:\s+({_NAME}))?"),
    re.compile(rf"\bgit\s+branch\s+({_NAME})(?:\s+({_NAME}))?"),
]


@dataclass
class Candidate:
    axiom_id: str
    session_id: str
    timestamp: str
    command: str
    has_explicit_base: bool
    potential_violation: bool
    source_path: str


def encode_cwd(cwd: str) -> str:
    # Claude Code transcripts encode `/` and `_` (and similar non-word chars)
    # to `-`. e.g. /Users/dj_workstation/... → -Users-dj-workstation-...
    return "-" + cwd.replace("/", "-").replace("_", "-").lstrip("-")


def transcript_dir_for(exocortex_root: Path) -> Path:
    encoded = encode_cwd(str(exocortex_root.resolve()))
    return Path.home() / ".claude" / "projects" / encoded


def iter_bash_commands(jsonl_path: Path):
    """Yield (timestamp, command) for every Bash tool_use in a transcript file."""
    try:
        with jsonl_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts = record.get("timestamp") or ""
                message = record.get("message") or {}
                content = message.get("content")
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") != "tool_use":
                        continue
                    if block.get("name") != "Bash":
                        continue
                    cmd = (block.get("input") or {}).get("command") or ""
                    if cmd:
                        yield ts, cmd
    except OSError as e:
        print(f"warn: cannot read {jsonl_path}: {e}", file=sys.stderr)


def parse_iso(ts: str) -> datetime | None:
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return None


def scan_a09(cmd: str) -> tuple[bool, bool] | None:
    """Return (matched, has_explicit_base) if cmd matches a09 trigger, else None."""
    for pat in CHECKOUT_PATTERNS:
        m = pat.search(cmd)
        if m:
            base = m.group(2)
            has_base = bool(base and not base.startswith("-"))
            return True, has_base
    return None


SCANNERS = {"a09": scan_a09}

# axiom_id → card filename within axioms/
AXIOM_CARD_FILES = {"a09": "a09_explicit_branch_base.md"}


def read_applies_from(axiom_id: str, repo_root: Path) -> datetime | None:
    """Read applies_from from axiom card frontmatter; None if absent."""
    fname = AXIOM_CARD_FILES.get(axiom_id)
    if not fname:
        return None
    card = repo_root / "axioms" / fname
    if not card.exists():
        return None
    text = card.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    for line in text[4:end].splitlines():
        if line.startswith("applies_from:"):
            v = line.split(":", 1)[1].strip()
            if v and v != "null":
                try:
                    return datetime.fromisoformat(v).replace(tzinfo=timezone.utc)
                except ValueError:
                    return None
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Stage 1 axiom evidence scanner")
    ap.add_argument("--axiom", required=True, help="axiom id (e.g. a09)")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument(
        "--exocortex-root",
        type=Path,
        default=Path.home() / "Documents" / "Projects" / "Exocortex-personal",
    )
    ap.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    ap.add_argument("--date", help="override scan label date (default: today)")
    args = ap.parse_args()

    scanner = SCANNERS.get(args.axiom)
    if scanner is None:
        print(f"error: axiom {args.axiom} not supported (current: {list(SCANNERS)})", file=sys.stderr)
        return 2

    tdir = transcript_dir_for(args.exocortex_root)
    if not tdir.exists():
        print(f"warn: transcript dir not found: {tdir}", file=sys.stderr)
        jsonls: list[Path] = []
    else:
        jsonls = sorted(tdir.glob("*.jsonl"))

    days_cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    applies_from = read_applies_from(args.axiom, Path(__file__).resolve().parent.parent)
    cutoff = max(days_cutoff, applies_from) if applies_from else days_cutoff
    if applies_from and applies_from > days_cutoff:
        print(f"info: applies_from={applies_from.date()} narrows window from {days_cutoff.date()}", file=sys.stderr)
    candidates: list[Candidate] = []

    for jsonl in jsonls:
        session_id = jsonl.stem
        for ts, cmd in iter_bash_commands(jsonl):
            dt = parse_iso(ts)
            if dt is None:
                continue
            if dt < cutoff:
                continue
            result = scanner(cmd)
            if result is None:
                continue
            _matched, has_base = result
            candidates.append(
                Candidate(
                    axiom_id=args.axiom,
                    session_id=session_id,
                    timestamp=ts,
                    command=cmd.strip(),
                    has_explicit_base=has_base,
                    potential_violation=not has_base,
                    source_path=str(jsonl),
                )
            )

    label = args.date or datetime.now().strftime("%Y-%m-%d")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / f"{label}_candidates.json"
    payload = {
        "axiom_id": args.axiom,
        "scan_date": label,
        "window_days": args.days,
        "applies_from": applies_from.date().isoformat() if applies_from else None,
        "effective_cutoff": cutoff.isoformat(),
        "transcript_dir": str(tdir),
        "total_candidates": len(candidates),
        "candidates": [asdict(c) for c in candidates],
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out} ({len(candidates)} candidates over {args.days}d)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
