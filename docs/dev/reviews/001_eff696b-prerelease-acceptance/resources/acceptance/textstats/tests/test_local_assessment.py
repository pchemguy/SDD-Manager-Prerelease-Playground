"""Local contracts must not implicitly cross remote boundaries."""
import json
from unittest.mock import patch
from .support import Sandbox,git
from .test_catalog import catalog
core=catalog.core


class LocalAssessment(Sandbox):
    def test_local_head_and_ownership_do_not_read_remote(self):
        (self.repo/'TASKS.md').write_text('- [ ] T-ONE actual local task\n');git(self.repo,'add','TASKS.md');git(self.repo,'commit','-m','local task')
        contract=self.root/'contract.json';contract.write_text(json.dumps({'schema_version':1,'checks':[{'id':'head','kind':'git','field':'head','expected':git(self.repo,'rev-parse','HEAD').stdout.strip()},{'id':'owners','kind':'task_ownership'}]}))
        with patch.object(core,'remote_read',side_effect=AssertionError('implicit remote read')):
            result,code=core.assessment(self.inputs,self.state,contract,None)
        self.assertEqual(code,0);self.assertEqual(result['status'],'Checks passed')

    def test_publication_contract_explicitly_reads_required_remote(self):
        contract=self.root/'contract.json';contract.write_text(json.dumps({'schema_version':1,'checks':[{'id':'published','kind':'git','field':'publication','expected':'published'}]}))
        with patch.object(core,'remote_read',wraps=core.remote_read) as read:
            result,code=core.assessment(self.inputs,self.state,contract,None)
        self.assertTrue(read.called);self.assertEqual(code,0)

    def test_selected_core_criteria_exclude_native_extension(self):
        (self.repo/'TASKS.md').write_text('- [ ] T-ONE actual local task\n')
        contract=__import__('pathlib').Path(__file__).parents[1]/'cases/assessor/A-024.json';state=dict(self.state,variant='denial');state['checkpoint_refs']={'product_commit':git(self.repo,'rev-parse','HEAD').stdout.strip()}
        result,code=core.assessment(self.inputs,state,contract,None)
        self.assertEqual(code,0);self.assertFalse(any('native handoff' in x for x in result['required_agent_checks']))

    def test_refusal_variant_does_not_require_cross_phase_execution(self):
        (self.repo/'TASKS.md').write_text('- [ ] T-ONE actual local task\n')
        contract=__import__('pathlib').Path(__file__).parents[1]/'cases/assessor/A-014.json'
        state=dict(self.state,variant='prerequisite-refusal');state['checkpoint_refs']={'product_commit':git(self.repo,'rev-parse','HEAD').stdout.strip()}
        result,code=core.assessment(self.inputs,state,contract,None)
        self.assertEqual(code,0)
        self.assertFalse(any('earlier phase completes' in x for x in result['required_agent_checks']))
        self.assertTrue(any('refus' in x.lower() for x in result['required_agent_checks']))

    def test_legacy_checkpoint_discloses_missing_variant_criteria_selection(self):
        (self.repo/'TASKS.md').write_text('- [ ] T-ONE actual local task\n')
        contract=__import__('pathlib').Path(__file__).parents[1]/'cases/assessor/A-024.json'
        state=dict(self.state);state['checkpoint_refs']={'product_commit':git(self.repo,'rev-parse','HEAD').stdout.strip()}
        result,code=core.assessment(self.inputs,state,contract,None)
        self.assertEqual(code,0)
        self.assertTrue(result.get('variant_selection_required'))
        self.assertIn('native-recovery',result.get('available_variant_agent_checks',{}))
        self.assertFalse(result['agent_behavior_assessed'])
