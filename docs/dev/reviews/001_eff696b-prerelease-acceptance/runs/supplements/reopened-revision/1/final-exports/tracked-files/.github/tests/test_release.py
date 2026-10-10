"""Publisher contracts: real Git/ZIP fixtures and controlled provider boundaries."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile
import warnings

SCRIPT = Path(__file__).parents[1] / 'scripts' / 'release.py'
if SCRIPT.exists():
    spec = importlib.util.spec_from_file_location('publisher', SCRIPT)
    publisher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(publisher)
else:
    publisher = None


def handoff(**changes):
    notes = '## Changes\n\nHuman section — $(touch SHOULD_NOT_EXIST)\n'
    data = dict(source='a' * 40, tag='v0.15.0', notes_source='a' * 40,
                notes=notes, notes_sha256=hashlib.sha256(notes.encode()).hexdigest(),
                publish=False, prerelease=False, make_latest=False, request_id='trial-001')
    data.update(changes)
    return data


class Contract(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(publisher, 'Selected publisher implementation is absent')


class HandoffTests(Contract):
    def test_curated_multiline_bytes_survive(self):
        data = handoff()
        self.assertEqual(publisher.validate_handoff(data), data)
        self.assertFalse(Path('SHOULD_NOT_EXIST').exists())

    def test_invalid_inputs_stop(self):
        for changes in ({'source': 'main'}, {'notes_source': 'b'*40},
                        {'notes_sha256': '0'*64}, {'notes': ''},
                        {'notes': '---\nx: y\n---\nbody'}, {'notes': 'x'*60001},
                        {'publish': 'false'}, {'unknown': 'value'},
                        {'tag': 'v0.15.0;evil'}, {'prerelease': True, 'make_latest': True}):
            with self.subTest(changes=list(changes)), self.assertRaises(ValueError):
                publisher.validate_handoff(handoff(**changes))

    def test_missing_field_stops(self):
        data=handoff(); del data['notes_source']
        with self.assertRaises(ValueError): publisher.validate_handoff(data)


class PackageTests(Contract):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/'repo'; self.root.mkdir()
        def git(*args):
            return subprocess.check_output(['git','-C',str(self.root),*args], text=True).strip()
        self.git=git
        git('init','-q'); git('config','user.name','Fixture'); git('config','user.email','fixture@example.test')
        manifest=b'{"name":"sdd-manager","version":"0.15.0"}\n'
        for name in ('LICENSE','README.md','AGENTS.md','Greenfield Project Prompt Template.md',
                     'SDD-MANAGER.md','AI_DISCLOSURE.md','assets/icon.svg','skills/sample/SKILL.md',
                     '.codex-plugin/plugin.json','plugin.json','docs/excluded.md'):
            p=self.root/name; p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(manifest if name.endswith('plugin.json') else (name+'\n').encode())
        git('add','.'); git('commit','-qm','fixture'); self.sha=git('rev-parse','HEAD')
        self.data=handoff(source=self.sha,notes_source=self.sha)
        self.out=Path(self.tmp.name)/'output'; self.out.mkdir()

    def test_archive_matches_exact_tree_and_exclusions(self):
        paths=publisher.build_package(self.root,self.data,self.out)
        self.assertEqual(set(paths),{'sdd-manager.zip','sdd-manager.zip.sha256'})
        with zipfile.ZipFile(paths['sdd-manager.zip']) as z:
            self.assertNotIn('sdd-manager/docs/excluded.md',z.namelist())
            self.assertEqual(z.read('sdd-manager/README.md'),b'README.md\n')
        raw=paths['sdd-manager.zip'].read_bytes()
        self.assertEqual(paths['sdd-manager.zip.sha256'].read_text(),hashlib.sha256(raw).hexdigest()+'  sdd-manager.zip\n')

    def test_wrong_checkout_or_version_stops(self):
        for changes in ({'source':'a'*40,'notes_source':'a'*40},{'tag':'v9.9.9'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                publisher.build_package(self.root,dict(self.data,**changes),self.out)

    def test_mismatched_manifest_stops(self):
        (self.root/'.codex-plugin/plugin.json').write_text('{}')
        self.git('add','.'); self.git('commit','-qm','mismatch')
        sha=self.git('rev-parse','HEAD')
        with self.assertRaises(ValueError): publisher.build_package(self.root,handoff(source=sha,notes_source=sha),self.out)

    def test_actual_archive_tampering_stops(self):
        paths=publisher.build_package(self.root,self.data,self.out)
        for bad_name in ('sdd-manager/README.md','sdd-manager/../escape'):
            with self.subTest(name=bad_name):
                bad=self.out/'bad.zip'
                with zipfile.ZipFile(paths['sdd-manager.zip']) as original, zipfile.ZipFile(bad,'w') as z:
                    for item in original.infolist():
                        if not item.is_dir(): z.writestr(item.filename,original.read(item.filename))
                    with warnings.catch_warnings():
                        warnings.filterwarnings('ignore', message='Duplicate name:', category=UserWarning)
                        z.writestr(bad_name,b'wrong')
                with self.assertRaises(ValueError): publisher.inspect_archive(self.root,self.sha,bad)


class Provider:
    """Controlled external boundary, independent of publisher decisions."""
    def __init__(self):
        self.source='a'*40; self.release=None; self.latest=19; self.events=[]; self.bytes={}; self.fail_upload=False
    def tag_source(self,tag): self.events.append('tag'); return self.source
    def latest_id(self): self.events.append('latest'); return self.latest
    def find_release(self,tag): self.events.append('read'); return copy.deepcopy(self.release)
    def get_release(self,release_id):
        self.events.append('read-id')
        if self.release is None or self.release['id'] != release_id: return None
        return copy.deepcopy(self.release)
    def create_draft(self,data):
        self.events.append('create')
        self.release=dict(id=23,tag_name=data['tag'],name='SDD Manager '+data['tag'],body=data['notes'],draft=True,prerelease=data['prerelease'],assets=[])
        return copy.deepcopy(self.release)
    def upload(self,release,name,raw):
        self.events.append('upload:'+name)
        if self.fail_upload: raise OSError('controlled upload failure')
        asset=dict(id=len(self.bytes)+1,name=name,size=len(raw),state='uploaded')
        self.bytes[asset['id']]=raw; self.release['assets'].append(asset)
    def download(self,asset): self.events.append('download'); return self.bytes[asset['id']]
    def publish(self,release,data):
        self.events.append('publish'); self.release['draft']=False
        if data['make_latest']: self.latest=self.release['id']


class LifecycleTests(Contract):
    def setUp(self):
        super().setUp(); self.api=Provider(); self.files={'sdd-manager.zip':b'archive','sdd-manager.zip.sha256':b'checksum'}
    def run_release(self,**changes): return publisher.reconcile_release(self.api,handoff(publish=True,**changes),self.files)
    def test_first_publish_uploads_before_publish_and_reads_back(self):
        result=self.run_release()
        self.assertFalse(result['draft']); self.assertEqual(self.api.latest,19)
        self.assertLess(self.api.events.index('upload:sdd-manager.zip.sha256'),self.api.events.index('publish'))
        self.assertTrue(any(x in ('read', 'read-id') for x in self.api.events[self.api.events.index('publish')+1:]))
    def test_fresh_publish_survives_lagging_release_inventory(self):
        # The provider acknowledges creation, but its global inventory lags.
        self.api.find_release=lambda tag: None
        result=self.run_release()
        self.assertFalse(result['draft'])
        self.assertEqual(self.api.events.count('create'),1)
        self.assertEqual(set(a['name'] for a in result['assets']),set(self.files))
    def test_missing_acknowledged_release_stops_without_recreating(self):
        self.api.get_release=lambda release_id: None
        with self.assertRaises(ValueError): self.run_release()
        self.assertEqual(self.api.events.count('create'),1)
        self.assertFalse(any(x.startswith(('upload','publish')) for x in self.api.events))
    def test_direct_read_cannot_substitute_another_release_identity(self):
        original=self.api.get_release
        def wrong(release_id):
            release=original(release_id); release['id']=99; return release
        self.api.get_release=wrong
        with self.assertRaises(ValueError): self.run_release()
        self.assertEqual(self.api.events.count('create'),1)
        self.assertFalse(any(x.startswith(('upload','publish')) for x in self.api.events))
    def test_complete_rerun_has_no_mutation(self):
        self.run_release(); self.api.events=[]; self.run_release()
        self.assertFalse(any(x.startswith(('create','upload','publish')) for x in self.api.events))
    def test_partial_draft_uploads_only_missing(self):
        self.api.create_draft(handoff()); self.api.upload(self.api.release,'sdd-manager.zip',b'archive'); self.api.events=[]
        self.run_release()
        self.assertNotIn('upload:sdd-manager.zip',self.api.events)
        self.assertIn('upload:sdd-manager.zip.sha256',self.api.events)
    def test_upload_failure_retains_draft(self):
        self.api.fail_upload=True
        with self.assertRaises(OSError): self.run_release()
        self.assertTrue(self.api.release['draft']); self.assertNotIn('publish',self.api.events)
    def test_wrong_tag_stops_before_mutation(self):
        self.api.source='b'*40
        with self.assertRaises(ValueError): self.run_release()
        self.assertNotIn('create',self.api.events)
    def test_conflicting_body_foreign_duplicate_starter_and_bytes_stop(self):
        for kind in ('body','foreign','duplicate','starter','bytes'):
            with self.subTest(kind=kind):
                self.api=Provider(); self.api.create_draft(handoff())
                self.api.upload(self.api.release,'sdd-manager.zip',b'archive')
                if kind=='body': self.api.release['body']='foreign'
                if kind=='foreign': self.api.upload(self.api.release,'foreign',b'x')
                if kind=='duplicate': self.api.release['assets'].append(copy.deepcopy(self.api.release['assets'][0]))
                if kind=='starter': self.api.release['assets'][0]['state']='starter'
                if kind=='bytes': self.api.bytes[1]=b'changed'
                self.api.events=[]
                with self.assertRaises(ValueError): self.run_release()
                self.assertFalse(any(x.startswith(('create','upload','publish')) for x in self.api.events))
    def test_build_only_has_no_provider_calls(self):
        publisher.reconcile_release(self.api,handoff(),self.files)
        self.assertEqual(self.api.events,[])
    def test_latest_readback_detects_unexpected_change(self):
        original=self.api.publish
        def changed(release,data): original(release,data); self.api.latest=88
        self.api.publish=changed
        with self.assertRaises(ValueError): self.run_release()
    def test_opt_in_latest_is_verified(self):
        self.run_release(make_latest=True); self.assertEqual(self.api.latest,23)
    def test_uncertain_upload_is_not_blindly_replayed(self):
        original=self.api.upload
        def uncertain(release,name,raw): original(release,name,raw); raise OSError('response lost after effect')
        self.api.upload=uncertain
        with self.assertRaises(OSError): self.run_release()
        self.assertTrue(self.api.release['draft']); self.api.upload=original; self.api.events=[]
        self.run_release(); self.assertNotIn('upload:sdd-manager.zip',self.api.events)


class AdapterTests(Contract):
    def setUp(self):
        super().setUp()
        self.assertTrue(hasattr(publisher, 'GitHub'), 'Actual provider adapter is absent')

    def test_annotated_tag_is_peeled(self):
        replies=[{'object':{'type':'tag','sha':'b'*40}}, {'object':{'type':'commit','sha':'a'*40}}]
        calls=[]
        def request(method,path,**kwargs): calls.append((method,path)); return replies.pop(0)
        api=publisher.GitHub('owner/repo', request=request)
        self.assertEqual(api.tag_source('v0.15.0'),'a'*40)
        self.assertIn('/git/tags/',calls[1][1])

    def test_complete_assets_are_paginated(self):
        calls=[]
        def request(method,path,**kwargs):
            calls.append(path)
            if '/releases?' in path: return [dict(id=23,tag_name='v0.15.0',assets=[])]
            if '&page=1' in path: return [dict(id=i,name=str(i)) for i in range(100)]
            return [dict(id=101,name='last')]
        api=publisher.GitHub('owner/repo',request=request)
        self.assertEqual(len(api.find_release('v0.15.0')['assets']),101)
        self.assertTrue(any('page=2' in path for path in calls))

    def test_missing_lookup_and_transport_failure_are_distinct(self):
        api=publisher.GitHub('owner/repo',request=lambda *a,**k:None)
        self.assertIsNone(api.tag_source('v0.15.0'))
        with self.assertRaises(ValueError): api.find_release('v0.15.0')

    def test_direct_release_read_uses_acknowledged_id_and_complete_assets(self):
        calls=[]
        def request(method,path,**kwargs):
            calls.append((method,path))
            if path.endswith('/releases/23'): return dict(id=23,tag_name='v0.15.0',assets=[])
            if '&page=1' in path: return [dict(id=i,name=str(i)) for i in range(100)]
            return [dict(id=101,name='last')]
        api=publisher.GitHub('owner/repo',request=request)
        self.assertTrue(hasattr(api,'get_release'), 'Direct acknowledged-ID readback is absent')
        self.assertEqual(len(api.get_release(23)['assets']),101)
        self.assertEqual(calls[0],('GET',api.base+'/releases/23'))
        self.assertTrue(all(method=='GET' for method,path in calls))
        self.assertTrue(any('page=2' in path for method,path in calls))

    def test_body_and_upload_are_structured_data(self):
        calls=[]
        def request(method,path,**kwargs): calls.append((method,path,kwargs)); return {'id':23}
        api=publisher.GitHub('owner/repo',request=request)
        api.create_draft(handoff()); api.upload({'id':23},'sdd-manager.zip',b'actual')
        self.assertEqual(calls[0][2]['data']['body'],handoff()['notes'])
        self.assertTrue(calls[0][2]['data']['draft'])
        self.assertEqual(calls[1][2]['data'],b'actual')
        self.assertTrue(calls[1][1].startswith('https://uploads.github.com/'))

    def test_event_handoff_is_read_as_data(self):
        self.assertTrue(hasattr(publisher, 'read_event'), 'Workflow event reader is absent')
        with tempfile.TemporaryDirectory() as directory:
            event=Path(directory)/'event.json'
            event.write_text(json.dumps({'inputs':{'handoff':json.dumps(handoff())}}))
            self.assertEqual(publisher.read_event(event),handoff())


if __name__=='__main__': unittest.main()
