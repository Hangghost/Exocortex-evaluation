#!/usr/bin/env python3
"""Tests for the historical-window rescan feature in scan_axiom_usage.py.

Covers: label/window consistency refusal, overwrite protection, and
--since/--until window slicing. Run with `python3 tools/test_scan_axiom_usage.py`.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import scan_axiom_usage as sau  # noqa: E402


class ComputeWindowTests(unittest.TestCase):
    def test_default_no_date_uses_now_as_until(self):
        before = datetime.now(timezone.utc)
        label, cutoff, until = sau.compute_window(None, 7, None, None, None)
        after = datetime.now(timezone.utc)
        self.assertEqual(label, datetime.now().strftime("%Y-%m-%d"))
        self.assertTrue(before <= until <= after)
        self.assertEqual(until - cutoff, timedelta(days=7))

    def test_date_sets_label_and_until_together(self):
        label, cutoff, until = sau.compute_window("2026-07-19", 7, None, None, None)
        self.assertEqual(label, "2026-07-19")
        self.assertEqual(until, datetime(2026, 7, 20, tzinfo=timezone.utc))
        self.assertEqual(cutoff, datetime(2026, 7, 13, tzinfo=timezone.utc))

    def test_date_and_matching_until_ok(self):
        label, cutoff, until = sau.compute_window("2026-07-19", 7, None, "2026-07-19", None)
        self.assertEqual(label, "2026-07-19")
        self.assertEqual(until, datetime(2026, 7, 20, tzinfo=timezone.utc))

    def test_date_and_conflicting_until_refuses(self):
        with self.assertRaises(sau.WindowError):
            sau.compute_window("2026-07-19", 7, None, "2026-07-20", None)

    def test_explicit_since_until(self):
        label, cutoff, until = sau.compute_window(None, 7, "2026-06-01", "2026-06-10", None)
        self.assertEqual(label, "2026-06-10")
        self.assertEqual(cutoff, datetime(2026, 6, 1, tzinfo=timezone.utc))
        self.assertEqual(until, datetime(2026, 6, 11, tzinfo=timezone.utc))

    def test_since_not_before_until_refuses(self):
        with self.assertRaises(sau.WindowError):
            sau.compute_window(None, 7, "2026-06-15", "2026-06-10", None)

    def test_applies_from_floors_cutoff(self):
        applies_from = datetime(2026, 7, 16, tzinfo=timezone.utc)
        label, cutoff, until = sau.compute_window("2026-07-19", 7, None, None, applies_from)
        self.assertEqual(cutoff, applies_from)

    def test_invalid_date_format_refuses(self):
        with self.assertRaises(sau.WindowError):
            sau.compute_window("07-19-2026", 7, None, None, None)


class CheckOverwriteTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name) / "2026-07-19_candidates.json"
        self.cutoff = datetime(2026, 7, 13, tzinfo=timezone.utc)
        self.until = datetime(2026, 7, 20, tzinfo=timezone.utc)

    def test_missing_file_ok(self):
        sau.check_overwrite(self.out, self.cutoff, self.until, force=False)

    def test_matching_window_ok(self):
        self.out.write_text(json.dumps({
            "effective_cutoff": self.cutoff.isoformat(),
            "window_until": self.until.isoformat(),
        }))
        sau.check_overwrite(self.out, self.cutoff, self.until, force=False)

    def test_different_window_refuses_without_force(self):
        self.out.write_text(json.dumps({
            "effective_cutoff": self.cutoff.isoformat(),
            "window_until": self.until.isoformat(),
        }))
        new_cutoff = datetime(2026, 7, 26, tzinfo=timezone.utc)
        new_until = datetime(2026, 8, 2, tzinfo=timezone.utc)
        with self.assertRaises(sau.OverwriteRefused):
            sau.check_overwrite(self.out, new_cutoff, new_until, force=False)

    def test_different_window_with_force_ok(self):
        self.out.write_text(json.dumps({
            "effective_cutoff": self.cutoff.isoformat(),
            "window_until": self.until.isoformat(),
        }))
        new_cutoff = datetime(2026, 7, 26, tzinfo=timezone.utc)
        new_until = datetime(2026, 8, 2, tzinfo=timezone.utc)
        sau.check_overwrite(self.out, new_cutoff, new_until, force=True)


class MainIntegrationTests(unittest.TestCase):
    """Exercises main() end-to-end with a fixture transcript and a mocked
    transcript environment, so no real ~/.claude/projects data is touched."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.tmp_path = Path(self.tmp.name)
        self.output_dir = self.tmp_path / "data"
        self.jsonl = self.tmp_path / "session1.jsonl"

        def rec(ts: str, cmd: str) -> str:
            return json.dumps({
                "timestamp": ts,
                "message": {
                    "content": [
                        {"type": "tool_use", "name": "Bash", "input": {"command": cmd}}
                    ]
                },
            })

        lines = [
            rec("2026-06-05T00:00:00Z", "git checkout -b feature/before main"),
            rec("2026-06-10T00:00:00Z", "git checkout -b feature/in-window main"),
            rec("2026-06-15T00:00:00Z", "git checkout -b feature/in-window-violation"),
            rec("2026-06-20T00:00:00Z", "git checkout -b feature/after main"),
        ]
        self.jsonl.write_text("\n".join(lines) + "\n", encoding="utf-8")

        patchers = [
            mock.patch.object(sau, "enumerate_transcript_dirs", return_value=[self.tmp_path]),
            mock.patch.object(sau, "iter_transcripts", return_value=[self.jsonl]),
            mock.patch.object(sau, "read_applies_from", return_value=None),
        ]
        for p in patchers:
            p.start()
            self.addCleanup(p.stop)

    def run_main(self, extra_args: list[str]) -> int:
        argv = [
            "scan_axiom_usage.py",
            "--axiom", "a09",
            "--exocortex-root", str(self.tmp_path),
            "--output-dir", str(self.output_dir),
        ] + extra_args
        with mock.patch.object(sys, "argv", argv):
            return sau.main()

    def test_since_until_slices_window(self):
        rc = self.run_main(["--since", "2026-06-08", "--until", "2026-06-16"])
        self.assertEqual(rc, 0)
        out = self.output_dir / "2026-06-16_candidates.json"
        payload = json.loads(out.read_text())
        self.assertEqual(payload["total_candidates"], 2)
        self.assertEqual(payload["effective_cutoff"], datetime(2026, 6, 8, tzinfo=timezone.utc).isoformat())
        self.assertEqual(payload["window_until"], datetime(2026, 6, 17, tzinfo=timezone.utc).isoformat())
        commands = {c["command"] for c in payload["candidates"]}
        self.assertEqual(commands, {"git checkout -b feature/in-window main", "git checkout -b feature/in-window-violation"})

    def test_date_until_mismatch_refuses_before_writing(self):
        rc = self.run_main(["--date", "2026-06-16", "--until", "2026-06-17"])
        self.assertEqual(rc, 4)
        self.assertFalse((self.output_dir / "2026-06-16_candidates.json").exists())
        self.assertFalse((self.output_dir / "2026-06-17_candidates.json").exists())

    def test_overwrite_refused_without_force(self):
        rc1 = self.run_main(["--since", "2026-06-08", "--until", "2026-06-16"])
        self.assertEqual(rc1, 0)
        out = self.output_dir / "2026-06-16_candidates.json"
        original = out.read_text()

        rc2 = self.run_main(["--since", "2026-06-01", "--until", "2026-06-16"])
        self.assertEqual(rc2, 5)
        self.assertEqual(out.read_text(), original)

    def test_overwrite_with_force_succeeds(self):
        rc1 = self.run_main(["--since", "2026-06-08", "--until", "2026-06-16"])
        self.assertEqual(rc1, 0)
        out = self.output_dir / "2026-06-16_candidates.json"

        rc2 = self.run_main(["--since", "2026-06-01", "--until", "2026-06-16", "--force"])
        self.assertEqual(rc2, 0)
        payload = json.loads(out.read_text())
        self.assertEqual(payload["effective_cutoff"], datetime(2026, 6, 1, tzinfo=timezone.utc).isoformat())


if __name__ == "__main__":
    unittest.main()
