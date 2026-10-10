"""Actual package pinning retains user documentation and its dirty identity."""
import hashlib
from pathlib import Path, PurePosixPath
from .support import Sandbox, git


class PackageDocumentation(Sandbox):
    def test_legacy_manifest_matches_canonical_manifest(self):
        source = Path(__file__).resolve().parents[3]
        legacy = source / '.codex-plugin/plugin.json'
        self.assertTrue(legacy.is_file(), 'Legacy discovery manifest is missing')
        self.assertEqual(legacy.read_bytes(), (source / 'plugin.json').read_bytes())

    def test_notice_navigation_is_retained_in_committed_and_dirty_snapshots(self):
        source=self.root/'notice-package'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture');git(source,'config','user.email','fixture@example.invalid')
        (source/'plugin.json').write_text('{"name":"fixture"}\n')
        readme=b'Development uses [SDD Manager](SDD-MANAGER.md). See [disclosure](AI_DISCLOSURE.md).\n'
        notice=b'# Usage\n\nSee [disclosure](AI_DISCLOSURE.md).\n'
        disclosure=b'# Disclosure\n\nMaintainer owns the published work.\n'
        (source/'README.md').write_bytes(readme)
        (source/'SDD-MANAGER.md').write_bytes(notice)
        (source/'AI_DISCLOSURE.md').write_bytes(disclosure)
        git(source,'add','.');git(source,'commit','-m','notice links')
        import sys
        from pathlib import Path
        sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
        import core
        inputs={'plugin_revision':git(source,'rev-parse','HEAD').stdout.strip(),'source_mode':'committed'}
        committed,files=core.package(source,inputs)
        import re
        for owner in ['README.md','SDD-MANAGER.md']:
            self.assertIn(owner,files)
            for target in re.findall(r'\]\(([^)]+)\)',files[owner].decode()):
                self.assertIn(str(PurePosixPath(owner).parent/target),files)
        self.assertEqual(files.get('AI_DISCLOSURE.md'),disclosure)
        (source/'AI_DISCLOSURE.md').write_bytes(disclosure+b'Updated notice.\n')
        dirty,files=core.package(source,dict(inputs,source_mode='dirty'))
        self.assertIn('AI_DISCLOSURE.md',dirty['changed_package_paths'])
        self.assertEqual(files['AI_DISCLOSURE.md'],disclosure+b'Updated notice.\n')
        self.assertNotEqual(dirty['fingerprint'],committed['fingerprint'])

    def test_committed_and_dirty_readme_and_license_are_packaged(self):
        source=self.root/'package-source'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture');git(source,'config','user.email','fixture@example.invalid')
        manifest=b'{"name":"fixture","version":"1.0.0"}\n'
        (source/'plugin.json').write_bytes(manifest)
        (source/'README.md').write_bytes(b'Human package documentation\n')
        (source/'AGENTS.md').write_bytes(b'Agent package orientation\n')
        (source/'Greenfield Project Prompt Template.md').write_bytes(b'Project seed prompt\n')
        (source/'LICENSE').write_bytes(b'Fixture license\n')
        git(source,'add','.');git(source,'commit','-m','package documentation')
        committed,_=self.ok(self.invoke('preflight',extra=['--source-root',source]))
        hashes=committed['plugin_source']['package_hashes']
        self.assertEqual(hashes.get('README.md'),hashlib.sha256(b'Human package documentation\n').hexdigest())
        self.assertEqual(hashes.get('AGENTS.md'),hashlib.sha256(b'Agent package orientation\n').hexdigest())
        self.assertEqual(hashes.get('Greenfield Project Prompt Template.md'),hashlib.sha256(b'Project seed prompt\n').hexdigest())
        self.assertEqual(hashes.get('LICENSE'),hashlib.sha256(b'Fixture license\n').hexdigest())
        (source/'README.md').write_bytes(b'Updated package documentation\n')
        (source/'AGENTS.md').write_bytes(b'Updated agent package orientation\n')
        (source/'Greenfield Project Prompt Template.md').write_bytes(b'Updated project seed prompt\n')
        dirty,_=self.ok(self.invoke('preflight',dict(self.inputs,source_mode='dirty'),extra=['--source-root',source]))
        self.assertEqual(dirty['plugin_source']['package_hashes']['README.md'],hashlib.sha256(b'Updated package documentation\n').hexdigest())
        self.assertEqual(dirty['plugin_source']['package_hashes']['AGENTS.md'],hashlib.sha256(b'Updated agent package orientation\n').hexdigest())
        self.assertEqual(dirty['plugin_source']['package_hashes']['Greenfield Project Prompt Template.md'],hashlib.sha256(b'Updated project seed prompt\n').hexdigest())
        self.assertIn('README.md',dirty['plugin_source']['changed_package_paths'])
        self.assertIn('AGENTS.md',dirty['plugin_source']['changed_package_paths'])
        self.assertIn('Greenfield Project Prompt Template.md',dirty['plugin_source']['changed_package_paths'])
        self.assertNotEqual(dirty['plugin_source']['fingerprint'],committed['plugin_source']['fingerprint'])
