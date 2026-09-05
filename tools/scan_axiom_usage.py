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

from transcript_source import (
    TranscriptEnvironmentError,
    describe_dirs,
    enumerate_transcript_dirs,
    iter_transcripts,
)

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


class WindowError(ValueError):
    """Raised when --date/--since/--until produce an inconsistent or invalid window."""


class OverwriteRefused(RuntimeError):
    """Raised when an existing output file's window differs from this run's."""


@dataclass
class Candidate:
    axiom_id: str
    session_id: str
    timestamp: str
    command: str
    has_explicit_base: bool
    potential_violation: bool
    source_path: str




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


def parse_iso_date(s: str) -> datetime:
    """Parse an ISO 'YYYY-MM-DD' date into a UTC midnight datetime.

    Raises WindowError (not a bare ValueError) so callers surface one
    scanner-specific message instead of a strptime traceback.
    """
    try:
        return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError as e:
        raise WindowError(f"invalid date {s!r} (expected YYYY-MM-DD): {e}") from e


def compute_window(
    date_arg: str | None,
    days: int,
    since_arg: str | None,
    until_arg: str | None,
    applies_from: datetime | None,
) -> tuple[str, datetime, datetime]:
    """Resolve (label, effective_cutoff, window_until) from CLI args.

    Design: --date sets BOTH the output label and the window's upper bound
    (until), so a bare `--date X --days N` scan is structurally guaranteed to
    write to a file named after the window it actually covers — the original
    defect was label and window being computed independently (label from
    args.date, window always from datetime.now()). --since/--until are
    explicit overrides for backfill scans. When --date and --until are both
    given and disagree, that is a contradiction the caller must resolve, not
    something to silently pick a winner for.
    """
    if date_arg and until_arg:
        if parse_iso_date(date_arg) != parse_iso_date(until_arg):
            raise WindowError(
                f"--date {date_arg} and --until {until_arg} disagree; "
                "pass matching values or omit one"
            )

    label = date_arg or until_arg or datetime.now().strftime("%Y-%m-%d")

    until_source = until_arg or date_arg
    if until_source:
        # until is inclusive of the given calendar day, so the boundary sits
        # at the start of the following day.
        window_until = parse_iso_date(until_source) + timedelta(days=1)
    else:
        window_until = datetime.now(timezone.utc)

    since_dt = parse_iso_date(since_arg) if since_arg else window_until - timedelta(days=days)
    if since_dt >= window_until:
        raise WindowError(
            f"--since ({since_dt.date()}) is not before the window's upper bound "
            f"({window_until.date()})"
        )

    effective_cutoff = max(since_dt, applies_from) if applies_from else since_dt
    if applies_from and applies_from > since_dt:
        print(f"info: applies_from={applies_from.date()} narrows window from {since_dt.date()}", file=sys.stderr)

    return label, effective_cutoff, window_until


def check_overwrite(out_path: Path, effective_cutoff: datetime, window_until: datetime, force: bool) -> None:
    """Refuse to overwrite `out_path` if its recorded window differs from this run's.

    Same label with a different measured window means the previous batch's
    data would be silently replaced by data covering a different period —
    exactly the corruption this feature exists to prevent. --force overrides.
    """
    if force or not out_path.exists():
        return
    try:
        existing = json.loads(out_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise OverwriteRefused(f"cannot read existing {out_path} to compare windows: {e}") from e
    existing_cutoff = existing.get("effective_cutoff")
    existing_until = existing.get("window_until")
    if existing_cutoff != effective_cutoff.isoformat() or existing_until != window_until.isoformat():
        raise OverwriteRefused(
            f"{out_path} already exists with a different window "
            f"(effective_cutoff={existing_cutoff!r}, window_until={existing_until!r}); "
            f"this run computed (effective_cutoff={effective_cutoff.isoformat()!r}, "
            f"window_until={window_until.isoformat()!r}). Pass --force to overwrite."
        )


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
    # No default: a hardcoded path is an environment assumption that the
    # scheduling layer's template substitution cannot keep in sync. When the
    # repo moved out of ~/Documents (2026-06-07) the stale default silently
    # pointed at a vanished directory for 8 weeks. The plist passes this
    # explicitly via __REPO_ROOT__.
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
    ap.add_argument(
        "--date",
        help="scan label date (YYYY-MM-DD); also sets the window's upper "
        "bound (until) unless --until is given explicitly (default: today/now)",
    )
    ap.add_argument("--since", help="explicit window lower bound (YYYY-MM-DD); overrides --days")
    ap.add_argument("--until", help="explicit window upper bound (YYYY-MM-DD); must agree with --date if both given")
    ap.add_argument(
        "--force",
        action="store_true",
        help="overwrite an existing output file even if its recorded window differs from this run's",
    )
    args = ap.parse_args()

    scanner = SCANNERS.get(args.axiom)
    if scanner is None:
        print(f"error: axiom {args.axiom} not supported (current: {list(SCANNERS)})", file=sys.stderr)
        return 2

    # Fail loud: a missing environment is not a zero-candidate result.
    # Raising here means no output file is written, so a stale newest file in
    # data/ is itself the signal that the pipeline is broken (see design D5).
    try:
        tdirs = enumerate_transcript_dirs(args.exocortex_root)
    except TranscriptEnvironmentError as e:
        print(f"error: {e}", file=sys.stderr)
        return 3
    jsonls = list(iter_transcripts(tdirs))

    applies_from = read_applies_from(args.axiom, Path(__file__).resolve().parent.parent)
    try:
        label, cutoff, window_until = compute_window(args.date, args.days, args.since, args.until, applies_from)
    except WindowError as e:
        print(f"error: {e}", file=sys.stderr)
        return 4
    candidates: list[Candidate] = []

    for jsonl in jsonls:
        session_id = jsonl.stem
        for ts, cmd in iter_bash_commands(jsonl):
            dt = parse_iso(ts)
            if dt is None:
                continue
            if dt < cutoff or dt >= window_until:
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

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / f"{label}_candidates.json"
    try:
        check_overwrite(out, cutoff, window_until, args.force)
    except OverwriteRefused as e:
        print(f"error: {e}", file=sys.stderr)
        return 5
    payload = {
        "axiom_id": args.axiom,
        "scan_date": label,
        "window_days": args.days,
        "applies_from": applies_from.date().isoformat() if applies_from else None,
        "effective_cutoff": cutoff.isoformat(),
        "window_until": window_until.isoformat(),
        # scanned_dirs marks the measurement scope. Scans before 2026-08
        # covered only the main checkout and systematically undercounted;
        # presence of this field distinguishes the two calibrations.
        "scanned_dirs": describe_dirs(tdirs),
        "sessions_scanned": len(jsonls),
        "total_candidates": len(candidates),
        "candidates": [asdict(c) for c in candidates],
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    window_days = (window_until - cutoff).days
    print(
        f"wrote {out} ({len(candidates)} candidates over {window_days}d "
        f"[{cutoff.date()}, {window_until.date()}); "
        f"{len(jsonls)} sessions across {len(tdirs)} dirs)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
