"""Actual partial Git/file operations and recovery controls, not agent acceptance."""
import importlib.util
from pathlib import Path
import sys
from .support import Sandbox, git


class TrialControls(Sandbox):
    def module(self):
        p=Path(__file__).parents[1]/'scripts/trial_control.py'
        spec=importlib.util.spec_from_file_location('trial_control',p)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

    def test_partial_action_is_held_then_resumed_once(self):
        m=self.module();gate=self.root/'gate.json'
        actions=[[sys.executable,'-c','from pathlib import Path; Path("one.md").write_text("transferred")'],[sys.executable,'-c','from pathlib import Path; Path("two.md").write_text("transferred")']]
        first=m.execute(self.repo,actions,['one.md','two.md'],gate,hold_after=1)
        self.assertEqual(first['status'],'Held');self.assertTrue((self.repo/'one.md').exists());self.assertFalse((self.repo/'two.md').exists())
        m.execute(self.repo,actions,['one.md','two.md'],gate,resume=True)
        self.assertTrue((self.repo/'two.md').exists())
        with self.assertRaises(ValueError):m.execute(self.repo,actions,['one.md','two.md'],gate,resume=True)

    def test_missing_change_and_completed_transfer_cannot_be_triggers(self):
        m=self.module()
        with self.assertRaises(ValueError):m.execute(self.repo,[[sys.executable,'-c','pass'],[sys.executable,'-c','pass']],['one.md'],self.root/'gate.json',hold_after=1)
        with self.assertRaises(ValueError):m.execute(self.repo,[[sys.executable,'-c','pass']],['one.md'],self.root/'second.json',hold_after=1)

    def test_resume_rejects_drift_and_different_commands(self):
        m=self.module();gate=self.root/'gate.json';actions=[[sys.executable,'-c','from pathlib import Path; Path("one.md").write_text("pending")'],[sys.executable,'-c','pass']]
        m.execute(self.repo,actions,['one.md'],gate,hold_after=1);(self.repo/'one.md').write_text('changed outside hold')
        with self.assertRaises(ValueError):m.execute(self.repo,actions,['one.md'],gate,resume=True)

    def test_incomplete_phase_and_outside_prerequisite_are_not_eligible(self):
        m=self.module();task=self.repo/'TASKS.md';task.write_text('- [x] T-001 first\n- [ ] T-002 second\n');git(self.repo,'add','TASKS.md');git(self.repo,'commit','-m','actual incomplete tasks')
        with self.assertRaisesRegex(ValueError,'incomplete'):m.eligibility(self.repo,'TASKS.md',['T-001','T-002'])
        with self.assertRaisesRegex(ValueError,'missing'):m.eligibility(self.repo,'TASKS.md',['T-MISSING'])
        task.write_text('- [x] T-001 first\n- [x] T-002 second\n');git(self.repo,'add','TASKS.md');git(self.repo,'commit','-m','complete actual tasks')
        self.assertEqual(m.eligibility(self.repo,'TASKS.md',['T-001','T-002'])['status'],'Eligible')

    def test_optional_facilities_are_not_run_and_required_are_blocked(self):
        m=self.module()
        self.assertEqual(m.facilities({'requirement':'optional','facilities':['native']},set())['status'],'Not run')
        self.assertEqual(m.facilities({'requirement':'required','facilities':['native']},set())['status'],'Blocked')

    def test_receipt_symlinks_rejected_before_fresh_or_resume_operations(self):
        m=self.module();actions=[[sys.executable,'-c','pass']]
        for occupied in (False,True):
            for resume in (False,True):
                with self.subTest(occupied=occupied,resume=resume):
                    target=self.root/f'target-{occupied}-{resume}.json'
                    if occupied:target.write_text('preserve this evidence')
                    receipt=self.root/f'link-{occupied}-{resume}.json';receipt.symlink_to(target)
                    with self.assertRaisesRegex(ValueError,'symlink'):
                        m.execute(self.repo,actions,['pending.md'],receipt,resume=resume)
                    self.assertTrue(receipt.is_symlink())
                    if occupied:self.assertEqual(target.read_text(),'preserve this evidence')
                    else:self.assertFalse(target.exists())

    def test_symlinked_receipt_parent_rejected_without_creation(self):
        m=self.module();target=self.root/'real-directory';target.mkdir()
        linked=self.root/'linked-directory';linked.symlink_to(target,target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'symlink'):
            m.execute(self.repo,[[sys.executable,'-c','pass']],['pending.md'],linked/'gate.json')
        self.assertEqual(list(target.iterdir()),[])

    def test_pending_selected_transfer_cannot_already_be_completed(self):
        m=self.module();actions=[[sys.executable,'-c','from pathlib import Path; Path("one.md").write_text("done"); Path("two.md").write_text("done")'],[sys.executable,'-c','pass']]
        with self.assertRaisesRegex(ValueError,'pending transfer'):
            m.execute(self.repo,actions,['one.md','two.md'],self.root/'gate.json',hold_after=1,pending_paths=['two.md'])

    def test_timeout_retains_safe_partial_channels_without_replay(self):
        import json
        import subprocess
        from unittest.mock import patch
        m=self.module();gate=self.root/'timeout.json';actions=[[sys.executable,'-c','pass']]
        # Simulate the subprocess exception boundary; not a live process-kill claim.
        failure=subprocess.TimeoutExpired(actions[0],60,output=b'partial observation',stderr=b'partial diagnostic')
        original=m.subprocess.run
        def inject(argv,*args,**kwargs):
            if argv==actions[0]:raise failure
            return original(argv,*args,**kwargs)
        with patch.object(m.subprocess,'run',side_effect=inject):
            with self.assertRaisesRegex(ValueError,'reconcile'):
                m.execute(self.repo,actions,['pending.md'],gate)
        record=json.loads(gate.read_text())
        self.assertEqual(record['status'],'Uncertain')
        self.assertEqual(record['commands'][0]['stdout'],'partial observation')
        self.assertEqual(record['commands'][0]['stderr'],'partial diagnostic')
        self.assertEqual(record['completed'],0)
        with self.assertRaises(ValueError):m.execute(self.repo,actions,['pending.md'],gate,resume=True)
