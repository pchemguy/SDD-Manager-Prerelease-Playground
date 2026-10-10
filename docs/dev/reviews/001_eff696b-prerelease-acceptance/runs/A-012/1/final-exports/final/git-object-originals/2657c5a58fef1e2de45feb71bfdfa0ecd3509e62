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
    def test_json_matrix_matches_api_and_retained_text(self):
        cases = [('', (0, 0), (0, 0)), ('α\r\n猫\rβ γ\n', (3, 4), (3, 4)),
                 ('\ufeff', (0, 0), (1, 1)), ('\ufeff\ufeff', (1, 1), (1, 1)),
                 ('alpha\u2028beta', (1, 2), (1, 2)), ('alpha\n\n', (2, 1), (2, 1)),
                 ('a\ufeffb', (1, 1), (1, 1))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            for text, default, retained in cases:
                raw = text.encode('utf-8')
                path.write_bytes(raw)
                for options, expected in [([], default), (['--keep-bom'], retained)]:
                    for args in [['--json', *options, str(path)], [str(path), *options, '--json']]:
                        with self.subTest(text=text, args=args):
                            result = self.invoke(*args)
                            self.assertEqual((result.returncode, result.stderr), (0, ''))
                            self.assertTrue(result.stdout.endswith('\n'))
                            self.assertEqual(result.stdout.count('\n'), 1)
                            payload = json.loads(result.stdout)
                            self.assertEqual(payload, {'lines': expected[0], 'words': expected[1]})
                            self.assertTrue(all(type(value) is int for value in payload.values()))
                            self.assertEqual(count_file(path, strip_bom=not options), TextStats(*expected))
                    result = self.invoke(*options, str(path))
                    self.assertEqual((result.returncode, result.stdout, result.stderr),
                                     (0, f'lines={expected[0]} words={expected[1]}\n', ''))
                    self.assertEqual(path.read_bytes(), raw)

    def test_json_errors_help_and_option_named_file(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / 'bad.txt'
            bad.write_bytes(b'valid\n\xff')
            for path in [bad, Path(directory) / 'missing.txt']:
                result = self.invoke('--json', str(path))
                self.assertEqual((result.returncode, result.stdout), (1, ''))
                self.assertIn(str(path), result.stderr)
                self.assertNotIn('Traceback', result.stderr)
            for args in [['--json'], ['--json', 'one', 'two'], ['--json', '--unknown', 'missing'], ['--j', 'missing']]:
                result = self.invoke(*args)
                self.assertEqual((result.returncode, result.stdout), (2, ''))
                self.assertIn('usage:', result.stderr)
            option_file = Path(directory) / '--json'
            option_file.write_bytes(b'alpha beta\n')
            result = self.invoke('--json', '--', '--json', cwd=directory)
            self.assertEqual((result.returncode, result.stderr), (0, ''))
            self.assertEqual(json.loads(result.stdout), {'lines': 1, 'words': 2})
        result = self.invoke('--help')
        self.assertEqual((result.returncode, result.stderr), (0, ''))
        self.assertIn('--json', result.stdout)

    def invoke(self, *args, cwd=ROOT):
        return subprocess.run([sys.executable, '-m', 'textstats', *args], cwd=cwd, env={**os.environ, 'PYTHONPATH': str(ROOT)}, capture_output=True, text=True)

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
