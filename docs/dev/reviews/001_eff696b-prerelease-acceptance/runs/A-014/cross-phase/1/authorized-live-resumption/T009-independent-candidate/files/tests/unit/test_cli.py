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
            return subprocess.run([sys.executable, "-B", str(root / 'tools' / 'check_tests.py')], cwd=root, capture_output=True, text=True)

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
