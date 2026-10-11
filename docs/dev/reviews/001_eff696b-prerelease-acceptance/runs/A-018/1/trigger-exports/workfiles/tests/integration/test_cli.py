"""Real module-entry named-file checks with exact process streams and bytes."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from textstats import TextStats, count_file

ROOT = Path(__file__).resolve().parents[2]


class ModuleCliTests(unittest.TestCase):
    def invoke(self, *args, cwd=ROOT):
        return subprocess.run([sys.executable, '-B', '-m', 'textstats', *args], cwd=cwd, env={**os.environ, 'PYTHONPATH': str(ROOT)}, capture_output=True, text=True)

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
        for args in [[], ['one', 'two'], ['--unknown', 'missing']]:
            result = self.invoke(*args)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, '')
            self.assertIn('usage:', result.stderr)

    def test_long_option_abbreviations_have_usage_status(self):
        with tempfile.TemporaryDirectory() as directory:
            valid = Path(directory) / 'valid.txt'
            missing = Path(directory) / 'missing.txt'
            raw = b'alpha beta\n'
            valid.write_bytes(raw)
            for option in ['--keep', '--keep-bo', '--hel']:
                for path in [valid, missing]:
                    for args in [[option, str(path)], [str(path), option]]:
                        with self.subTest(args=args):
                            result = self.invoke(*args)
                            self.assertEqual(result.returncode, 2)
                            self.assertEqual(result.stdout, '')
                            self.assertIn('usage:', result.stderr)
                            self.assertIn(option, result.stderr)
                            self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(valid.read_bytes(), raw)
            self.assertFalse(missing.exists())

    def test_missing_and_invalid_utf8_files_have_input_failure_status(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / 'missing.txt'
            invalid = Path(directory) / 'invalid.txt'
            raw = b'valid\n\xff'
            invalid.write_bytes(raw)
            for path, cause in [(missing, 'No such file'), (invalid, 'utf-8')]:
                for args in [[str(path)], ['--keep-bom', str(path)]]:
                    with self.subTest(args=args):
                        result = self.invoke(*args)
                        self.assertEqual(result.returncode, 1)
                        self.assertEqual(result.stdout, '')
                        self.assertIn(str(path), result.stderr)
                        self.assertIn(cause, result.stderr)
                        self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(invalid.read_bytes(), raw)
            self.assertFalse(missing.exists())
