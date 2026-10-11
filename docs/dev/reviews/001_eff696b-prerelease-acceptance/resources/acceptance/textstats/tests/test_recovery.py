"""Actual-state observation and recovery reconstruction tests in disposable repos.

Checks retained files/index stages/commit roots and uncertainty at local remotes.
These controlled restores test helper exports, not fresh-agent recovery behavior."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
try:
    from .support import Sandbox, SCRIPTS, git
except ImportError:
    from support import Sandbox, SCRIPTS, git

class RecoveryTests(Sandbox):
    def _consumer_snapshot(self):
        return (git(self.repo,'rev-parse','HEAD').stdout,
                git(self.repo,'for-each-ref').stdout,
                git(self.repo,'status','--porcelain').stdout,
                (self.repo/'.git/index').read_bytes(),
                (self.repo/'owned.txt').read_bytes(),
                (self.repo/'owned.txt').stat().st_mode,
                sorted(str(p.relative_to(self.repo)) for p in self.repo.rglob('*') if '.git' not in p.relative_to(self.repo).parts))

    def _observe_from_caller(self, output):
        (self.root/'inputs.json').write_text(json.dumps(self.inputs))
        (self.root/'state.json').write_text(json.dumps(self.state))
        return subprocess.run([sys.executable,str(SCRIPTS/'observe.py'),
                               '--inputs','inputs.json','--run-state','state.json',
                               '--output',str(output)],cwd=self.root,capture_output=True,text=True)

    def _assert_caller_export(self, output):
        before=self._consumer_snapshot()
        proc=self._observe_from_caller(output)
        self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
        out=self.root/output
        data=json.loads(out.read_text())
        export=Path(data['recovery']['path'])
        self.assertTrue(export.is_absolute())
        self.assertEqual(export,Path(str(out)+'.recovery'))
        manifest_path=export/'manifest.json'
        self.assertEqual(hashlib.sha256(manifest_path.read_bytes()).hexdigest(),data['recovery']['manifest_sha256'])
        manifest=json.loads(manifest_path.read_text())
        self.assertTrue(manifest['complete'])
        self.assertEqual(manifest['bundle'],'objects.bundle')
        self.assertIn('objects.bundle',manifest['artifact_hashes'])
        for name,expected in manifest['artifact_hashes'].items():
            self.assertEqual(hashlib.sha256((export/name).read_bytes()).hexdigest(),expected,name)
        self.assertEqual(self._consumer_snapshot(),before)
        restored=out.parent/(out.name+'.restored')
        git(self.root,'clone',str(self.remote),str(restored))
        git(restored,'bundle','verify',str(export/'objects.bundle'))
        git(restored,'fetch',str(export/'objects.bundle'),'refs/heads/main')
        self.assertEqual(git(restored,'rev-parse','FETCH_HEAD').stdout.strip(),manifest['head'])

    def test_caller_relative_cli_exports_verified_bundle_outside_consumer(self):
        for output in (Path('relative-observation.json'),Path('new-attempt/nested/observation.json')):
            with self.subTest(output=str(output)):
                self._assert_caller_export(output)

    def test_absolute_cli_output_creates_missing_parent(self):
        self._assert_caller_export(self.root/'absolute-attempt/nested/observation.json')

    def test_cli_refuses_occupied_and_dangling_output_and_recovery_paths(self):
        for suffix,cause in (('', 'output_occupied'),('.recovery','recovery_export_occupied')):
            for kind in ('file','directory','symlink','dangling-symlink'):
                with self.subTest(suffix=suffix,kind=kind):
                    output=Path('refuse-'+kind+('-recovery' if suffix else '')+'.json')
                    occupied=self.root/(str(output)+suffix)
                    target=self.root/(str(output)+'.target')
                    if kind=='file': occupied.write_text('retained evidence\n')
                    elif kind=='directory':
                        occupied.mkdir()
                        (occupied/'retained').write_text('retained evidence\n')
                    else:
                        if kind=='symlink': target.mkdir()
                        occupied.symlink_to(target,target_is_directory=True)
                    before=self._consumer_snapshot()
                    proc=self._observe_from_caller(output)
                    self.assertEqual(proc.returncode,2,proc.stdout+proc.stderr)
                    self.assertEqual(json.loads(proc.stdout)['cause'],cause)
                    self.assertEqual(self._consumer_snapshot(),before)
                    if kind=='file': self.assertEqual(occupied.read_text(),'retained evidence\n')
                    elif kind=='directory': self.assertEqual((occupied/'retained').read_text(),'retained evidence\n')
                    else:
                        self.assertTrue(occupied.is_symlink())
                        self.assertEqual(occupied.readlink(),target)
                        if kind=='symlink': self.assertEqual(list(target.iterdir()),[])
                        else: self.assertFalse(target.exists())
                    if suffix: self.assertFalse((self.root/output).exists())
                    else: self.assertFalse(Path(str(self.root/output)+'.recovery').exists())

    def test_actual_staged_and_unstaged_intent_export_and_restore(self):
        (self.repo / 'owned.txt').write_text('staged\n')
        git(self.repo,'add','owned.txt')
        (self.repo / 'owned.txt').write_text('unstaged\n')
        (self.repo / 'new.bin').write_bytes(b'\x00pending\xff')
        (self.repo / 'link').symlink_to('owned.txt')
        data, _ = self.ok(self.invoke('observe', state=self.state))
        self.assertEqual(data['git']['staged_paths'], ['owned.txt'])
        self.assertEqual(data['git']['unstaged_paths'], ['owned.txt'])
        export = Path(data['recovery']['path'])
        manifest = json.loads((export/'manifest.json').read_text())
        restored = self.root/'restored'
        git(self.root,'clone',str(self.remote),str(restored))
        git(restored,'checkout','main')
        git(restored,'bundle','verify',str(export/'objects.bundle'))
        git(restored,'fetch',str(export/'objects.bundle'),'refs/heads/main')
        for entry in manifest['index']:
            blob = (export/'blobs'/entry['oid']).read_bytes()
            subprocess.run(['git','-C',str(restored),'hash-object','-w','--stdin'],input=blob,check=True,capture_output=True)
        raw = ''.join(f"{e['mode']} {e['oid']} {e['stage']}\t{e['path']}\n" for e in manifest['index'])
        git(restored,'read-tree','--empty')
        subprocess.run(['git','-C',str(restored),'update-index','--index-info'],input=raw,text=True,check=True,capture_output=True)
        for entry in manifest['workfiles']:
            path = restored/entry['path']
            path.parent.mkdir(parents=True,exist_ok=True)
            if path.exists() or path.is_symlink(): path.unlink()
            if entry['kind']=='symlink': path.symlink_to(entry['target'])
            else:
                content=(export/'files'/entry['sha256']).read_bytes()
                self.assertEqual(hashlib.sha256(content).hexdigest(),entry['sha256'])
                path.write_bytes(content)
                path.chmod(entry['mode'])
        self.assertEqual(git(restored,'ls-files','--stage').stdout,git(self.repo,'ls-files','--stage').stdout)
        self.assertEqual((restored/'owned.txt').read_text(),'unstaged\n')
        self.assertEqual((restored/'new.bin').read_bytes(),b'\x00pending\xff')
        self.assertEqual((restored/'link').readlink(),Path('owned.txt'))
        self.assertEqual(data['recovery']['publication'],'local-only')

    def test_deletion_and_conflict_stages_merge_parents_preserved(self):
        git(self.repo,'checkout','-b','other')
        (self.repo/'owned.txt').write_text('other\n')
        git(self.repo,'commit','-am','other')
        other=git(self.repo,'rev-parse','HEAD').stdout.strip()
        git(self.repo,'checkout','main')
        (self.repo/'owned.txt').write_text('main\n')
        git(self.repo,'commit','-am','main')
        git(self.repo,'merge','other',check=False)
        before=git(self.repo,'ls-files','--stage').stdout
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['git']['merge_heads'],[other])
        self.assertEqual(data['git']['conflict_paths'],['owned.txt'])
        manifest=json.loads((Path(data['recovery']['path'])/'manifest.json').read_text())
        self.assertEqual([e['stage'] for e in manifest['index']],[1,2,3])
        self.assertEqual(manifest['merge_heads'],[other])
        self.assertEqual(git(self.repo,'ls-files','--stage').stdout,before)

    def test_unpublished_commit_recognized_without_checkpoint_hint(self):
        (self.repo/'owned.txt').write_text('local\n')
        git(self.repo,'commit','-am','local')
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['git']['publication'],'unpublished')
        self.assertIn('existing commit',data['next_action'])

    def test_uncertain_push_reconciles_actual_destination_even_cursor_lags(self):
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'branch':'main','commit':head}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['reconciliation']['effect'],'observed-published')
        self.assertFalse(data['reconciliation']['retry_safe'])

    def test_uncertain_api_effect_remains_unknown_no_replay(self):
        self.state['pending_operation']={'kind':'api','status':'uncertain','description':'lost response','identity':{'issue_number':3}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['reconciliation']['effect'],'unknown')
        self.assertFalse(data['reconciliation']['retry_safe'])

    def test_unavailable_remote_does_not_claim_unpublished(self):
        git(self.repo,'remote','set-url','origin',str(self.root/'gone.git'))
        values=dict(self.inputs,test_repository=str(self.root/'gone.git'))
        data,_=self.ok(self.invoke('observe',values,state=self.state))
        self.assertEqual(data['git']['publication'],'unknown')

    def test_protected_file_is_not_read_or_exported(self):
        (self.repo/'gh.tkn').write_text('SECRET_SENTINEL')
        (self.repo/'.gitignore').write_text('*.tkn\n')
        data,out=self.ok(self.invoke('observe',state=self.state))
        self.assertNotIn('SECRET_SENTINEL',out.read_text())
        exported=Path(data['recovery']['path'])
        self.assertFalse(any(b'SECRET_SENTINEL' in p.read_bytes() for p in exported.rglob('*') if p.is_file()))

    def test_secret_state_and_unknown_nested_field_fails_without_leak(self):
        for operation in [{'kind':'push','status':'uncertain','description':'github_pat_SECRET_SENTINEL'}, {'kind':'push','status':'uncertain','description':'lost','identity':{'token':'SECRET_SENTINEL'}}]:
            state=dict(self.state,pending_operation=operation)
            p,_,out=self.invoke('observe',state=state)
            self.assertNotEqual(p.returncode,0)
            self.assertNotIn('SECRET_SENTINEL',p.stdout+p.stderr)
            self.assertFalse(out.exists())

    def test_staged_deletion_and_unstaged_deletion_are_reconstructable(self):
        (self.repo/'unstaged.txt').write_text('retained baseline\n')
        git(self.repo,'add','unstaged.txt')
        git(self.repo,'commit','-m','second')
        git(self.repo,'rm','owned.txt')
        (self.repo/'unstaged.txt').unlink()
        data,_=self.ok(self.invoke('observe',state=self.state))
        manifest=json.loads((Path(data['recovery']['path'])/'manifest.json').read_text())
        self.assertEqual(data['git']['staged_paths'],['owned.txt'])
        self.assertEqual(data['git']['unstaged_paths'],['unstaged.txt'])
        self.assertNotIn('owned.txt',[e['path'] for e in manifest['index']])
        self.assertEqual(next(e['kind'] for e in manifest['workfiles'] if e['path']=='unstaged.txt'),'deleted')
        self.assertIn('owned.txt',manifest['tracked_paths'])
        export=Path(data['recovery']['path'])
        restored=self.root/'deleted-restore'
        git(self.root,'clone',str(self.repo),str(restored))
        git(restored,'checkout','main')
        git(restored,'read-tree','--empty')
        for entry in manifest['index']:
            subprocess.run(['git','-C',str(restored),'hash-object','-w','--stdin'],input=(export/'blobs'/entry['oid']).read_bytes(),check=True,capture_output=True)
        raw=''.join(f"{e['mode']} {e['oid']} {e['stage']}\t{e['path']}\n" for e in manifest['index'])
        subprocess.run(['git','-C',str(restored),'update-index','--index-info'],input=raw,text=True,check=True,capture_output=True)
        retained={e['path'] for e in manifest['workfiles'] if e['kind']!='deleted'}
        for name in manifest['tracked_paths']:
            if name not in retained and (restored/name).exists(): (restored/name).unlink()
        self.assertEqual(git(restored,'diff','--cached','--binary').stdout,git(self.repo,'diff','--cached','--binary').stdout)
        self.assertEqual(git(restored,'diff','--binary').stdout,git(self.repo,'diff','--binary').stdout)

    def test_remote_tip_with_unavailable_ancestry_remains_unknown(self):
        other=self.root/'other'
        git(self.root,'clone',str(self.remote),str(other))
        git(other,'checkout','main')
        git(other,'config','user.name','Fixture')
        git(other,'config','user.email','fixture@example.invalid')
        (other/'owned.txt').write_text('remote advance\n')
        git(other,'commit','-am','advance')
        git(other,'push','origin','main')
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['git']['publication'],'unknown')

    def test_index_conflict_export_restores_usable_merge_metadata(self):
        git(self.repo,'checkout','-b','other')
        (self.repo/'owned.txt').write_text('other\n')
        git(self.repo,'commit','-am','other')
        git(self.repo,'checkout','main')
        (self.repo/'owned.txt').write_text('main\n')
        git(self.repo,'commit','-am','main')
        incoming=git(self.repo,'rev-parse','other').stdout.strip()
        git(self.repo,'branch','-D','other')
        git(self.repo,'merge',incoming,check=False)
        data,_=self.ok(self.invoke('observe',state=self.state))
        export=Path(data['recovery']['path'])
        manifest=json.loads((export/'manifest.json').read_text())
        restored=self.root/'restored-conflict'
        git(self.root,'clone',str(self.remote),str(restored))
        git(restored,'fetch',str(export/'objects.bundle'),'refs/heads/main')
        git(restored,'checkout','-B','main',manifest['head'])
        for entry in manifest['index']:
            subprocess.run(['git','-C',str(restored),'hash-object','-w','--stdin'],input=(export/'blobs'/entry['oid']).read_bytes(),check=True,capture_output=True)
        git(restored,'read-tree','--empty')
        raw=''.join(f"{e['mode']} {e['oid']} {e['stage']}\t{e['path']}\n" for e in manifest['index'])
        subprocess.run(['git','-C',str(restored),'update-index','--index-info'],input=raw,text=True,check=True,capture_output=True)
        for entry in manifest['workfiles']:
            (restored/entry['path']).write_bytes((export/'files'/entry['sha256']).read_bytes())
        for name,content in manifest['merge_metadata'].items():
            path=Path(git(restored,'rev-parse','--git-path',name).stdout.strip())
            if not path.is_absolute(): path=restored/path
            path.write_text(content)
        self.assertEqual(git(restored,'ls-files','--stage').stdout,git(self.repo,'ls-files','--stage').stdout)
        self.assertEqual(git(restored,'diff','--binary').stdout,git(self.repo,'diff','--binary').stdout)
        self.assertEqual(git(restored,'rev-parse','MERGE_HEAD').stdout,git(self.repo,'rev-parse','MERGE_HEAD').stdout)
        self.assertTrue((restored/'.git/MERGE_MSG').exists())

    def test_parent_symlink_cannot_export_external_workfile_contents(self):
        nested=self.repo/'nested'
        nested.mkdir()
        (nested/'file.txt').write_text('baseline\n')
        git(self.repo,'add','nested')
        git(self.repo,'commit','-m','nested')
        (nested/'file.txt').unlink()
        nested.rmdir()
        foreign=self.root/'foreign'
        foreign.mkdir()
        (foreign/'file.txt').write_text('EXTERNAL_SENTINEL')
        nested.symlink_to(foreign,target_is_directory=True)
        p,data,out=self.invoke('observe',state=self.state)
        self.assertNotEqual(p.returncode,0)
        self.assertFalse(out.exists())
        self.assertNotIn('EXTERNAL_SENTINEL',p.stdout+p.stderr)

    def test_uncertain_push_explicit_ref_overrides_current_branch_publication(self):
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'branch':'main','ref':'refs/heads/missing-target','commit':head}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['git']['publication'],'published')
        self.assertEqual(data['reconciliation']['effect'],'not-observed-at-destination')
        self.assertFalse(data['reconciliation']['retry_safe'])

    def test_uncertain_push_explicit_ref_with_unknown_ancestry_stays_unknown(self):
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        other=self.root/'incoming-push'
        git(self.root,'clone',str(self.remote),str(other))
        git(other,'checkout','main')
        git(other,'config','user.name','Fixture')
        git(other,'config','user.email','fixture@example.invalid')
        (other/'owned.txt').write_text('remote advance\n')
        git(other,'commit','-am','advance')
        git(other,'push','origin','HEAD:refs/heads/other-target')
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'branch':'main','ref':'refs/heads/other-target','commit':head}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['reconciliation']['effect'],'unknown')

    def test_uncertain_push_recorded_repository_mismatch_is_unknown(self):
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        self.state['repository']={'identity':str(self.remote)}
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'repository':str(self.root/'different.git'),'branch':'main','commit':head}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['reconciliation']['effect'],'unknown')

    def test_uncertain_push_explicit_target_ancestor_is_published_when_current_branch_is_not(self):
        (self.repo/'owned.txt').write_text('candidate\n')
        git(self.repo,'commit','-am','candidate')
        candidate=git(self.repo,'rev-parse','HEAD').stdout.strip()
        git(self.repo,'checkout','-b','other-target')
        (self.repo/'owned.txt').write_text('descendant\n')
        git(self.repo,'commit','-am','descendant')
        git(self.repo,'push','origin','other-target')
        git(self.repo,'checkout','main')
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'repository':str(self.remote),'branch':'main','ref':'refs/heads/other-target','commit':candidate}}
        data,_=self.ok(self.invoke('observe',state=self.state))
        self.assertEqual(data['git']['publication'],'unpublished')
        self.assertEqual(data['reconciliation']['effect'],'observed-published')
        self.assertFalse(data['reconciliation']['retry_safe'])

    def test_shallow_checkout_with_both_endpoints_keeps_unproven_containment_unknown(self):
        candidate=git(self.repo,'rev-parse','HEAD').stdout.strip()
        git(self.repo,'branch','candidate',candidate)
        (self.repo/'owned.txt').write_text('middle\n')
        git(self.repo,'commit','-am','middle')
        middle=git(self.repo,'rev-parse','HEAD').stdout.strip()
        (self.repo/'owned.txt').write_text('destination\n')
        git(self.repo,'commit','-am','destination')
        destination=git(self.repo,'rev-parse','HEAD').stdout.strip()
        git(self.repo,'push','origin','main','candidate')
        self.assertEqual(git(self.repo,'merge-base','--is-ancestor',candidate,destination).returncode,0)
        shallow=self.root/'shallow'
        git(self.root,'clone','--depth','2','--no-single-branch','--branch','main',self.remote.as_uri(),str(shallow))
        git(shallow,'checkout','-B','main',candidate)
        for commit in (candidate,destination):
            self.assertEqual(git(shallow,'cat-file','-e',commit+'^{commit}').returncode,0)
        self.assertEqual(git(shallow,'rev-parse','--is-shallow-repository').stdout.strip(),'true')
        self.assertEqual(git(shallow,'merge-base','--is-ancestor',candidate,destination,check=False).returncode,1)
        before=(git(shallow,'for-each-ref').stdout,git(shallow,'status','--porcelain').stdout,(shallow/'.git/shallow').read_bytes(),git(shallow,'cat-file','--batch-all-objects','--batch-check=%(objectname)').stdout)
        spec=importlib.util.spec_from_file_location('textstats_core',Path(__file__).resolve().parents[1]/'scripts/core.py')
        core=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(core)
        inputs=dict(self.inputs,test_repository=self.remote.as_uri(),local_checkout=str(shallow))
        self.state['pending_operation']={'kind':'push','status':'uncertain','description':'lost response','identity':{'repository':self.remote.as_uri(),'ref':'refs/heads/main','commit':candidate}}
        # Exercise readback without recovery export: shallow bundle portability is outside this ancestry check.
        data=core.observation(inputs,self.state,self.root/'unused-output',exports=False)
        for actual,expected in ((data['git']['publication'],'unknown'),(data['git']['remote_containment'],'ancestry-unavailable'),(data['reconciliation']['effect'],'unknown')):
            with self.subTest(actual=actual,expected=expected): self.assertEqual(actual,expected)
        self.assertFalse(data['reconciliation']['retry_safe'])
        self.assertEqual(before,(git(shallow,'for-each-ref').stdout,git(shallow,'status','--porcelain').stdout,(shallow/'.git/shallow').read_bytes(),git(shallow,'cat-file','--batch-all-objects','--batch-check=%(objectname)').stdout))
        # Equality and a visible positive ancestry path still establish the exact pending effect.
        for commit in (destination,middle):
            with self.subTest(proven_commit=commit):
                self.state['pending_operation']['identity']['commit']=commit
                data=core.observation(inputs,self.state,self.root/'unused-output',exports=False)
                self.assertEqual(data['reconciliation']['effect'],'observed-published')
        git(shallow,'checkout','-B','main',middle)
        data=core.observation(inputs,self.state,self.root/'unused-output',exports=False)
        self.assertEqual(data['git']['publication'],'published')
        self.assertEqual(data['git']['remote_containment'],'ancestor')
