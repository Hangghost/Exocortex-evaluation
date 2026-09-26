"""Tests for the visual Stage 2 path (render_review_page + import_review_json).

Synthetic fixtures only. The key contract: the visual path's human_review.json is
field-for-field identical to the markdown path's (render_review_dashboard →
checked markdown → parse_human_review), so Stage 3 cannot tell them apart.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import import_review_json as irj  # noqa: E402
import parse_human_review as phr  # noqa: E402
import render_review_dashboard as rrd  # noqa: E402
import render_review_page as rrp  # noqa: E402


def _cand(i: int, violation: bool) -> dict:
    return {
        "session_id": f"s{i}", "timestamp": f"2026-09-0{i}T10:00:00",
        "command": f"git checkout -b feat-{i}" + ("</script><b>x" if i == 2 else ""),
        "has_explicit_base": not violation, "potential_violation": violation,
        "source_path": f"/tmp/t{i}.jsonl",
    }


def _write(data: Path, label: str, n: int, axiom: str = "a09") -> dict:
    payload = {"axiom_id": axiom, "scan_date": label, "window_days": 7,
               "total_candidates": n, "candidates": [_cand(i, i % 2 == 1) for i in range(1, n + 1)]}
    (data / f"{label}_candidates.json").write_text(json.dumps(payload), encoding="utf-8")
    return payload


def _doc(batches: dict) -> dict:
    return {"schema": rrp.SCHEMA, "generated_on": "2026-09-26", "batches": batches}


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.data = Path(self._tmp.name) / "data"
        self.data.mkdir()

    def tearDown(self) -> None:
        self._tmp.cleanup()


class PendingTests(Base):
    def test_selects_only_unreviewed_nonempty_non_gap_batches(self) -> None:
        _write(self.data, "2026-08-01", 2)
        _write(self.data, "2026-08-08", 0)                     # empty
        _write(self.data, "2026-08-15", 1)
        (self.data / "2026-08-15_human_review.json").write_text("{}")  # reviewed
        _write(self.data, "2026-08-22", 1)
        (self.data / "DATA_GAPS.md").write_text("| 日期 | x |\n|---|---|\n| 2026-08-22 | blind |\n")
        self.assertEqual([b["label"] for b in rrp.pending_batches(self.data)], ["2026-08-01"])


class RenderTests(Base):
    def test_page_is_self_contained_and_script_safe(self) -> None:
        _write(self.data, "2026-08-01", 3)
        page = rrp.render(rrp.pending_batches(self.data), generated_on="2026-09-26")
        self.assertIn(rrp.SCHEMA, page)
        self.assertEqual(page.count("</script>"), 1)            # the payload cannot close the tag
        self.assertNotIn("http://", page.replace("http://www.w3.org", ""))
        self.assertNotIn("https://", page)                      # zero external resources
        for key in ("approve", "skip", "manual_violation", "manual_compliance"):
            self.assertIn(key, page)


class ImportTests(Base):
    def test_matches_markdown_path_field_for_field(self) -> None:
        payload = _write(self.data, "2026-08-01", 3)
        statuses = ["approve", "skip", "manual_violation"]
        # markdown path
        md = rrd.render(payload)
        for i, st in enumerate(statuses, 1):
            block = md.split(f"### Candidate {i}\n", 1)
            block[1] = block[1].replace(f"- [ ] {st} ", f"- [x] {st} ", 1)
            md = f"### Candidate {i}\n".join(block)
        md_reviewed = phr.parse(md)
        md_merged = [{**payload["candidates"][r["candidate_index"] - 1], "status": r["status"]} for r in md_reviewed]
        # visual path
        doc = _doc({"2026-08-01": {"axiom_id": "a09", "count": 3,
                                    "decisions": [{"candidate_index": i, "status": s} for i, s in enumerate(statuses, 1)]}})
        writes, notes = irj.plan(doc, self.data)
        self.assertEqual(notes, [])
        (path, body), = writes
        self.assertEqual(path.name, "2026-08-01_human_review.json")
        self.assertEqual(set(body), {"axiom_id", "scan_date", "reviewed_at", "reviewed"})
        self.assertEqual(body["reviewed"], md_merged)

    def test_partial_batch_skipped_complete_batch_written(self) -> None:
        _write(self.data, "2026-08-01", 2)
        _write(self.data, "2026-08-08", 2)
        doc = _doc({
            "2026-08-01": {"axiom_id": "a09", "count": 2, "decisions": [{"candidate_index": 1, "status": "skip"}]},
            "2026-08-08": {"axiom_id": "a09", "count": 2, "decisions": [
                {"candidate_index": 1, "status": "skip"}, {"candidate_index": 2, "status": "approve"}]},
        })
        writes, notes = irj.plan(doc, self.data)
        self.assertEqual([p.name for p, _ in writes], ["2026-08-08_human_review.json"])
        self.assertTrue(any("1/2" in n for n in notes))

    def test_any_malformed_decision_writes_nothing(self) -> None:
        _write(self.data, "2026-08-01", 2)
        _write(self.data, "2026-08-08", 1)
        good = {"axiom_id": "a09", "count": 1, "decisions": [{"candidate_index": 1, "status": "skip"}]}
        for bad in (
            {"axiom_id": "a09", "count": 2, "decisions": [{"candidate_index": 3, "status": "skip"}]},
            {"axiom_id": "a09", "count": 2, "decisions": [{"candidate_index": 1, "status": "maybe"}]},
            {"axiom_id": "a09", "count": 2, "decisions": [{"candidate_index": 1, "status": "skip"},
                                                           {"candidate_index": 1, "status": "approve"}]},
            {"axiom_id": "t10", "count": 2, "decisions": []},
            {"axiom_id": "a09", "count": 5, "decisions": []},
        ):
            with self.subTest(bad=bad), self.assertRaises(irj.ReviewImportError):
                irj.plan(_doc({"2026-08-01": bad, "2026-08-08": good}), self.data)
        with self.assertRaises(irj.ReviewImportError):
            irj.plan({"schema": "other", "batches": {}}, self.data)

    def test_never_overwrites_without_force(self) -> None:
        _write(self.data, "2026-08-01", 1)
        (self.data / "2026-08-01_human_review.json").write_text('{"keep": true}')
        doc = _doc({"2026-08-01": {"axiom_id": "a09", "count": 1, "decisions": [{"candidate_index": 1, "status": "skip"}]}})
        writes, notes = irj.plan(doc, self.data)
        self.assertEqual(writes, [])
        self.assertTrue(any("--force" in n for n in notes))
        self.assertEqual(len(irj.plan(doc, self.data, force=True)[0]), 1)

    def test_cli_dry_run_writes_nothing(self) -> None:
        _write(self.data, "2026-08-01", 1)
        f = self.data.parent / "export.json"
        f.write_text(json.dumps(_doc({"2026-08-01": {"axiom_id": "a09", "count": 1,
                                                      "decisions": [{"candidate_index": 1, "status": "skip"}]}})))
        argv = ["import_review_json.py", str(f), "--data-dir", str(self.data), "--dry-run"]
        with mock.patch.object(sys, "argv", argv):
            self.assertEqual(irj.main(), 0)
        self.assertFalse((self.data / "2026-08-01_human_review.json").exists())


if __name__ == "__main__":
    unittest.main()
