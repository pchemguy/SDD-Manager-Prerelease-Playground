"""Asset/graph/handoff sensitivity; these tests never represent consumer acceptance."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

from .support import Sandbox, git

ASSESSOR=Path(__file__).resolve().parents[1]/'cases/assessor'
def module(name):
    spec=importlib.util.spec_from_file_location('textstats_'+name,ASSESSOR/(name+'.py'))
    value=importlib.util.module_from_spec(spec); spec.loader.exec_module(value); return value
catalog=module('catalog_tools'); capture=module('capture')

class CatalogIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'bundle'
        shutil.copytree(ASSESSOR.parents[1],self.root)
        self.value=json.loads((self.root/'cases/catalog.json').read_text())

    def test_all27_resolve_and_contracts_have_independent_criteria(self):
        result=catalog.validate_catalog(self.root)
        self.assertEqual(set(result),catalog.IDS)
        for case in result.values():
            contract=json.loads((self.root/case['assessor_contract']).read_text())
            self.assertTrue(contract['checks']); self.assertTrue(contract['required_agent_checks'])

    def test_duplicate_missing_and_invalid_ids_fail(self):
        for mutation in ['duplicate','missing','invalid']:
            value=copy.deepcopy(self.value)
            if mutation=='duplicate': value['cases'][1]['id']=value['cases'][0]['id']
            if mutation=='missing': value['cases'].pop()
            if mutation=='invalid': value['cases'][0]['id']='A-999'
            with self.subTest(mutation=mutation),self.assertRaises(ValueError): catalog.validate_catalog(self.root,value)

    def test_real_dependency_cycle_and_unknown_prerequisite_fail(self):
        cyclic=copy.deepcopy(self.value)
        cyclic['cases'][0]['dependencies']=['A-002']; cyclic['cases'][0]['checkpoint_bindings']['start']['from_case']='A-002'
        with self.assertRaisesRegex(ValueError,'cycle'): catalog.validate_catalog(self.root,cyclic)
        invalid=copy.deepcopy(self.value); invalid['cases'][1]['dependencies']=['A-999']
        with self.assertRaisesRegex(ValueError,'prerequisite'): catalog.validate_catalog(self.root,invalid)

    def test_missing_duplicate_and_escaping_assets_fail(self):
        for path in ['cases/consumer/missing.md','../outside.md',self.value['cases'][0]['consumer_input']]:
            value=copy.deepcopy(self.value); value['cases'][1]['consumer_input']=path
            with self.subTest(path=path),self.assertRaises(ValueError): catalog.validate_catalog(self.root,value)

    def test_empty_contract_and_invalid_dsl_fail(self):
        path=self.root/'cases/assessor/A-002.json'; value=json.loads(path.read_text())
        for checks in [[],[{'id':'invented','kind':'auto_pass'}],[{'id':'head','kind':'git','field':'head','expected_ref':'checkpoint_refs.historical_task_id'}]]:
            changed=copy.deepcopy(value); changed['checks']=checks; path.write_text(json.dumps(changed))
            with self.assertRaises(ValueError): catalog.validate_catalog(self.root)

    def test_optional_ownership_documents_contract_validation(self):
        def contract(documents):
            return {'schema_version': 1, 'case_id': 'A-002',
                    'checks': [{'id': 'owners', 'kind': 'task_ownership', 'documents': documents}],
                    'required_agent_checks': ['Assess actual task-list coverage independently.']}
        catalog.validate_contract(contract(['docs/dev/tasks/slice.md']), 'A-002')
        for documents in [[], 'docs/dev/tasks/slice.md', [False], ['../escape.md'], ['/absolute.md'],
                          ['gh.tkn'], ['docs/dev/reviews/old/TASKS.md'],
                          ['docs/dev/tasks/slice.md', 'docs/dev/tasks/slice.md']]:
            with self.subTest(documents=documents), self.assertRaises(ValueError):
                catalog.validate_contract(contract(documents), 'A-002')

    def test_route_answer_leakage_and_missing_trigger_fail(self):
        path=self.root/'cases/consumer/A-012.md'; original=path.read_text()
        path.write_text(original+'\nThe expected routing is sdd-steer.\n')
        with self.assertRaisesRegex(ValueError,'leakage'): catalog.validate_catalog(self.root)
        path.write_text(original)
        value=copy.deepcopy(self.value); value['cases'][14].pop('interruption_trigger')
        with self.assertRaisesRegex(ValueError,'protocol'): catalog.validate_catalog(self.root,value)

    def test_historical_fixed_identity_and_expected_import_absent(self):
        for path in (self.root/'cases').rglob('*'):
            if path.is_file() and path.suffix in {'.md','.json','.py'}:
                self.assertNotRegex(path.read_text(),r'AgentPlayground|/workspace/scratch/|\b[0-9a-f]{40}\b')
        self.assertNotIn('expected.json',capture.Path(capture.__file__).read_text())

class HandoffIntegrity(Sandbox):
    def bindings(self, case_id="A-001"):
        # Synthetic independent predecessor identity; actual publication is still checked.
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        refs={'product_commit':head,'product_branch':'main','integration_commit':head,'integration_branch':'main'}
        assessment={'case_id':case_id,'status':'Passed','agent_behavior_assessed':True,'checkpoint_refs':refs}
        path=self.repo/'independent.json'; path.write_text(json.dumps(assessment))
        git(self.repo,'add','independent.json'); git(self.repo,'commit','-m','independent assessment'); git(self.repo,'push')
        evidence=git(self.repo,'rev-parse','HEAD').stdout.strip()
        point={'case_id':case_id,'status':'Passed','assessment_path':'independent.json','checkpoint_refs':refs,'local_checkout':str(self.repo),'remote':'origin','remote_ref':'refs/heads/main','evidence_publication':{'status':'published','commit':evidence,'path':'independent.json','remote':'origin','ref':'refs/heads/main'}}
        return {'checkpoints':[point],'current':{'summary':'Authorized selection only. Actual main checkout contains prepared product work.'}}

    def test_render_uses_only_request_and_actual_current_state(self):
        value=self.bindings(); rendered=catalog.render('A-002',value,bindings_root=self.repo)
        self.assertIn('Select work only',rendered); self.assertIn(value['current']['summary'],rendered)
        self.assertNotIn('Independent lifecycle',rendered); self.assertNotIn('correct owning',rendered)

    def test_missing_ambiguous_and_unassessed_checkpoint_fail(self):
        value=self.bindings()
        for changed in [dict(value,checkpoints=[]),dict(value,checkpoints=value['checkpoints']*2)]:
            with self.assertRaises(ValueError): catalog.render('A-002',changed,bindings_root=self.repo)
        path=self.repo/'independent.json'; grade=json.loads(path.read_text()); grade['agent_behavior_assessed']=False; path.write_text(json.dumps(grade))
        with self.assertRaisesRegex(ValueError,'independent assessment'): catalog.render('A-002',value,bindings_root=self.repo)

    def test_unpublished_actual_ref_and_mismatched_published_evidence_fail(self):
        value=self.bindings(); git(self.repo,'commit','--allow-empty','-m','unpublished actual task')
        new=git(self.repo,'rev-parse','HEAD').stdout.strip()
        value['checkpoints'][0]['checkpoint_refs']['product_commit']=new
        path=self.repo/'independent.json'; grade=json.loads(path.read_text()); grade['checkpoint_refs']=value['checkpoints'][0]['checkpoint_refs']; path.write_text(json.dumps(grade))
        with self.assertRaisesRegex(ValueError,'published at exact destination'): catalog.render('A-002',value,bindings_root=self.repo)
        git(self.repo,'push')
        with self.assertRaisesRegex(ValueError,'published assessment differs'): catalog.render('A-002',value,bindings_root=self.repo)

    def test_selected_placeholders_require_actual_values(self):
        value=self.bindings('A-004')
        with self.assertRaisesRegex(ValueError,'selected input'): catalog.render('A-014',value,bindings_root=self.repo)
        value['current'].update(range_start='observed first owner',range_end='observed final owner')
        text=catalog.render('A-014',value,bindings_root=self.repo)
        self.assertIn('observed first owner through observed final owner',text)
        self.assertNotIn('{{',text)

    def test_initial_empty_product_and_final_failed_campaign_do_not_require_successful_product(self):
        value={'checkpoints':[],'current':{'summary':'P0 operating baseline published; no product implementation. Prepare within authorized repository.'}}
        self.assertIn('Prepare TextStats',catalog.render('A-001',value))
        value['current']['summary']='Product work blocked at preparation; report actual retained state only.'
        self.assertIn('Product status',catalog.render('A-027',value))

class CaptureSensitivity(Sandbox):
    def test_raw_actual_command_status_channels_are_retained(self):
        journal=[]
        proc=capture.invoke([sys.executable,'-c','import sys; print("observed"); sys.stderr.write("diagnostic\\n"); sys.exit(7)'],self.root,dict(__import__('os').environ),b'',journal)
        self.assertEqual(proc.returncode,7); self.assertEqual(journal[0]['stdout'],'observed\n'); self.assertEqual(journal[0]['stderr'],'diagnostic\n')
        self.assertTrue(journal[0]['stdout_base64']); self.assertEqual(journal[0]['command'][0],sys.executable)

    def test_error_facts_are_derived_from_actual_status_channels_and_fixture(self):
        vector={'name':'decode','error':True,'json':False,'stdin':False,'source_identification':True}
        from subprocess import CompletedProcess
        proc=CompletedProcess(['actual'],0,b'false success',b'Traceback (most recent call last)\n')
        observed=capture.cli_observation(vector,proc,'before','different','decode.txt')
        self.assertEqual(observed['returncode'],0); self.assertEqual(observed['stdout'],'false success')
        self.assertFalse(observed['unchanged']); self.assertFalse(observed['no_traceback']); self.assertFalse(observed['source_identified'])

    def test_each_literal_suite_detects_changed_actual_evidence(self):
        expected=json.loads((ASSESSOR/'expected.json').read_text())['literals']
        for suite,constant in expected.items():
            contract=self.root/(suite+'.json'); contract.write_text(json.dumps({'schema_version':1,'checks':[{'id':'literal','kind':'literal','key':suite,'expected':constant}]}))
            evidence=self.root/(suite+'-actual.json'); evidence.write_text(json.dumps({'schema_version':1,'literals':{suite:constant}}))
            result,code=catalog.core.assessment(self.inputs,self.state,contract,evidence)
            self.assertEqual(code,0)
            evidence.write_text(json.dumps({'schema_version':1,'literals':{suite:{'corrupt_actual_output':True}}}))
            result,code=catalog.core.assessment(self.inputs,self.state,contract,evidence)
            self.assertEqual(code,1); self.assertFalse(result['agent_behavior_assessed'])

    def test_all_shipped_contracts_are_consumed_by_actual_helper_dsl(self):
        # Expected literals are intentionally supplied for DSL consumability only;
        # this is not execution of TextStats or independent lifecycle acceptance.
        (self.repo/'TASKS.md').write_text('- [ ] T-FIXTURE-ONE synthetic checker owner\n')
        git(self.repo,'add','TASKS.md'); git(self.repo,'commit','-m','nonempty DSL task fixture'); git(self.repo,'push')
        head=git(self.repo,'rev-parse','HEAD').stdout.strip()
        self.state['checkpoint_refs']={'product_commit':head,'merge_parents':git(self.repo,'show','-s','--format=%P','HEAD').stdout.split()}
        for path in sorted(ASSESSOR.glob('A-*.json')):
            contract=json.loads(path.read_text())
            literals={c['key']:c['expected'] for c in contract['checks'] if c['kind']=='literal'}
            evidence=self.root/'dsl-evidence.json'; evidence.write_text(json.dumps({'schema_version':1,'literals':literals}))
            result,code=catalog.core.assessment(self.inputs,self.state,path,evidence)
            with self.subTest(contract=path.name):
                self.assertEqual(code,0,result)
                self.assertFalse(result['agent_behavior_assessed'])

    def test_capture_import_origin_rejects_unavailable_product(self):
        with self.assertRaises(ValueError): capture.capture(self.root,'baseline')

class FailedCaptureProvenance(Sandbox):
    def cli(self,product=None,python=None,occupied=False):
        import subprocess
        output=self.root/'capture.json'; provenance=self.root/'commands.json'
        if occupied: provenance.write_text('original attempt')
        command=[sys.executable,str(ASSESSOR/'capture.py'),'--product-root',str(product or self.root),'--suite','baseline','--output',str(output),'--provenance',str(provenance)]
        if python: command += ['--python',str(python)]
        proc=subprocess.run(command,capture_output=True,text=True)
        return proc,output,provenance

    def test_actual_cli_import_failure_retains_first_attempt_channels(self):
        (self.root/'textstats.py').write_text('import sys\nprint("FIRST_IMPORT_STDOUT_MARKER")\nsys.stderr.write("FIRST_IMPORT_STDERR_MARKER\\n")\nraise RuntimeError("observed import failure")\n')
        proc,output,provenance=self.cli()
        self.assertEqual(proc.returncode,2); self.assertFalse(output.exists())
        self.assertTrue(provenance.exists(),'failed first attempt provenance must survive')
        data=json.loads(provenance.read_text())
        self.assertEqual(data['status'],'Failed')
        self.assertEqual(data['commands'][0]['returncode'],1)
        self.assertIn('FIRST_IMPORT_STDOUT_MARKER',data['commands'][0]['stdout'])
        self.assertIn('FIRST_IMPORT_STDERR_MARKER',data['commands'][0]['stderr'])
        self.assertIn('RuntimeError',data['commands'][0]['stderr'])

    def test_timeout_preserves_actual_partial_channels_and_not_completed_status(self):
        import subprocess
        def timeout(command,**kwargs):
            raise subprocess.TimeoutExpired(command,30,output=b'FIRST_TIMEOUT_STDOUT',stderr=b'FIRST_TIMEOUT_STDERR')
        journal=[]
        with self.assertRaises(subprocess.TimeoutExpired):
            capture.invoke([sys.executable,'-c','actual command'],self.root,{},b'',journal,runner=timeout)
        self.assertEqual(len(journal),1,'started timed-out command must survive')
        self.assertEqual(journal[0]['status'],'Timed out'); self.assertIsNone(journal[0]['returncode'])
        self.assertEqual(journal[0]['stdout'],'FIRST_TIMEOUT_STDOUT'); self.assertEqual(journal[0]['stderr'],'FIRST_TIMEOUT_STDERR')
        self.assertTrue(journal[0]['stdout_base64']); self.assertTrue(journal[0]['stderr_base64'])

    def test_cli_launch_failure_and_occupied_attempt_are_preserved(self):
        proc,output,provenance=self.cli(python=self.root/'absent-interpreter')
        self.assertEqual(proc.returncode,2); self.assertFalse(output.exists())
        command=json.loads(provenance.read_text())['commands'][0]
        self.assertEqual(command['status'],'Not started'); self.assertIsNone(command['returncode'])
        self.assertEqual(command['launch_error'],'FileNotFoundError')
        original=provenance.read_bytes()
        proc,output,provenance=self.cli()
        self.assertEqual(proc.returncode,2); self.assertEqual(provenance.read_bytes(),original); self.assertFalse(output.exists())

    def test_cli_later_timeout_retains_prior_command_and_partial_bytes(self):
        import contextlib,io,subprocess
        from unittest.mock import patch
        (self.root/'textstats.py').write_text('# Empty module used only for actual import-origin observation.\n')
        output=self.root/'timeout-literals.json'; provenance=self.root/'timeout-commands.json'
        calls=[]
        def runner(command,**kwargs):
            calls.append(command)
            if len(calls)==1: return subprocess.run(command,**kwargs)
            raise subprocess.TimeoutExpired(command,30,output=b'PARTIAL_SUITE_STDOUT',stderr=b'PARTIAL_SUITE_STDERR')
        original=capture.capture
        def timed_capture(root,suite,python,provenance):
            return original(root,suite,python,runner=runner,provenance=provenance)
        args=['capture','--product-root',str(self.root),'--suite','baseline','--output',str(output),'--provenance',str(provenance)]
        with patch.object(sys,'argv',args),patch.object(capture,'capture',timed_capture),contextlib.redirect_stdout(io.StringIO()):
            code=capture.main()
        self.assertEqual(code,2); self.assertFalse(output.exists())
        data=json.loads(provenance.read_text()); self.assertEqual(data['status'],'Failed'); self.assertEqual(len(data['commands']),2)
        self.assertTrue(data['commands'][0]['origin_accepted'])
        self.assertEqual(data['commands'][1]['status'],'Timed out'); self.assertIsNone(data['commands'][1]['returncode'])
        self.assertEqual(data['commands'][1]['stdout'],'PARTIAL_SUITE_STDOUT'); self.assertEqual(data['commands'][1]['stderr'],'PARTIAL_SUITE_STDERR')

    def test_failed_capture_withholds_protected_partial_output(self):
        import contextlib,io,subprocess
        from unittest.mock import patch
        secret='ghp_'+'SYNTHETIC_NOT_A_CREDENTIAL'
        def runner(command,**kwargs):
            raise subprocess.TimeoutExpired(command,30,output=b'safe partial',stderr=secret.encode())
        output=self.root/'blocked-literals.json'; provenance=self.root/'blocked-commands.json'
        original=capture.capture
        def protected_capture(root,suite,python,provenance):
            return original(root,suite,python,runner=runner,provenance=provenance)
        args=['capture','--product-root',str(self.root),'--suite','baseline','--output',str(output),'--provenance',str(provenance)]
        with patch.object(sys,'argv',args),patch.object(capture,'capture',protected_capture),contextlib.redirect_stdout(io.StringIO()) as stdout:
            code=capture.main()
        self.assertEqual(code,2); self.assertFalse(output.exists()); self.assertTrue(provenance.exists())
        retained=provenance.read_text(); self.assertNotIn(secret,retained+stdout.getvalue())
        data=json.loads(retained); self.assertEqual(data['status'],'Failed'); self.assertEqual(data['commands'][0]['channels'],'Withheld: sensitive content')
        self.assertNotIn('stdout_base64',data['commands'][0]); self.assertNotIn('stderr_base64',data['commands'][0])

    def test_outside_import_origin_rejection_retains_observation(self):
        import subprocess
        def runner(command,**kwargs):
            return subprocess.CompletedProcess(command,0,b'/outside/textstats.py\n',b'origin diagnostic\n')
        provenance={}
        with self.assertRaises(ValueError): capture.capture(self.root,'baseline',runner=runner,provenance=provenance)
        self.assertEqual(provenance['status'],'Failed'); self.assertFalse(provenance['commands'][0]['origin_accepted'])
        self.assertEqual(provenance['commands'][0]['stdout'],'/outside/textstats.py\n'); self.assertEqual(provenance['commands'][0]['stderr'],'origin diagnostic\n')
