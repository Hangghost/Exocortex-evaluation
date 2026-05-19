#!/usr/bin/env python3
"""Stage 2b — parse human-reviewed markdown checklist back into JSON.

Validates that each candidate has exactly one status checked (approve / skip /
manual_violation / manual_compliance). Multi-checked or all-empty → error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

VALID_STATUSES = {"approve", "skip", "manual_violation", "manual_compliance"}
CHECK_RE = re.compile(r"^- \[(x| )\] (\w+)", re.IGNORECASE)
CAND_HEADER_RE = re.compile(r"^### Candidate (\d+)")


def parse(md_text: str) -> list[dict]:
    """Return list of {candidate_index, status}."""
    blocks: list[tuple[int, list[str]]] = []
    current_idx: int | None = None
    current_lines: list[str] = []
    for raw in md_text.splitlines():
        m = CAND_HEADER_RE.match(raw)
        if m:
            if current_idx is not None:
                blocks.append((current_idx, current_lines))
            current_idx = int(m.group(1))
            current_lines = []
            continue
        if current_idx is not None:
            current_lines.append(raw)
    if current_idx is not None:
        blocks.append((current_idx, current_lines))

    results: list[dict] = []
    for idx, lines in blocks:
        checked: list[str] = []
        for line in lines:
            m = CHECK_RE.match(line.strip())
            if not m:
                continue
            mark, key = m.groups()
            if mark.lower() == "x" and key in VALID_STATUSES:
                checked.append(key)
        if len(checked) == 0:
            raise SystemExit(f"error: candidate {idx} has no status checked")
        if len(checked) > 1:
            raise SystemExit(f"error: candidate {idx} has multiple statuses checked: {checked}")
        results.append({"candidate_index": idx, "status": checked[0]})
    return results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="scan date label (default: today)")
    ap.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    ap.add_argument(
        "--dashboards-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "dashboards",
    )
    args = ap.parse_args()

    label = args.date or datetime.now().strftime("%Y-%m-%d")
    md_path = args.dashboards_dir / f"{label}_candidates.md"
    cand_path = args.data_dir / f"{label}_candidates.json"
    if not md_path.exists():
        print(f"error: {md_path} not found", file=sys.stderr)
        return 2
    if not cand_path.exists():
        print(f"error: {cand_path} not found", file=sys.stderr)
        return 2

    reviewed = parse(md_path.read_text(encoding="utf-8"))
    candidates = json.loads(cand_path.read_text(encoding="utf-8"))
    cands = candidates["candidates"]

    if len(reviewed) != len(cands):
        print(
            f"error: reviewed count {len(reviewed)} != candidates {len(cands)}",
            file=sys.stderr,
        )
        return 2

    merged = []
    for r in reviewed:
        i = r["candidate_index"] - 1
        if i < 0 or i >= len(cands):
            print(f"error: candidate index {r['candidate_index']} out of range", file=sys.stderr)
            return 2
        merged.append({**cands[i], "status": r["status"]})

    out = args.data_dir / f"{label}_human_review.json"
    out.write_text(
        json.dumps(
            {
                "axiom_id": candidates["axiom_id"],
                "scan_date": candidates["scan_date"],
                "reviewed_at": datetime.now().isoformat(timespec="seconds"),
                "reviewed": merged,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"wrote {out} ({len(merged)} reviewed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
