"""Exercise evidence-only integration against actual disposable Git objects."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import evidence_merge


class EvidenceMergeTests(unittest.TestCase):
    def test_actual_merge_preserves_product_and_rejects_wrong_parents(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.check_output(['git', '-C', folder, *args], stderr=subprocess.DEVNULL).decode().strip()
            git('init', '-b', 'main'); git('config', 'user.name', 'Test'); git('config', 'user.email', 'test@example.invalid')
            (root / 'product.py').write_text('original\n')
            git('add', 'product.py'); git('commit', '-m', 'product'); product = git('rev-parse', 'HEAD')
            git('checkout', '-b', 'evidence')
            campaign = 'docs/dev/reviews/test'
            path = root / campaign; path.mkdir(parents=True)
            (path / 'DIAGNOSTIC-REPORT.md').write_text('actual report\n')
            git('add', campaign); git('commit', '-m', 'evidence'); evidence = git('rev-parse', 'HEAD')
            git('checkout', 'main'); git('merge', '--no-ff', 'evidence', '-m', 'integrate')
            merge = git('rev-parse', 'HEAD')
            record = evidence_merge.verify(root, merge, product, evidence, campaign)
            self.assertTrue(record['product_preserved'])
            self.assertFalse(record['publication_verified'])
            with self.assertRaisesRegex(ValueError, 'parents'):
                evidence_merge.verify(root, merge, evidence, product, campaign)
            with self.assertRaisesRegex(ValueError, 'parents'):
                evidence_merge.verify(root, evidence, product, evidence, campaign)
            git('checkout', 'evidence')
            (root / 'product.py').write_text('unauthorized fixture change\n')
            git('add', 'product.py'); git('commit', '-m', 'product changed'); bad = git('rev-parse', 'HEAD')
            git('checkout', 'main'); prior = git('rev-parse', 'HEAD'); git('merge', '--no-ff', 'evidence', '-m', 'bad integrate')
            with self.assertRaisesRegex(ValueError, 'product or foreign'):
                evidence_merge.verify(root, git('rev-parse', 'HEAD'), prior, bad, campaign)


if __name__ == '__main__': unittest.main()
