"""Public entry-point checks for Python Unicode whitespace semantics."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class ProspectiveWordContractTests(unittest.TestCase):
    def test_file_separator_is_a_word_separator_in_public_api(self):
        from textstats import TextStats, count_file, count_text
        sample = "alpha\x1cbeta\n"
        self.assertEqual(count_text(sample), TextStats(1, 2))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(sample.encode("utf-8"))
            self.assertEqual(count_file(path), TextStats(1, 2))

    def test_file_separator_is_a_word_separator_in_real_module(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            data = b"alpha\x1cbeta\n"
            path.write_bytes(data)
            result = subprocess.run([sys.executable, "-B", "-m", "textstats", str(path)], capture_output=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, b"lines=1 words=2\n")
            self.assertEqual(result.stderr, b"")
            self.assertEqual(path.read_bytes(), data)
