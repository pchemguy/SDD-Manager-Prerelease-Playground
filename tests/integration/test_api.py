"""Direct public text API signatures, values, silence and input preservation."""

import contextlib
import inspect
import io
import subprocess
import sys
import unittest


class TextApiTests(unittest.TestCase):
    def test_direct_exports_and_keyword_only_policy(self):
        from textstats import TextStats, count_text
        signature = inspect.signature(count_text)
        self.assertEqual(list(signature.parameters), ["text", "strip_bom"])
        self.assertIs(signature.parameters["strip_bom"].kind,
                      inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(signature.parameters["strip_bom"].default, True)
        self.assertEqual(list(inspect.signature(TextStats).parameters), ["lines", "words"])
        with self.assertRaises(TypeError):
            count_text("alpha", False)
        self.assertIsInstance(count_text("alpha"), TextStats)

    def test_fresh_process_import_and_calls_are_silent(self):
        result = subprocess.run(
            [sys.executable, "-B", "-c",
             "from textstats import TextStats, count_text; "
             "assert count_text('alpha') == TextStats(1, 1)"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_public_api_silence_and_unchanged_input(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            from textstats import TextStats, count_text
            text = "\ufeffcafé\r\n茶\u2028beta\n"
            original = text.encode("utf-8")
            self.assertEqual(count_text(text), TextStats(2, 3))
            self.assertEqual(count_text(text, strip_bom=False), TextStats(2, 3))
            self.assertEqual(text.encode("utf-8"), original)
            self.assertEqual(count_text("\ufeff"), TextStats(0, 0))
            self.assertEqual(count_text("\ufeff", strip_bom=False), TextStats(1, 1))
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
