"""Preflight and fresh-preparation contract tests using isolated Git fixtures.

Checks source pinning, protected configuration, repository identity and bounded
setup without authenticating, publishing hosted work or changing source inputs."""
import json
from pathlib import Path
import sys
try:
    from .support import Sandbox, git, SOURCE
except ImportError:
    from support import Sandbox, git, SOURCE

class PreflightTests(Sandbox):
    def test_missing_repository_requests_input_without_any_output_write(self):
        p, data, out = self.invoke('preflight', {'schema_version': 1})
        self.assertNotEqual(p.returncode, 0)
        self.assertFalse(out.exists())
        self.assertEqual(json.loads(p.stdout)['next_action'], 'Which dedicated test repository should this run use? Supply its URL or local checkout path.')

    def test_blank_repository_requests_same_input(self):
        p, data, out = self.invoke('prepare', {'schema_version': 1, 'test_repository': ''})
        self.assertFalse(out.exists())
        self.assertIn('Which dedicated test repository', p.stdout)

    def test_ambiguous_remotes_require_resolution(self):
        git(self.repo, 'remote', 'add', 'backup', str(self.remote))
        p, data, out = self.invoke('preflight')
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual(json.loads(p.stdout)['cause'], 'repository_ambiguous')
        self.assertFalse(out.exists())

    def test_repository_identity_mismatch_fails(self):
        values = dict(self.inputs, test_repository=str(self.root / 'other.git'))
        p, _, _ = self.invoke('preflight', values)
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual(json.loads(p.stdout)['cause'], 'repository_identity_mismatch')

    def test_unknown_and_secret_configuration_fails_without_echo(self):
        for values in [dict(self.inputs, token='SECRET_SENTINEL'), dict(self.inputs, scope={'typo': 'SECRET_SENTINEL'}), dict(self.inputs, test_repository='https://user:SECRET_SENTINEL@example.invalid/repo.git'), dict(self.inputs, plugin_revision='github_pat_SECRET_SENTINEL')]:
            p, _, out = self.invoke('preflight', values)
            self.assertNotEqual(p.returncode, 0)
            self.assertNotIn('SECRET_SENTINEL', p.stdout + p.stderr)
            self.assertFalse(out.exists())

    def test_strict_schema_constraints_and_no_type_coercion(self):
        for updates in [{'schema_version': True}, {'scope': {'cases': ['A-001','A-001']}}, {'scope': {'cases':['A-999']}}, {'stop_after':'P9'}, {'run_id':'../escape'}, {'profile':'full'}]:
            p, _, _ = self.invoke('preflight', dict(self.inputs, **updates))
            self.assertNotEqual(p.returncode, 0)

    def test_pin_uses_git_object_bytes_and_complete_package_manifest(self):
        data, _ = self.ok(self.invoke('preflight'))
        self.assertEqual(data['plugin_source']['commit'], git(SOURCE, 'rev-parse', 'HEAD').stdout.strip())
        expected=set(git(SOURCE,'ls-tree','-r','--name-only','HEAD','plugin.json','.codex-plugin','README.md','AGENTS.md','Greenfield Project Prompt Template.md','LICENSE','SDD-MANAGER.md','AI_DISCLOSURE.md','skills','assets').stdout.splitlines())
        self.assertEqual(set(data['plugin_source']['package_hashes']), expected)
        self.assertEqual(data['plugin_source']['source_mode'], 'committed')
        self.assertEqual(data['repository']['remote'], 'origin')
        self.assertFalse(data['capabilities']['github_api'])

    def test_preflight_has_no_worktree_or_index_side_effects(self):
        (self.repo / 'owned.txt').write_text('staged\n')
        git(self.repo, 'add', 'owned.txt')
        (self.repo / 'owned.txt').write_text('unstaged\n')
        before = git(self.repo, 'ls-files', '--stage').stdout
        self.ok(self.invoke('preflight'))
        self.assertEqual(git(self.repo, 'ls-files', '--stage').stdout, before)
        self.assertEqual((self.repo / 'owned.txt').read_text(), 'unstaged\n')

    def test_prepare_requires_new_explicit_workspace_and_preserves_existing_run(self):
        campaign = self.repo / 'docs/dev/reviews/001_fixture'
        campaign.mkdir(parents=True)
        (campaign / 'RUN-STATE.json').write_text('retained')
        p, _, _ = self.invoke('prepare')
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual((campaign / 'RUN-STATE.json').read_text(), 'retained')
        target = self.root / 'occupied'
        target.mkdir()
        (target / 'foreign').write_text('retain')
        p, _, _ = self.invoke('prepare', extra=['--workspace',target])
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual((target / 'foreign').read_text(), 'retain')

    def test_prepare_resume_does_not_clone(self):
        target = self.root / 'fresh'
        p, _, _ = self.invoke('prepare', dict(self.inputs, run_id='001_fixture'), extra=['--workspace',target])
        self.assertNotEqual(p.returncode, 0)
        self.assertFalse(target.exists())

    def test_prepare_isolated_clone_contains_only_vendor_and_provenance(self):
        (self.repo / 'AGENTS.md').write_text('original operating instructions\n')
        git(self.repo, 'add', 'AGENTS.md')
        git(self.repo, 'commit', '-m', 'instructions')
        target = self.root / 'fresh'
        data, _ = self.ok(self.invoke('prepare', extra=['--workspace',target]))
        self.assertEqual((target / 'AGENTS.md').read_text(), 'original operating instructions\n')
        self.assertFalse((target / 'textstats').exists())
        snapshot = Path(data['plugin_source']['snapshot_path'])
        self.assertEqual({str(p.relative_to(snapshot)) for p in snapshot.rglob('*') if p.is_file()}, set(data['plugin_source']['package_hashes']))
        self.assertFalse((snapshot / 'tests').exists())
        self.assertEqual(git(self.repo,'status','--porcelain').stdout, '')

    def test_prepare_new_unborn_remote_is_bounded_and_does_not_publish(self):
        empty = self.root / 'empty.git'
        git(self.root, 'init', '--bare', str(empty))
        target = self.root / 'unborn'
        data, _ = self.ok(self.invoke('prepare', {'schema_version':1,'test_repository':str(empty),'profile':'local-only'}, extra=['--workspace',target]))
        self.assertTrue((target / 'AGENTS.md').exists())
        self.assertTrue((target / '.gitignore').exists())
        self.assertEqual(git(empty,'for-each-ref').stdout, '')
        self.assertEqual(git(target,'rev-parse','--verify','HEAD',check=False).returncode, 128)

    def test_dirty_source_fingerprint_and_committed_default(self):
        source=self.root/'source'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture')
        git(source,'config','user.email','fixture@example.invalid')
        (source/'skills/demo').mkdir(parents=True)
        (source/'skills/demo/SKILL.md').write_text('committed\n')
        (source/'plugin.json').write_text('{"name":"fixture"}\n')
        git(source,'add','.')
        git(source,'commit','-m','package')
        import hashlib
        (source/'skills/demo/SKILL.md').write_text('dirty\n')
        (source/'skills/demo/new.md').write_text('new dirty\n')
        committed,_=self.ok(self.invoke('preflight',extra=['--source-root',source]))
        self.assertEqual(committed['plugin_source']['package_hashes']['skills/demo/SKILL.md'],hashlib.sha256(b'committed\n').hexdigest())
        dirty,_=self.ok(self.invoke('preflight',dict(self.inputs,source_mode='dirty'),extra=['--source-root',source]))
        self.assertEqual(dirty['plugin_source']['package_hashes']['skills/demo/SKILL.md'],hashlib.sha256(b'dirty\n').hexdigest())
        self.assertIn('skills/demo/new.md',dirty['plugin_source']['changed_package_paths'])
        self.assertNotEqual(dirty['plugin_source']['fingerprint'],committed['plugin_source']['fingerprint'])

    def test_package_preserves_manifest_orientation_and_binary_assets_in_dirty_snapshot(self):
        import hashlib
        source=self.root/'package-source'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture')
        git(source,'config','user.email','fixture@example.invalid')
        (source/'plugin.json').write_text('{"name":"fixture","skills":"./skills/"}\n')
        (source/'.codex-plugin').mkdir()
        (source/'.codex-plugin/plugin.json').write_bytes((source/'plugin.json').read_bytes())
        (source/'AGENTS.md').write_text('Use package instructions.\n')
        (source/'assets').mkdir()
        asset=source/'assets/logo.png'
        original=b'\x89PNG\r\n\x1a\nfixture\x00'
        asset.write_bytes(original)
        git(source,'add','.')
        git(source,'commit','-m','package')
        committed,_=self.ok(self.invoke('preflight',extra=['--source-root',source]))
        self.assertIn('plugin.json',committed['plugin_source']['package_hashes'])
        self.assertEqual(committed['plugin_source']['package_hashes'].get('.codex-plugin/plugin.json'),committed['plugin_source']['package_hashes']['plugin.json'])
        self.assertEqual(committed['plugin_source']['package_hashes']['AGENTS.md'],hashlib.sha256(b'Use package instructions.\n').hexdigest())
        self.assertEqual(committed['plugin_source']['package_hashes']['assets/logo.png'],hashlib.sha256(original).hexdigest())
        changed=original+b'dirty'
        asset.write_bytes(changed)
        (source/'AGENTS.md').write_text('Use changed package instructions.\n')
        (source/'.codex-plugin/new.svg').write_text('<svg/>')
        target=self.root/'codex-snapshot'
        dirty,_=self.ok(self.invoke('prepare',dict(self.inputs,source_mode='dirty'),extra=['--source-root',source,'--workspace',target]))
        snapshot=Path(dirty['plugin_source']['snapshot_path'])
        self.assertEqual((snapshot/'assets/logo.png').read_bytes(),changed)
        self.assertTrue((snapshot/'plugin.json').is_file())
        self.assertEqual((snapshot/'.codex-plugin/plugin.json').read_bytes(),(snapshot/'plugin.json').read_bytes())
        self.assertIn('.codex-plugin/new.svg',dirty['plugin_source']['changed_package_paths'])
        self.assertEqual((snapshot/'AGENTS.md').read_text(),'Use changed package instructions.\n')
        self.assertIn('AGENTS.md',dirty['plugin_source']['changed_package_paths'])
        self.assertIn('assets/logo.png',dirty['plugin_source']['changed_package_paths'])
        diff=Path(dirty['plugin_source']['dirty_diff_path']).read_bytes()
        self.assertIn(b'assets/logo.png',diff)

    def test_dirty_source_tracks_executable_mode_changes(self):
        source=self.root/'mode-source'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture')
        git(source,'config','user.email','fixture@example.invalid')
        (source/'skills/demo').mkdir(parents=True)
        path=source/'skills/demo/run.sh'
        path.write_text('echo fixture\n')
        (source/'plugin.json').write_text('{}\n')
        git(source,'add','.')
        git(source,'commit','-m','package')
        base,_=self.ok(self.invoke('preflight',extra=['--source-root',source]))
        path.chmod(0o755)
        dirty,_=self.ok(self.invoke('preflight',dict(self.inputs,source_mode='dirty'),extra=['--source-root',source]))
        self.assertNotEqual(base['plugin_source']['fingerprint'],dirty['plugin_source']['fingerprint'])
        self.assertIn('skills/demo/run.sh',dirty['plugin_source']['changed_package_paths'])

    def test_prepare_refuses_dangling_workspace_symlink_before_resolving(self):
        lexical=self.root/'requested-workspace'
        destination=self.root/'foreign-destination'
        lexical.symlink_to(destination,target_is_directory=True)
        p,data,out=self.invoke('prepare',extra=['--workspace',lexical])
        self.assertNotEqual(p.returncode,0)
        self.assertFalse(destination.exists())
        self.assertTrue(lexical.is_symlink())
        self.assertFalse(out.exists())

    def test_dirty_package_parent_symlink_is_not_followed(self):
        source=self.root/'boundary-source'
        git(self.root,'init','-b','main',str(source))
        git(source,'config','user.name','Fixture')
        git(source,'config','user.email','fixture@example.invalid')
        (source/'skills/demo').mkdir(parents=True)
        (source/'skills/demo/SKILL.md').write_text('committed\n')
        (source/'plugin.json').write_text('{}\n')
        (source/'.gitignore').write_text('/skills/demo\n')
        git(source,'add','plugin.json','.gitignore')
        git(source,'add','-f','skills/demo/SKILL.md')
        git(source,'commit','-m','package')
        (source/'skills/demo/SKILL.md').unlink()
        (source/'skills/demo').rmdir()
        foreign=self.root/'foreign-package'
        foreign.mkdir()
        (foreign/'SKILL.md').write_text('EXTERNAL_SENTINEL')
        (source/'skills/demo').symlink_to(foreign,target_is_directory=True)
        p,data,out=self.invoke('preflight',dict(self.inputs,source_mode='dirty'),extra=['--source-root',source])
        self.assertNotEqual(p.returncode,0)
        self.assertFalse(out.exists())
        self.assertNotIn('EXTERNAL_SENTINEL',p.stdout+p.stderr)

    def test_username_only_ssh_transport_is_allowed_but_embedded_credentials_rejected(self):
        url='ssh://git@example.invalid/owner/repository.git'
        git(self.repo,'remote','set-url','origin',url)
        data,_=self.ok(self.invoke('preflight',dict(self.inputs,test_repository=url)))
        self.assertEqual(data['repository']['remote_url'],url)
        for value in ['ssh://git:SECRET_SENTINEL@example.invalid/owner/repo.git','ssh://git@example.invalid/owner/repo.git?token=SECRET_SENTINEL','https://user@example.invalid/owner/repo.git','https://example.invalid/owner/repo.git?access_token=SECRET_SENTINEL']:
            p,data,out=self.invoke('preflight',dict(self.inputs,test_repository=value))
            self.assertNotEqual(p.returncode,0)
            self.assertNotIn('SECRET_SENTINEL',p.stdout+p.stderr)
            self.assertFalse(out.exists())
