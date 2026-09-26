#!/usr/bin/env python3
"""Stage 2b (visual) — turn the review page's exported JSON into
`data/<date>_human_review.json`, byte-for-byte the same shape `parse_human_review.py`
writes (so Stage 3 `llm_judge.py` cannot tell which path produced it).

Rules:
- Any malformed input (wrong schema, unknown status, duplicate / out-of-range index,
  axiom or count mismatch against data/<date>_candidates.json) → write NOTHING.
- A batch is written only when every candidate has exactly one status; partially
  reviewed batches are listed and skipped, so review can proceed batch by batch.
- An existing human_review.json is never overwritten unless --force.

Pure stdlib (Python 3.10).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = "axiom-eval-review/v1"
VALID_STATUSES = {"approve", "skip", "manual_violation", "manual_compliance"}


class ReviewImportError(ValueError):
    pass


def plan(doc: dict, data_dir: Path, *, force: bool = False) -> tuple[list[tuple[Path, dict]], list[str]]:
    """Return (files_to_write, notes). Raises ReviewImportError on any malformed input."""
    if not isinstance(doc, dict) or doc.get("schema") != SCHEMA:
        raise ReviewImportError(f"schema 不符：預期 {SCHEMA!r}")
    batches = doc.get("batches")
    if not isinstance(batches, dict):
        raise ReviewImportError("缺少 batches")
    writes: list[tuple[Path, dict]] = []
    notes: list[str] = []
    errors: list[str] = []
    reviewed_at = datetime.now().isoformat(timespec="seconds")
    for label, b in sorted(batches.items()):
        cand_path = data_dir / f"{label}_candidates.json"
        if not cand_path.is_file():
            errors.append(f"{label}：找不到 {cand_path.name}")
            continue
        payload = json.loads(cand_path.read_text(encoding="utf-8"))
        cands = payload["candidates"]
        if b.get("axiom_id") != payload["axiom_id"] or b.get("count") != len(cands):
            errors.append(f"{label}：axiom 或候選數與 {cand_path.name} 不一致（審閱頁可能過期，請重新 render）")
            continue
        seen: dict[int, str] = {}
        for d in b.get("decisions") or []:
            idx, st = d.get("candidate_index"), d.get("status")
            if not isinstance(idx, int) or not 1 <= idx <= len(cands):
                errors.append(f"{label}：candidate_index {idx!r} 超出範圍")
            elif st not in VALID_STATUSES:
                errors.append(f"{label}：candidate {idx} 的 status {st!r} 無效")
            elif idx in seen:
                errors.append(f"{label}：candidate {idx} 重複")
            else:
                seen[idx] = st
        if len(seen) != len(cands):
            notes.append(f"{label}：已標 {len(seen)}/{len(cands)}，未完成，略過")
            continue
        out = data_dir / f"{label}_human_review.json"
        if out.exists() and not force:
            notes.append(f"{label}：{out.name} 已存在，略過（要覆蓋請加 --force）")
            continue
        merged = [{**cands[i - 1], "status": seen[i]} for i in range(1, len(cands) + 1)]
        writes.append((out, {
            "axiom_id": payload["axiom_id"],
            "scan_date": payload["scan_date"],
            "reviewed_at": reviewed_at,
            "reviewed": merged,
        }))
    if errors:
        raise ReviewImportError("; ".join(errors))
    return writes, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("review_json", type=Path)
    ap.add_argument("--data-dir", type=Path, default=ROOT / "data")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="覆蓋既有 human_review.json")
    args = ap.parse_args()
    try:
        writes, notes = plan(json.loads(args.review_json.read_text(encoding="utf-8")),
                             args.data_dir, force=args.force)
    except (ReviewImportError, json.JSONDecodeError) as exc:
        print(f"error: 一筆都沒有寫入——{exc}", file=sys.stderr)
        return 2
    for n in notes:
        print(f"· {n}")
    for path, body in writes:
        if args.dry_run:
            print(f"[dry-run] would write {path.name}")
        else:
            path.write_text(json.dumps(body, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"wrote {path.name}")
    if not writes:
        print("沒有完整標完的批次可寫入")
    return 0


if __name__ == "__main__":
    sys.exit(main())
