"""Real module-entry named-file checks with exact process streams and bytes."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from textstats import TextStats, count_file

ROOT = Path(__file__).resolve().parents[2]


class StdinModuleTests(unittest.TestCase):
    def invoke(self, args, raw, *, locale='C', cwd=ROOT):
        return subprocess.run([sys.executable, '-B', '-m', 'textstats', *args], input=raw,
                              cwd=cwd, env={**os.environ, 'PYTHONPATH': str(ROOT),
                              'PYTHONDONTWRITEBYTECODE': '1', 'LC_ALL': locale,
                              'PYTHONUTF8': '0', 'PYTHONCOERCECLOCALE': '0'}, capture_output=True)

    def assert_counts(self, args, raw, expected, **kwargs):
        result = self.invoke(args, raw, **kwargs)
        self.assertEqual((result.returncode, result.stdout, result.stderr),
                         (0, f'lines={expected[0]} words={expected[1]}\n'.encode(), b''))

    def test_binary_stdin_matrix_is_independent_of_text_locale(self):
        cases = [('', (0, 0), (0, 0)), ('α\r\n猫\rβ γ\n', (3, 4), (3, 4)),
                 ('\ufeff', (0, 0), (1, 1)), ('\ufeff\ufeff', (1, 1), (1, 1)),
                 ('alpha\u2028beta', (1, 2), (1, 2)), ('a\n\n', (2, 1), (2, 1))]
        for locale in ['C', 'C.UTF-8']:
            for text, default, retained in cases:
                for args, expected in [(['-'], default), (['--keep-bom', '-'], retained),
                                       (['-', '--keep-bom'], retained)]:
                    with self.subTest(locale=locale, text=text, args=args):
                        self.assert_counts(args, text.encode(), expected, locale=locale)

    def test_stdin_range_anchors_and_both_spellings(self):
        anchors = [('alpha beta\nbeta\nlast two', '2:3', (2, 3), (2, 3)),
                   ('alpha beta\nbeta\nlast two', '2:99', (2, 3), (2, 3)),
                   ('alpha beta\nbeta\nlast two', '4:99', (0, 0), (0, 0)),
                   ('a\n\n', '2:9', (1, 0), (1, 0)),
                   ('a\r\nb c\rd\n', '2:3', (2, 3), (2, 3)),
                   ('a\n\ufeff', '2:2', (1, 1), (1, 1)), ('', '1:99', (0, 0), (0, 0)),
                   ('\ufeff', '1:1', (0, 0), (1, 1)), ('\ufeff\ufeff', '1:1', (1, 1), (1, 1)),
                   ('alpha\u2028beta', '1:1', (1, 2), (1, 2)), ('\n', '1:1', (1, 0), (1, 0))]
        for text, endpoint, default, retained in anchors:
            for keep, expected in [(False, default), (True, retained)]:
                flags = ['--keep-bom'] if keep else []
                for spelling in [['--lines', endpoint], ['--lines=' + endpoint]]:
                    self.assert_counts([*flags, '-', *spelling], text.encode(), expected)

    def test_stdin_option_permutations_and_unbounded_endpoints(self):
        import itertools
        raw = b'alpha beta\nbeta\nlast two'
        for spelling in [('--lines', '2:3'), ('--lines=2:3',)]:
            for groups in itertools.permutations([spelling, ('--keep-bom',)]):
                for position in range(3):
                    ordered = list(groups)
                    ordered.insert(position, ('-',))
                    self.assert_counts([a for group in ordered for a in group], raw, (2, 3))
        huge = '9' * 5001
        for endpoint, expected in [('2:' + huge, (2, 3)), (huge + ':' + huge, (0, 0)),
                                   ('0' * 5000 + '2:' + '0' * 5000 + '3', (2, 3))]:
            for keep in [False, True]:
                for spelling in [['--lines', endpoint], ['--lines=' + endpoint]]:
                    self.assert_counts([*(['--keep-bom'] if keep else []), *spelling, '-'], raw, expected)

    def test_stdin_complete_decode_and_usage_failures(self):
        for args in [['-'], ['--keep-bom', '-'], ['--lines=1:1', '-']]:
            result = self.invoke(args, b'valid\n\xff')
            self.assertEqual((result.returncode, result.stdout), (1, b''))
            self.assertIn(b'stdin', result.stderr)
            self.assertIn(b'utf-8', result.stderr)
            self.assertNotIn(b'Traceback', result.stderr)
        for args in [['--json', '-'], ['--lines=0:1', '-'], ['-', 'extra'], ['--unknown', '-']]:
            result = self.invoke(args, b'\xff')
            self.assertEqual((result.returncode, result.stdout), (2, b''))
            self.assertIn(b'usage:', result.stderr)
            self.assertNotIn(b'Traceback', result.stderr)

    def test_explicit_dash_file_is_distinct_from_stdin(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '-'
            path.write_bytes(b'alpha beta\n')
            self.assert_counts(['./-'], b'', (1, 2), cwd=directory)
            self.assert_counts(['--lines=1:1', '--', './-'], b'other', (1, 2), cwd=directory)
            self.assert_counts(['--', '-'], b'other', (1, 1), cwd=directory)
            self.assertEqual(path.read_bytes(), b'alpha beta\n')


class ModuleCliTests(unittest.TestCase):
    def test_removed_json_usage_even_on_missing_or_undecodable_file(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / 'bad.txt'
            bad.write_bytes(b'valid\n\xff')
            for path in [bad, Path(directory) / 'missing.txt']:
                for option in ['--json', '--json=true', '--j']:
                    for args in [[option, str(path)], [str(path), option],
                                 ['--keep-bom', '--lines=1:1', str(path), option]]:
                        result = self.invoke(*args)
                        self.assertEqual((result.returncode, result.stdout), (2, ''))
                        self.assertIn('usage:', result.stderr)
                        self.assertIn('error:', result.stderr)
                        self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(bad.read_bytes(), b'valid\n\xff')
        help_result = self.invoke('--help')
        self.assertEqual((help_result.returncode, help_result.stderr), (0, ''))
        self.assertNotIn('--json', help_result.stdout)
        for flag in ['--keep-bom', '--lines', 'INPUT']:
            self.assertIn(flag, help_result.stdout)

    def test_literal_json_filename_in_whole_and_range_modes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '--json'
            raw = b'alpha beta\nbeta'
            path.write_bytes(raw)
            for args, expected in [(['--', '--json'], (2, 3)),
                                   (['--lines', '2:2', '--', '--json'], (1, 1)),
                                   (['--keep-bom', '--lines=1:1', '--', '--json'], (1, 2))]:
                result = self.invoke(*args, cwd=directory)
                self.assertEqual((result.returncode, result.stdout, result.stderr),
                                 (0, f'lines={expected[0]} words={expected[1]}\n', ''))
                self.assertEqual(path.read_bytes(), raw)

    def invoke(self, *args, cwd=ROOT):
        return subprocess.run([sys.executable, '-B', '-m', 'textstats', *args], cwd=cwd, env={**os.environ, 'PYTHONPATH': str(ROOT), 'PYTHONDONTWRITEBYTECODE': '1'}, capture_output=True, text=True)

    def test_named_file_matrix_and_bom_option_order(self):
        cases = [('', (0, 0), (0, 0)), ('α\r\n猫\rβ γ\n', (3, 4), (3, 4)), ('\ufeff', (0, 0), (1, 1)), ('\ufeff\ufeff', (1, 1), (1, 1)), ('alpha\u2028beta', (1, 2), (1, 2)), ('a\n\n', (2, 1), (2, 1)), ('a\ufeffb', (1, 1), (1, 1))]
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
                result = self.invoke('--', './-' if name == '-' else name, cwd=directory)
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


class RangeModuleTests(unittest.TestCase):
    invoke = ModuleCliTests.invoke

    def assert_counts(self, result, expected):
        self.assertEqual((result.returncode, result.stderr), (0, ''))
        self.assertTrue(result.stdout.endswith('\n'))
        self.assertEqual(result.stdout, f'lines={expected[0]} words={expected[1]}\n')

    def test_every_feature_anchor_text_and_bom_policy(self):
        cases = [('alpha beta\nbeta\nlast two', '2:3', (2, 3), (2, 3)), ('alpha beta\nbeta\nlast two', '2:99', (2, 3), (2, 3)), ('alpha beta\nbeta\nlast two', '1:1', (1, 2), (1, 2)), ('alpha beta\nbeta\nlast two', '0001:0001', (1, 2), (1, 2)), ('alpha beta\nbeta\nlast two', '4:99', (0, 0), (0, 0)), ('a\n\n', '2:9', (1, 0), (1, 0)), ('a\r\nb c\rd\n', '2:3', (2, 3), (2, 3)), ('a\n\ufeff', '2:2', (1, 1), (1, 1)), ('', '1:99', (0, 0), (0, 0)), ('\ufeff', '1:1', (0, 0), (1, 1)), ('\ufeff\ufeff', '1:1', (1, 1), (1, 1)), ('alpha\u2028beta', '1:1', (1, 2), (1, 2)), ('\n', '1:1', (1, 0), (1, 0))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            for text, value, default, retained in cases:
                raw = text.encode()
                path.write_bytes(raw)
                for keep in (False, True):
                    args = ['--lines=' + value, str(path)]
                    if keep:
                        args += ['--keep-bom']
                    with self.subTest(text=text, value=value, keep=keep):
                        self.assert_counts(self.invoke(*args), retained if keep else default)
                        self.assertEqual(path.read_bytes(), raw)

    def test_all_option_permutations_spellings_and_input_positions(self):
        import itertools
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            path.write_bytes(b'a\nb c\rd\n')
            for spelling in [['--lines', '2:3'], ['--lines=2:3']]:
                for keep in (False, True):
                    options = [spelling] + ([['--keep-bom']] if keep else [])
                    for order in itertools.permutations(options):
                        for position in range(len(order) + 1):
                            groups = list(order)
                            groups.insert(position, [str(path)])
                            args = [arg for group in groups for arg in group]
                            with self.subTest(args=args):
                                self.assert_counts(self.invoke(*args), (2, 3))

    def test_huge_and_leading_zero_endpoints(self):
        huge = '9' * 5001
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample'
            path.write_bytes(b'a\nb')
            for value, expected in [('1:' + huge, (2, 2)), (huge + ':' + huge, (0, 0)), ('0' * 5001 + '1:' + '0' * 5001 + '1', (1, 1))]:
                args = ['--lines', value, str(path)]
                self.assert_counts(self.invoke(*args), expected)

    def test_invalid_range_is_usage_on_missing_file_and_decode_after_end_is_input_failure(self):
        from tests.unit.test_cli import RangeCliTests
        with tempfile.TemporaryDirectory() as directory:
            missing = str(Path(directory) / 'missing')
            bad = Path(directory) / 'bad'
            bad.write_bytes(b'a\n\xff')
            invalid = [['--lines=' + value, missing] for value in RangeCliTests.INVALID]
            invalid += [['--lines', value, missing] for value in RangeCliTests.INVALID]
            invalid += [['--lines', missing], ['--lines', '--json', missing], ['--lines', '1:2', '--lines', '1:2', missing], ['--lines=1:2', '--lines=1:2', missing], ['--lines', '1:2', '--lines=1:2', missing]]
            for args in invalid:
                result = self.invoke(*args)
                self.assertEqual((result.returncode, result.stdout), (2, ''))
                self.assertIn('usage:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)
            for options in [[], ['--keep-bom']]:
                result = self.invoke('--lines=1:1', str(bad), *options)
                self.assertEqual((result.returncode, result.stdout), (1, ''))
                self.assertIn(str(bad), result.stderr)
                self.assertIn('utf-8', result.stderr)
                self.assertNotIn('Traceback', result.stderr)
                self.assertEqual(bad.read_bytes(), b'a\n\xff')

    def test_dash_named_files_after_option_termination(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ['-sample', '--lines', '--json', '-']:
                path = Path(directory) / name
                path.write_bytes(b'a\nb c')
                args = ['--lines', '2:2'] + ['--', './-' if name == '-' else name]
                self.assert_counts(self.invoke(*args, cwd=directory), (1, 2))
                self.assertEqual(path.read_bytes(), b'a\nb c')
