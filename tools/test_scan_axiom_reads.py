#!/usr/bin/env python3
"""Tests for Bash-read counting and entrypoint split in scan_axiom_reads.py.

Run with `python3 tools/test_scan_axiom_reads.py`.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import scan_axiom_reads as sar  # noqa: E402

KNOWN = ["INDEX.md", "a01_foo.md", "a02_bar.md", "v02_signal.md", "v03_other.md", "v04_x.md"]


class BashAxiomReadsTests(unittest.TestCase):
    def test_for_loop_cat_over_explicit_files(self):
        cmd = (
            "for f in rules/axioms/INDEX.md rules/axioms/a01_foo.md; "
            'do echo "=== $f ==="; cat "$f"; done'
        )
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), {"INDEX.md", "a01_foo.md"})

    def test_for_loop_over_small_glob(self):
        cmd = "for f in rules/axioms/v0[23]_*.md; do cat $f; done"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), {"v02_signal.md", "v03_other.md"})

    def test_pipeline_first_stage_print_verb(self):
        cmd = "cat rules/axioms/INDEX.md | head -40"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), {"INDEX.md"})

    def test_cd_then_relative_cat(self):
        cmd = "cd rules/axioms && cat INDEX.md a01_foo.md"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), {"INDEX.md", "a01_foo.md"})

    def test_grep_search_is_not_a_read(self):
        cmd = "grep -rn 'silent' rules/axioms/"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), set())

    def test_ls_and_wc_are_not_reads(self):
        self.assertEqual(sar.bash_axiom_reads("ls rules/axioms/ | wc -l", KNOWN), set())

    def test_pipeline_where_verb_is_not_first_stage(self):
        cmd = "ls rules/axioms/ | head -5"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), set())

    def test_wide_glob_is_a_directory_scan(self):
        cmd = "cat rules/axioms/*.md"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), set())

    def test_write_target_is_excluded(self):
        cmd = "cat /tmp/new.md > rules/axioms/a01_foo.md"
        self.assertEqual(sar.bash_axiom_reads(cmd, KNOWN), set())

    def test_command_without_axioms_is_ignored(self):
        self.assertEqual(sar.bash_axiom_reads("cat README.md", KNOWN), set())


def _write_transcript(path: Path, entrypoint: str, commands: list[tuple[str, dict]]) -> None:
    records = [{"type": "user", "entrypoint": entrypoint, "message": {"content": "hi"}}]
    for tool, tool_input in commands:
        records.append(
            {
                "type": "assistant",
                "entrypoint": entrypoint,
                "message": {
                    "content": [{"type": "tool_use", "name": tool, "input": tool_input}]
                },
            }
        )
    path.write_text("\n".join(json.dumps(r) for r in records), encoding="utf-8")


class ScanTranscriptTests(unittest.TestCase):
    def test_bash_read_counts_and_entrypoint_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.jsonl"
            _write_transcript(
                p,
                "cli",
                [
                    (
                        "Bash",
                        {"command": "for f in rules/axioms/INDEX.md; do cat $f; done"},
                    ),
                    ("Bash", {"command": "grep -rn x rules/axioms/"}),
                    ("Read", {"file_path": "/r/rules/axioms/a01_foo.md"}),
                ],
            )
            hits, read_index, entrypoint = sar.scan_transcript(p, KNOWN)
        self.assertTrue(read_index)
        self.assertEqual(dict(hits), {"a01_foo.md": 1})
        self.assertEqual(entrypoint, "cli")

    def test_missing_entrypoint_is_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.jsonl"
            p.write_text(json.dumps({"type": "user", "message": {"content": "x"}}))
            _, _, entrypoint = sar.scan_transcript(p, KNOWN)
        self.assertEqual(entrypoint, sar.UNKNOWN_ENTRYPOINT)

    def test_sdk_cli_is_pipeline(self):
        self.assertIn("sdk-cli", sar.PIPELINE_ENTRYPOINTS)
        self.assertNotIn("cli", sar.PIPELINE_ENTRYPOINTS)


if __name__ == "__main__":
    unittest.main()
