#!/usr/bin/env python3
"""Behavior tests for the de-slop linter."""

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "lint_text.py"
SPEC = importlib.util.spec_from_file_location("lint_text", SCRIPT_PATH)
LINT_TEXT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(LINT_TEXT)


def codes(text: str, include_code: bool = False):
    return [item.code for item in LINT_TEXT.lint(text, include_code=include_code)]


class LintTextTests(unittest.TestCase):
    def test_clean_copy_passes(self):
        text = (
            "The dashboard shows failed jobs and the owner of each one. "
            "Open a job to view its logs or retry it."
        )
        self.assertEqual(codes(text), [])

    def test_hard_rules_are_flagged(self):
        text = (
            "It is not just a dashboard, but a command center \u2014 "
            "one that changes everything."
        )
        found = codes(text)
        self.assertIn("DS001", found)
        self.assertIn("DS002", found)
        self.assertEqual(found.count("DS002"), 1)
        self.assertNotIn("DS003", found)

    def test_repeated_negation_is_flagged(self):
        text = "No delay. No confusion. Just results."
        self.assertIn("DS004", codes(text))

    def test_inline_and_fenced_code_are_ignored_by_default(self):
        text = (
            "Use `not just x, but y` as a test fixture.\n"
            "```text\n"
            "Here is the thing \u2014 this is sample input.\n"
            "```\n"
            "The final copy is direct."
        )
        self.assertEqual(codes(text), [])
        found_with_code = codes(text, include_code=True)
        self.assertIn("DS001", found_with_code)
        self.assertIn("DS002", found_with_code)

    def test_generic_closer_is_flagged(self):
        self.assertIn(
            "DS021",
            codes("The export is ready. If you would like, I can explain more."),
        )

    def test_duplicate_paragraph_is_flagged(self):
        paragraph = "The release adds alerts and saved filters for every account."
        text = paragraph + "\n\n" + paragraph
        self.assertIn("DS090", codes(text))

    def test_watchword_density_requires_multiple_terms(self):
        text = (
            "This robust platform showcases an intricate landscape. "
            "It can streamline work and foster collaboration."
        )
        self.assertIn("DS070", codes(text))
        self.assertNotIn("DS070", codes("The parser is robust under packet loss."))

    def test_heading_density_is_flagged(self):
        text = (
            "# Overview\nOne sentence.\n\n"
            "## What Changes Now\nOne sentence.\n\n"
            "## Why This Matters\nOne sentence."
        )
        self.assertIn("DS080", codes(text))

    def test_separate_short_lists_do_not_form_one_long_list(self):
        text = (
            "- One\n\n- Two\n\nA paragraph separates the lists.\n\n"
            "- Three\n\n- Four\n\n- Five\n\n- Six\n\n- Seven\n\n- Eight"
        )
        self.assertNotIn("DS081", codes(text))


if __name__ == "__main__":
    unittest.main()
