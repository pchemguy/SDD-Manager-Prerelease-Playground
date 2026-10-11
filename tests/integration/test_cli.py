"""Real module-entry named-file checks with exact process streams and bytes."""

import os
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from textstats import TextStats, count_file

ROOT = Path(__file__).resolve().parents[2]


class ModuleCliTests(unittest.TestCase):
    def test_json_semantic_matrix_and_option_composition(self):
        cases = [("", (0, 0), (0, 0)), ("alpha beta", (1, 2), (1, 2)),
                 ("alpha\n", (1, 1), (1, 1)), ("\n", (1, 0), (1, 0)),
                 ("α\r\n猫\rβ γ\n", (3, 4), (3, 4)), ("alpha\n\n", (2, 1), (2, 1)),
                 (" \t", (1, 0), (1, 0)), ("alpha\u2028beta", (1, 2), (1, 2)),
                 ("\ufeff", (0, 0), (1, 1)), ("\ufeff\ufeff", (1, 1), (1, 1)),
                 ("\ufeffalpha beta", (1, 2), (1, 2)), ("a\ufeffb", (1, 1), (1, 1)),
                 ("\r\n", (1, 0), (1, 0)), ("\r", (1, 0), (1, 0))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            for text, default, retained in cases:
                raw = text.encode("utf-8")
                path.write_bytes(raw)
                choices = [(["--json", str(path)], True, default),
                           ([str(path), "--json"], True, default),
                           (["--json", "--keep-bom", str(path)], False, retained),
                           (["--keep-bom", str(path), "--json"], False, retained),
                           ([str(path), "--json", "--keep-bom"], False, retained)]
                for args, policy, expected in choices:
                    with self.subTest(text=text, args=args):
                        result = self.invoke(*args)
                        self.assertEqual((result.returncode, result.stderr), (0, ""))
                        self.assertEqual(result.stdout.count("\n"), 1)
                        self.assertTrue(result.stdout.endswith("\n"))
                        value = json.loads(result.stdout)
                        self.assertEqual(set(value), {"lines", "words"})
                        self.assertTrue(all(type(count) is int for count in value.values()))
                        self.assertEqual((value["lines"], value["words"]), expected)
                        self.assertEqual(count_file(path, strip_bom=policy), TextStats(*expected))
                        text_result = self.invoke(*([] if policy else ["--keep-bom"]), str(path))
                        self.assertEqual((text_result.returncode, text_result.stdout, text_result.stderr),
                                         (0, f"lines={expected[0]} words={expected[1]}\n", ""))
                        self.assertEqual(path.read_bytes(), raw)

    def test_json_errors_retain_status_streams_and_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "bad.txt"
            bad.write_bytes(b"valid prefix\n\xff")
            for path, cause in [(bad, "utf-8"), (bad.with_name("absent.txt"), "No such file")]:
                for options in [["--json"], ["--keep-bom", "--json"]]:
                    with self.subTest(path=path, options=options):
                        result = self.invoke(*options, str(path))
                        self.assertEqual((result.returncode, result.stdout), (1, ""))
                        self.assertIn(str(path), result.stderr)
                        self.assertIn(cause, result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(bad.read_bytes(), b"valid prefix\n\xff")
        for args in [["--json"], ["--json", "one", "two"],
                     ["--json", "--unknown", "missing"], ["--j", "missing"]]:
            result = self.invoke(*args)
            self.assertEqual((result.returncode, result.stdout), (2, ""))
            self.assertIn("usage:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_json_option_like_filename_after_double_dash(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "--json"
            path.write_bytes(b"alpha beta\n")
            result = self.invoke("--json", "--", "--json", cwd=directory)
            self.assertEqual((result.returncode, result.stderr), (0, ""))
            self.assertEqual(json.loads(result.stdout), {"lines": 1, "words": 2})
            text_result = self.invoke("--", "--json", cwd=directory)
            self.assertEqual((text_result.returncode, text_result.stdout, text_result.stderr),
                             (0, "lines=1 words=2\n", ""))
            self.assertEqual(path.read_bytes(), b"alpha beta\n")

    def invoke(self, *args, cwd=ROOT):
        return subprocess.run([sys.executable, "-B", '-m', 'textstats', *args], cwd=cwd, env={**os.environ, 'PYTHONPATH': str(ROOT)}, capture_output=True, text=True)

    def test_named_file_matrix_and_bom_option_order(self):
        cases = [('', (0, 0), (0, 0)), ('α\r\n猫\rβ γ\n', (3, 4), (3, 4)), ('\ufeff', (0, 0), (1, 1)), ('\ufeff\ufeff', (1, 1), (1, 1)), ('alpha\u2028beta', (1, 2), (1, 2)), ('a\n\n', (2, 1), (2, 1))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            for text, default, retained in cases:
                raw = text.encode('utf-8')
                path.write_bytes(raw)
                for args, policy, expected in [( [str(path)], True, default), (['--keep-bom', str(path)], False, retained), ([str(path), '--keep-bom'], False, retained)]:
                    with self.subTest(text=text, args=args):
                        result = self.invoke(*args)
                        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, f'lines={expected[0]} words={expected[1]}\n', ''))
                        self.assertEqual(count_file(path, strip_bom=policy), TextStats(*expected))
                        self.assertEqual(path.read_bytes(), raw)

    def test_help_without_input(self):
        for option in ['-h', '--help']:
            result = self.invoke(option)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, '')
            self.assertIn('usage:', result.stdout)
            self.assertIn('--keep-bom', result.stdout)
            self.assertIn('--json', result.stdout)
            self.assertIn('INPUT', result.stdout)

    def test_dash_filenames_and_double_dash_termination(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ['-sample', '--keep-bom', '-']:
                path = Path(directory) / name
                path.write_bytes(b'alpha beta\n')
                result = self.invoke('--', name, cwd=directory)
                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, 'lines=1 words=2\n', ''))
                self.assertEqual(path.read_bytes(), b'alpha beta\n')

    def test_exactly_one_input_is_required(self):
        for args in [[], ['one', 'two']]:
            result = self.invoke(*args)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, '')
            self.assertIn('usage:', result.stderr)

    def test_missing_and_invalid_utf8_are_clean_input_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / 'absent.txt'
            bad = Path(directory) / 'bad.txt'
            bad.write_bytes(b'valid prefix\n\xff')
            for path, cause in [(missing, 'No such file'), (bad, 'utf-8')]:
                for options in [[], ['--keep-bom']]:
                    with self.subTest(path=path, options=options):
                        result = self.invoke(*options, str(path))
                        self.assertEqual((result.returncode, result.stdout), (1, ''))
                        self.assertIn(str(path), result.stderr)
                        self.assertIn(cause, result.stderr)
                        self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(bad.read_bytes(), b'valid prefix\n\xff')

    def test_unknown_option_is_usage_even_with_missing_input(self):
        for option in ['--unknown', '--keep']:
            with self.subTest(option=option):
                result = self.invoke(option, 'nonexistent.txt')
                self.assertEqual((result.returncode, result.stdout), (2, ''))
                self.assertIn('usage:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)
