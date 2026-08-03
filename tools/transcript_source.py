#!/usr/bin/env python3
"""Shared transcript-source resolution for Stage 1 scanners.

Two scanners consume Claude Code transcripts (`scan_axiom_usage.py` for
per-axiom compliance, `scan_axiom_reads.py` for read-frequency). Both need the
same answer to "which transcript directories belong to this Exocortex repo?",
so the logic lives here rather than being duplicated.

Two invariants this module exists to enforce:

1. **Enumerate worktrees, not just the main checkout.** Background sessions
   always run inside `<repo>/.claude/worktrees/<name>/`, which Claude Code
   encodes into its own `~/.claude/projects/` directory. Resolving only the
   main checkout silently drops every bg session — measured at 295/926 (32%)
   of sessions on 2026-08-02.

2. **Fail loud on a missing environment.** A scanner that cannot find its
   transcripts has *not* observed "zero candidates"; it has failed. Collapsing
   both into `exit 0` + an empty result file is what let a repo relocation go
   unnoticed for 8 weeks. See axiom v02 (silent degradation must signal).
"""
from __future__ import annotations

from pathlib import Path

WORKTREE_INFIX = "--claude-worktrees-"


class TranscriptEnvironmentError(RuntimeError):
    """Raised when the transcript environment is missing or unusable.

    Callers SHALL treat this as a fatal error: exit non-zero and write no
    output file. It is never a legitimate "no results" outcome.
    """


def encode_cwd(cwd: str) -> str:
    """Encode an absolute path the way Claude Code names its project dirs.

    `/` and `_` (and similar non-word chars) collapse to `-`, e.g.
    `/Users/dj_workstation/Code/X` → `-Users-dj-workstation-Code-X`.
    """
    return "-" + cwd.replace("/", "-").replace("_", "-").lstrip("-")


def projects_root() -> Path:
    return Path.home() / ".claude" / "projects"


def enumerate_transcript_dirs(exocortex_root: Path) -> list[Path]:
    """Return every transcript dir belonging to `exocortex_root`.

    Includes the main checkout's dir plus one dir per `.claude/worktrees/*`
    session directory that Claude Code has created.

    Raises `TranscriptEnvironmentError` when `~/.claude/projects/` or the main
    checkout's transcript dir is absent — that means the root argument is wrong
    or the repo moved, not that there is nothing to report. Worktree dirs are
    optional: a machine that has never run a bg session legitimately has none.
    """
    root = projects_root()
    if not root.is_dir():
        raise TranscriptEnvironmentError(
            f"Claude Code projects root not found: {root}"
        )

    main_encoded = encode_cwd(str(Path(exocortex_root).resolve()))
    main_dir = root / main_encoded
    if not main_dir.is_dir():
        raise TranscriptEnvironmentError(
            f"transcript dir not found for --exocortex-root: {main_dir}\n"
            f"  (resolved from {exocortex_root})\n"
            "  The repo may have moved, or --exocortex-root may be wrong. "
            "Refusing to write an empty result file."
        )

    dirs = [main_dir]
    worktree_prefix = main_encoded + WORKTREE_INFIX
    dirs.extend(
        sorted(
            d
            for d in root.iterdir()
            if d.is_dir() and d.name.startswith(worktree_prefix)
        )
    )
    return dirs


def iter_transcripts(dirs: list[Path]):
    """Yield every `*.jsonl` transcript across the given dirs, sorted per dir."""
    for d in dirs:
        yield from sorted(d.glob("*.jsonl"))


def describe_dirs(dirs: list[Path]) -> list[str]:
    """Render dirs for the `scanned_dirs` output field (names, not full paths).

    Names alone identify main-vs-worktree scope while keeping the output file
    readable; the full path is reconstructible from `~/.claude/projects/`.
    """
    return [d.name for d in dirs]
