"""Independent literal-count contract and deliberate isolated regression fixture."""
import importlib.util
from pathlib import Path
from .support import Sandbox,git


class ContractProbe(Sandbox):
    def module(self):
        path=Path(__file__).parents[1]/'scripts/contract_probe.py'
        spec=importlib.util.spec_from_file_location('contract_probe',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

    def product(self):
        pkg=self.repo/'textstats';pkg.mkdir();(pkg/'__init__.py').write_text('from .core import count_text\n')
        (pkg/'core.py').write_text('from types import SimpleNamespace\ndef count_text(text, **kwargs):\n    s=text.lstrip("\\ufeff"); n=s.replace("\\r\\n","\\n").replace("\\r","\\n"); return SimpleNamespace(lines=n.count("\\n")+int(bool(n) and not n.endswith("\\n")),words=len(s.split()))\n')
        git(self.repo,'add','textstats');git(self.repo,'commit','-m','actual valid contract fixture');return git(self.repo,'rev-parse','HEAD').stdout.strip()

    def test_valid_baseline_then_actual_assertion_failure(self):
        m=self.module();head=self.product();self.assertEqual(m.probe(self.repo)['status'],'Passed')
        m.inject(self.repo,head);result=m.probe(self.repo);self.assertEqual(result['status'],'Failed');self.assertEqual(result['tests'],2);self.assertEqual(result['errors'],0);self.assertGreater(result['failures'],0)

    def test_unavailable_import_is_not_contract_failure(self):
        result=self.module().probe(self.repo);self.assertEqual(result['status'],'Unavailable');self.assertEqual(result['tests'],0)

    def test_public_package_only_implementation_passes(self):
        self.product();pkg=self.repo/'textstats'
        (pkg/'__init__.py').write_bytes((pkg/'core.py').read_bytes());(pkg/'core.py').unlink()
        result=self.module().probe(self.repo)
        self.assertEqual(result['status'],'Passed');self.assertEqual(result['tests'],2)
        self.assertEqual(result['errors'],0)
        self.assertEqual(Path(result['import_origin']),pkg/'__init__.py')

    def test_broken_public_export_fails_despite_correct_private_core(self):
        self.product()
        (self.repo/'textstats/__init__.py').write_text('from types import SimpleNamespace\ndef count_text(text, **kwargs):return SimpleNamespace(lines=99,words=99)\n')
        result=self.module().probe(self.repo)
        self.assertEqual(result['status'],'Failed');self.assertEqual(result['tests'],2)
        self.assertGreater(result['failures'],0);self.assertEqual(result['errors'],0)

    def test_wrong_identity_and_repeat_injection_rejected(self):
        m=self.module();head=self.product()
        with self.assertRaises(ValueError):m.inject(self.repo,'0'*40)
        m.inject(self.repo,head)
        with self.assertRaises(ValueError):m.inject(self.repo,head)
