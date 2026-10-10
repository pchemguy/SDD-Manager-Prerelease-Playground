"""Source allowlist and real isolated extracted-module acceptance contracts."""

import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.package_source import build_archive
from tools.check_distribution import verify_archive

ROOT = Path(__file__).resolve().parents[2]
APPROVED = {'README.md', 'docs/public-api.md', 'AI_DISCLOSURE.md', 'SDD-MANAGER.md',
            'textstats/__init__.py', 'textstats/__main__.py', 'textstats/core.py',
            'textstats/io.py', 'textstats/cli.py', 'tools/package_source.py',
            'tools/check_distribution.py'}


class DistributionTests(unittest.TestCase):
    def test_checker_rejects_json_wrong_types_while_text_still_works(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build_archive(ROOT, Path(directory) / 'source.zip')
            faulty = Path(directory) / 'faulty-json.zip'
            with zipfile.ZipFile(archive) as source, zipfile.ZipFile(faulty, 'w') as target:
                for name in source.namelist():
                    data = source.read(name)
                    if name == 'textstats-source/textstats/cli.py':
                        original = b"{'lines': stats.lines, 'words': stats.words}"
                        self.assertIn(original, data)
                        data = data.replace(original, b"{'lines': str(stats.lines), 'words': str(stats.words)}")
                    target.writestr(name, data)
            with self.assertRaises((AssertionError, RuntimeError)):
                verify_archive(faulty)

    def test_checker_rejects_ignored_range_with_healthy_whole_input(self):
        self._assert_range_mutation_rejected(
            b'if args.lines is None:', b'if True:')

    def test_checker_rejects_second_bom_normalization_after_selection(self):
        self._assert_range_mutation_rejected(
            b'_count_normalized(_select_lines(normalized, *args.lines))',
            b'__import__("textstats").count_text(_select_lines(normalized, *args.lines))')

    def _assert_range_mutation_rejected(self, original, replacement):
        """Alter only extracted range behavior; checkout and whole-input stay healthy."""
        with tempfile.TemporaryDirectory() as directory:
            archive = build_archive(ROOT, Path(directory) / 'source.zip')
            faulty = Path(directory) / 'faulty-range.zip'
            with zipfile.ZipFile(archive) as source, zipfile.ZipFile(faulty, 'w') as target:
                for name in source.namelist():
                    data = source.read(name)
                    if name == 'textstats-source/textstats/cli.py':
                        self.assertIn(original, data)
                        data = data.replace(original, replacement)
                    target.writestr(name, data)
            with self.assertRaises((AssertionError, RuntimeError)):
                verify_archive(faulty)

    def test_archive_exact_allowlist_excludes_unrelated_material(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'source'
            for name in APPROVED:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / name).read_bytes())
            for name in ['gh.tkn', 'textstats/__pycache__/cache.pyc', 'textstats/extra.py',
                         'textstats-run-resources/fake.txt', '.github/workflows/foreign.yml',
                         'tests/workflows/fake.py', 'docs/dev/fake.md', 'dist/old.zip']:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('unmanaged fixture, never a real credential')
            archive = build_archive(root, Path(directory) / 'source.zip')
            with zipfile.ZipFile(archive) as bundle:
                self.assertEqual(set(bundle.namelist()), {'textstats-source/' + n for n in APPROVED})
                for name in APPROVED:
                    self.assertEqual(bundle.read('textstats-source/' + name), (ROOT / name).read_bytes())

    def test_checker_verifies_real_extracted_module_with_polluted_import_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build_archive(ROOT, Path(directory) / 'source.zip')
            from unittest.mock import patch
            with patch.dict(os.environ, {'PYTHONPATH': str(ROOT)}):
                self.assertGreaterEqual(verify_archive(archive), 10)

    def test_checker_rejects_wrong_extracted_cli_even_when_checkout_is_healthy(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build_archive(ROOT, Path(directory) / 'source.zip')
            faulty = Path(directory) / 'faulty.zip'
            with zipfile.ZipFile(archive) as source, zipfile.ZipFile(faulty, 'w') as target:
                for name in source.namelist():
                    data = source.read(name)
                    if name == 'textstats-source/textstats/cli.py':
                        data = b'"""Controlled faulty extraction."""\ndef main(argv=None):\n    print("lines=999 words=999")\n    return 0\n'
                    target.writestr(name, data)
            with self.assertRaises((AssertionError, RuntimeError)):
                verify_archive(faulty)

    def test_documented_checker_script_builds_and_runs(self):
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'tools/check_distribution.py')], cwd=ROOT,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('extracted import:', result.stdout)
        self.assertIn('module cases passed', result.stdout)
