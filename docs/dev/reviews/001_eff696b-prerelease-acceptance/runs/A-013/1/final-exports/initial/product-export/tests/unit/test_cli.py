"""CLI success/parser policy and actual test-runner process contracts."""

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from textstats import TextStats
from textstats.cli import main


class CliTests(unittest.TestCase):
    def test_removed_json_forms_reject_before_all_acquisition(self):
        for option in ['--json', '--json=true', '--j']:
            for args in [[option, 'named'], ['named', option],
                         ['--keep-bom', option, 'named'],
                         ['--lines=1:1', 'named', option]]:
                with self.subTest(args=args):
                    out, err = io.StringIO(), io.StringIO()
                    with patch('textstats.io.open', return_value=io.BytesIO(b'a'), create=True) as acquire, patch('textstats.cli.count_file', return_value=TextStats(1, 1)) as counter:
                        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                            status = main(args)
                    self.assertEqual((status, out.getvalue()), (2, ''))
                    self.assertIn('usage:', err.getvalue())
                    self.assertIn('error:', err.getvalue())
                    self.assertNotIn('Traceback', err.getvalue())
                    acquire.assert_not_called()
                    counter.assert_not_called()

    def test_literal_json_filename_after_termination(self):
        out, err = io.StringIO(), io.StringIO()
        with patch('textstats.cli.count_file', return_value=TextStats(1, 2)) as counter:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                status = main(['--', '--json'])
        self.assertEqual((status, out.getvalue(), err.getvalue()), (0, 'lines=1 words=2\n', ''))
        counter.assert_called_once_with('--json', strip_bom=True)

    def test_success_renders_completed_counts(self):
        out, err = io.StringIO(), io.StringIO()
        with patch('textstats.cli.count_file', return_value=TextStats(3, 4)) as counter:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                status = main(['named'])
        self.assertEqual((status, out.getvalue(), err.getvalue()), (0, 'lines=3 words=4\n', ''))
        counter.assert_called_once_with('named', strip_bom=True)

    def test_keep_bom_before_and_after_input(self):
        for args in [['--keep-bom', 'named'], ['named', '--keep-bom']]:
            with self.subTest(args=args):
                with patch('textstats.cli.count_file', return_value=TextStats(1, 1)) as counter:
                    with contextlib.redirect_stdout(io.StringIO()):
                        self.assertEqual(main(args), 0)
                counter.assert_called_once_with('named', strip_bom=False)

    def test_double_dash_retains_option_like_filename(self):
        with patch('textstats.cli.count_file', return_value=TextStats(1, 1)) as counter:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['--', '--keep-bom']), 0)
        counter.assert_called_once_with('--keep-bom', strip_bom=True)

    def test_help_never_acquires_input(self):
        for option in ['-h', '--help']:
            out, err = io.StringIO(), io.StringIO()
            with patch('textstats.cli.count_file') as counter:
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    self.assertEqual(main([option]), 0)
            counter.assert_not_called()
            self.assertIn('usage:', out.getvalue())
            self.assertIn('--keep-bom', out.getvalue())
            self.assertEqual(err.getvalue(), '')

    def test_expected_input_failures_have_status_and_diagnostic(self):
        failures = [FileNotFoundError('missing input'), PermissionError('access denied'),
                    OSError('controlled read failure'), UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'invalid start byte')]
        for failure in failures:
            with self.subTest(failure=type(failure).__name__):
                out, err = io.StringIO(), io.StringIO()
                with patch('textstats.cli.count_file', side_effect=failure):
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main(['affected.txt'])
                self.assertEqual(status, 1)
                self.assertEqual(out.getvalue(), '')
                self.assertIn('affected.txt', err.getvalue())
                self.assertIn(str(failure), err.getvalue())
                self.assertNotIn('Traceback', err.getvalue())

    def test_usage_validates_before_acquisition(self):
        for args in [[], ['missing', 'extra'], ['--unknown', 'missing'], ['--keep', 'missing']]:
            with self.subTest(args=args):
                out, err = io.StringIO(), io.StringIO()
                with patch('textstats.cli.count_file') as counter:
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main(args)
                counter.assert_not_called()
                self.assertEqual((status, out.getvalue()), (2, ''))
                self.assertIn('usage:', err.getvalue())
                self.assertIn('error:', err.getvalue())
                self.assertNotIn('Traceback', err.getvalue())


class CheckRunnerTests(unittest.TestCase):
    def invoke_fixture(self, unit_source, integration_source):
        source = Path(__file__).resolve().parents[2] / 'tools' / 'check_tests.py'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'tools').mkdir()
            shutil.copyfile(source, root / 'tools' / 'check_tests.py')
            for suite, contents in [('unit', unit_source), ('integration', integration_source)]:
                target = root / 'tests' / suite
                target.mkdir(parents=True)
                (root / 'tests' / '__init__.py').touch()
                (target / '__init__.py').touch()
                if contents is not None:
                    (target / 'test_contract.py').write_text(contents)
            # Deliberately failing workflow fixture must never be collected.
            fixture = root / 'tests' / 'workflows'
            fixture.mkdir()
            (fixture / '__init__.py').touch()
            (fixture / 'test_foreign.py').write_text('raise RuntimeError("workflow fixture collected")\n')
            return subprocess.run([sys.executable, str(root / 'tools' / 'check_tests.py')], cwd=root, capture_output=True, text=True)

    GOOD = 'import unittest\nclass Contract(unittest.TestCase):\n    def test_contract(self):\n        self.assertEqual(2 + 2, 4)\n'
    BAD = 'import unittest\nclass Contract(unittest.TestCase):\n    def test_contract(self):\n        self.fail("controlled product failure")\n'

    def test_nonempty_success_reports_independent_counts(self):
        result = self.invoke_fixture(self.GOOD, self.GOOD)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('unit: 1 tests', result.stdout)
        self.assertIn('integration: 1 tests', result.stdout)

    def test_either_empty_suite_is_rejected(self):
        for unit, integration, empty in [(None, self.GOOD, 'unit'), (self.GOOD, None, 'integration')]:
            with self.subTest(empty=empty):
                result = self.invoke_fixture(unit, integration)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(empty + ': 0 tests', result.stdout)
                self.assertIn('empty product suite', result.stderr)

    def test_product_failure_is_propagated(self):
        result = self.invoke_fixture(self.BAD, self.GOOD)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('controlled product failure', result.stderr)


class RangeCliTests(unittest.TestCase):
    INVALID = ['0:1', '1:0', '3:2', '-1:2', '+1:2', '1:-2', '1:+2',
               ' 1:2', '1:2 ', '1 :2', '1:\t2', '١:٢', '１:２', ':2', '1:', ':', '1:2:3', '1', '']

    def invoke(self, args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = main(args)
        return status, out.getvalue(), err.getvalue()

    def test_full_invalid_matrix_precedes_file_acquisition(self):
        invalid = [[ '--lines', value, 'missing'] for value in self.INVALID]
        invalid += [['--lines='+value, 'missing'] for value in self.INVALID]
        invalid += [['missing', '--lines'], ['missing', '--lines='],
                    ['--lines', '--json', 'missing'],
                    ['--lines', '1:2', '--lines', '1:2', 'missing'],
                    ['--lines=1:2', '--lines=1:2', 'missing'],
                    ['--lines', '1:2', '--lines=1:2', 'missing']]
        for args in invalid:
            with self.subTest(args=args), patch('textstats.io.open', create=True) as acquire:
                status, out, err = self.invoke(args)
                self.assertEqual((status, out), (2, ''))
                self.assertIn('usage:', err)
                self.assertNotIn('Traceback', err)
                acquire.assert_not_called()

    def test_real_acquisition_normalizes_once_and_closes(self):
        for options in [[], ['--keep-bom']]:
            stream = io.BytesIO('\ufeffa\n\ufeff'.encode())
            with patch('textstats.io.open', return_value=stream, create=True) as acquire:
                status, out, err = self.invoke(['--lines=2:2', 'named', *options])
            self.assertEqual((status, err), (0, ''))
            self.assertEqual(out, 'lines=1 words=1\n')
            acquire.assert_called_once_with('named', 'rb')
            self.assertTrue(stream.closed)

    def test_full_decode_after_end_and_read_failure_close(self):
        class BrokenReader(io.BytesIO):
            def read(self, *args):
                raise OSError('controlled complete read failure')
        for stream, cause in [(io.BytesIO(b'a\n\xff'), 'utf-8'), (BrokenReader(), 'controlled complete read failure')]:
            with patch('textstats.io.open', return_value=stream, create=True):
                status, out, err = self.invoke(['--lines', '1:1', 'named'])
            self.assertEqual((status, out), (1, ''))
            self.assertIn('named', err)
            self.assertIn(cause, err)
            self.assertNotIn('Traceback', err)
            self.assertTrue(stream.closed)

    def test_valid_huge_and_leading_zero_decimals_do_not_use_conversion_guard(self):
        huge = '9' * 5001
        for value, expected in [('1:'+huge, (2, 2)), (huge+':'+huge, (0,0)),
                                ('0'*5001+'1:'+'0'*5001+'1', (1,1))]:
            with patch('textstats.io.open', return_value=io.BytesIO(b'a\nb'), create=True):
                status, out, err = self.invoke(['named', '--lines='+value])
            self.assertEqual((status,out,err),(0,f'lines={expected[0]} words={expected[1]}\n',''))
