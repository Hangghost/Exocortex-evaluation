#!/usr/bin/env python3
"""Weekly Stage 1 runner — invokes every scanner in one scheduled slot.

Both scanners are Stage 1, free, and share an environment, so they share a
launchd slot rather than each carrying its own plist and install.sh entry.

**Order is load-bearing.** The external liveness signal that Exocortex's
`state_audit` watches is the mtime of the newest `data/*_candidates.json` — it
deliberately cannot read file contents (that would leak evaluation conclusions
back across the reflector-blind boundary). For "candidates file is stale" to
stay a faithful proxy for "the pipeline is unwell", no scanner may succeed in
writing the candidates file while a sibling scanner is failing.

So: run read-frequency first and abort the whole run on any failure. Whichever
scanner breaks, the candidates file goes unwritten and the staleness signal
fires. See the Fail-loud contract section in README.md.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent


def run_scanner(script: str, args: list[str]) -> int:
    cmd = [sys.executable, str(TOOLS_DIR / script), *args]
    print(f"--- running {script}", flush=True)
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(
            f"error: {script} exited {result.returncode}; aborting run so the "
            "candidates file stays stale and the liveness check fires",
            file=sys.stderr,
        )
    return result.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Run all Stage 1 scanners")
    ap.add_argument("--exocortex-root", type=Path, required=True)
    ap.add_argument("--axiom", default="a09", help="axiom id for the compliance scan")
    ap.add_argument("--days", type=int, default=7, help="compliance scan window")
    ap.add_argument(
        "--read-days", type=int, default=30, help="read-frequency scan window"
    )
    args = ap.parse_args()

    root = ["--exocortex-root", str(args.exocortex_root)]

    rc = run_scanner("scan_axiom_reads.py", [*root, "--days", str(args.read_days)])
    if rc != 0:
        return rc

    rc = run_scanner(
        "scan_axiom_usage.py", [*root, "--axiom", args.axiom, "--days", str(args.days)]
    )
    if rc != 0:
        return rc

    print("--- all scanners ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
