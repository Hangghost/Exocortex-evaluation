#!/usr/bin/env python3
"""Stage 3 — write evaluation card from human_review.json.

Hard precondition: data/<date>_human_review.json MUST exist. If missing, abort
WITHOUT calling LLM (mandatory gate per spec).

LLM call is gated behind --enable-llm flag. Without it, only `manual_violation`
and `manual_compliance` candidates are committed to the card; `approve` records
are left for next run (or surfaced as warning).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AXIOMS_DIR = REPO_ROOT / "axioms"
DATA_DIR = REPO_ROOT / "data"

AXIOM_META = {
    "a09": {
        "name": "開分支必須顯式 base",
        "exocortex_path": "rules/axioms/a09_explicit_branch_base.md",
        "trigger": "所有 `git checkout -b` / `git branch <name>` 命令",
    },
}

DEFAULT_FRONTMATTER = {
    "promoted_at": None,
    "human_status": "uncertain",
    "human_reviewed_at": None,
    "total_scans": 0,
}


def load_existing_card(card_path: Path) -> tuple[dict, str]:
    """Return (frontmatter dict, body str). Empty defaults if file absent."""
    if not card_path.exists():
        return ({}, "")
    text = card_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return ({}, text)
    end = text.find("\n---\n", 4)
    if end == -1:
        return ({}, text)
    fm_text = text[4:end]
    body = text[end + 5 :]
    fm: dict = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, body


def write_card(card_path: Path, fm: dict, body: str) -> None:
    lines = ["---"]
    for k, v in fm.items():
        if v is None or v == "null":
            lines.append(f"{k}: null")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    text = "\n".join(lines) + "\n" + body
    card_path.write_text(text, encoding="utf-8")


def build_scan_section(scan_n: int, scan_date: str, window: int, reviewed: list[dict]) -> str:
    counts = Counter(r["status"] for r in reviewed)
    total = len(reviewed)
    followed = sum(1 for r in reviewed if r["has_explicit_base"])
    violations = [r for r in reviewed if r["status"] == "manual_violation"]
    pct = (followed / total * 100) if total else 0.0

    lines = [
        f"### Scan {scan_n} — {scan_date}",
        "",
        f"- **Window**: {window} 天",
        f"- **Total matches**: {total}",
        f"- **Has explicit base (符合 a09)**: {followed} ({pct:.1f}%)",
        f"- **Reviewed counts**: {dict(counts)}",
        f"- **Manual violations**: {len(violations)}",
    ]
    if violations:
        lines.append("- **Violation sessions**:")
        for v in violations:
            cmd = v["command"].replace("\n", " ⏎ ")
            if len(cmd) > 200:
                cmd = cmd[:197] + "…"
            lines.append(f"  - `{v['session_id']}` @ {v['timestamp']} — `{cmd}`")
    skipped_approves = [r for r in reviewed if r["status"] == "approve"]
    if skipped_approves:
        lines.append(f"- **`approve` candidates pending LLM**: {len(skipped_approves)} (run with --enable-llm)")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--axiom", required=True)
    ap.add_argument("--enable-llm", action="store_true", help="actually call LLM for `approve` candidates")
    args = ap.parse_args()

    if args.axiom not in AXIOM_META:
        print(f"error: axiom {args.axiom} unknown", file=sys.stderr)
        return 2

    review_path = DATA_DIR / f"{args.date}_human_review.json"
    if not review_path.exists():
        print(
            f"abort: Stage 2 未完成,SHALL 先 review data/{args.date}_candidates.json 並跑 parse_human_review.py",
            file=sys.stderr,
        )
        return 1

    cand_path = DATA_DIR / f"{args.date}_candidates.json"
    candidates_meta = json.loads(cand_path.read_text(encoding="utf-8"))
    window = candidates_meta.get("window_days", 7)

    review = json.loads(review_path.read_text(encoding="utf-8"))
    reviewed = review["reviewed"]

    if args.enable_llm:
        approves = [r for r in reviewed if r["status"] == "approve"]
        if approves:
            print(
                f"warn: --enable-llm requested but LLM judge stub not implemented for axiom {args.axiom}; "
                f"{len(approves)} `approve` candidates will be skipped",
                file=sys.stderr,
            )

    meta = AXIOM_META[args.axiom]
    card_path = AXIOMS_DIR / f"{args.axiom}_explicit_branch_base.md" if args.axiom == "a09" else AXIOMS_DIR / f"{args.axiom}.md"
    fm, body = load_existing_card(card_path)

    fm.setdefault("axiom_id", args.axiom)
    fm.setdefault("axiom_name", meta["name"])
    fm.setdefault("axiom_path", meta["exocortex_path"])
    fm.setdefault("promoted_at", DEFAULT_FRONTMATTER["promoted_at"])
    fm.setdefault("human_status", DEFAULT_FRONTMATTER["human_status"])
    fm.setdefault("human_reviewed_at", DEFAULT_FRONTMATTER["human_reviewed_at"])
    fm["last_scanned_at"] = args.date
    try:
        prior_scans = int(fm.get("total_scans", 0))
    except (TypeError, ValueError):
        prior_scans = 0
    fm["total_scans"] = str(prior_scans + 1)

    new_scan_section = build_scan_section(prior_scans + 1, args.date, window, reviewed)

    if not body.strip():
        body = (
            f"\n# {meta['name']}\n\n"
            f"## 觸發條件\n\n{meta['trigger']}\n\n"
            f"## Scan History\n\n{new_scan_section}\n"
            f"## Human Notes\n\n_(待人填:首輪試點觀察、是否需要 prompt 調整、是否考慮 demote)_\n"
        )
    else:
        scan_marker = "## Scan History"
        if scan_marker in body:
            head, _, rest = body.partition(scan_marker)
            body = f"{head}{scan_marker}\n\n{new_scan_section}{rest.split(scan_marker, 1)[-1]}"
        else:
            body = body.rstrip() + f"\n\n## Scan History\n\n{new_scan_section}"

    AXIOMS_DIR.mkdir(parents=True, exist_ok=True)
    write_card(card_path, fm, body)
    print(f"wrote {card_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
