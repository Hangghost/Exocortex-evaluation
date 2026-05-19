#!/usr/bin/env python3
"""Stage 2a — render candidates.json into markdown checklist for human review."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

CHECKLIST_OPTIONS = [
    ("approve", "送 LLM judge"),
    ("skip", "false positive"),
    ("manual_violation", "人標 confirmed violation,跳過 LLM"),
    ("manual_compliance", "人標 follow,跳過 LLM"),
]


def render(payload: dict) -> str:
    axiom_id = payload["axiom_id"]
    scan_date = payload["scan_date"]
    window = payload["window_days"]
    cands = payload["candidates"]

    lines = [
        f"# Axiom Evaluation Review — {scan_date}",
        "",
        f"- axiom: **{axiom_id}**",
        f"- window: {window} 天",
        f"- total candidates: {len(cands)}",
        "",
        "對每個 candidate 勾選 **一個** 選項。多選或全空會被 parser 拒絕。",
        "",
        f"## {axiom_id}",
        "",
    ]
    if not cands:
        lines.append("_(no candidates in this window)_")
        return "\n".join(lines) + "\n"

    for i, c in enumerate(cands, 1):
        flag = "⚠ potential violation" if c["potential_violation"] else "✓ has explicit base"
        lines += [
            f"### Candidate {i}",
            f"- session: `{c['session_id']}`",
            f"- timestamp: {c['timestamp']}",
            f"- command: `{c['command']}`",
            f"- has_explicit_base: **{c['has_explicit_base']}** ({flag})",
            f"- source: `{c['source_path']}`",
            "",
        ]
        for key, desc in CHECKLIST_OPTIONS:
            lines.append(f"- [ ] {key} — {desc}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="scan date label (default: today)")
    ap.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "dashboards",
    )
    args = ap.parse_args()

    label = args.date or datetime.now().strftime("%Y-%m-%d")
    src = args.data_dir / f"{label}_candidates.json"
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 2
    payload = json.loads(src.read_text(encoding="utf-8"))
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir / f"{label}_candidates.md"
    out.write_text(render(payload), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
