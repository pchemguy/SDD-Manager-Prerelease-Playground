"""Verify the delivered whole-text facade without claiming file API delivery."""

import contextlib
import importlib
import inspect
import io
import subprocess
import sys
import unittest

import textstats
from textstats import TextStats, count_text


class TextApiTests(unittest.TestCase):
    def test_direct_imports_and_delivered_exports(self):
        self.assertIs(textstats.TextStats, TextStats)
        self.assertIs(textstats.count_text, count_text)
        self.assertEqual(set(textstats.__all__), {"TextStats", "count_text"})
        self.assertFalse(hasattr(textstats, "count_file"))

    def test_signatures_and_keyword_only_policy(self):
        stats_parameters = inspect.signature(TextStats).parameters
        self.assertEqual(list(stats_parameters), ["lines", "words"])
        self.assertTrue(all(p.default is inspect.Parameter.empty for p in stats_parameters.values()))
        signature = inspect.signature(count_text)
        self.assertEqual(list(signature.parameters), ["text", "strip_bom"])
        self.assertIs(signature.parameters["strip_bom"].kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(signature.parameters["strip_bom"].default, True)
        annotations = inspect.get_annotations(count_text, eval_str=True)
        self.assertEqual(annotations, {"text": str, "strip_bom": bool, "return": TextStats})
        with self.assertRaises(TypeError):
            count_text("abc", False)

    def test_public_default_and_retaining_policy(self):
        self.assertEqual(count_text("\ufeff"), TextStats(0, 0))
        self.assertEqual(count_text("\ufeff", strip_bom=False), TextStats(1, 1))
        self.assertEqual(count_text("α\r\n猫\rβ γ\n"), TextStats(3, 4))

    def test_calls_and_reload_are_silent(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            importlib.reload(textstats)
            for value in ["", "\ufeff", "a\r\nb", "a\u2029b"]:
                count_text(value)
                count_text(value, strip_bom=False)
            TextStats(0, 0)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_initial_import_is_silent_in_fresh_process(self):
        result = subprocess.run([sys.executable, "-c", "import textstats"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
