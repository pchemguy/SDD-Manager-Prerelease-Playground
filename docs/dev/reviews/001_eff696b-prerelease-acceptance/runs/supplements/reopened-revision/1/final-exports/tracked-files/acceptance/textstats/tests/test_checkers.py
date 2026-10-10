"""Behavioral regressions for deterministic evidence and executable task ownership.

Exercises helper CLI results against literal contracts and disposable task lists;
passing these tests does not establish independent agent or live acceptance."""
import json
try:
    from .support import Sandbox, git
except ImportError:
    from support import Sandbox, git

class CheckerTests(Sandbox):
    def assess(self, checks, evidence=None):
        contract=self.root/'contract.json'
        contract.write_text(json.dumps({'schema_version':1,'checks':checks}))
        extra=['--contract',contract]
        if evidence is not None:
            path=self.root/'evidence.json'
            path.write_text(json.dumps(evidence))
            extra+=['--evidence',path]
        return self.invoke('assess',state=self.state,extra=extra)

    def test_literal_output_channel_and_status_sensitivity(self):
        expected={'returncode':0,'stdout':'lines=3 words=2\n','stderr':''}
        checks=[{'id':'cli','kind':'literal','key':'named-file','expected':expected}]
        evidence={'schema_version':1,'literals':{'named-file':expected}}
        data,_=self.ok(self.assess(checks,evidence))
        self.assertEqual(data['status'],'Checks passed')
        self.assertFalse(data['agent_behavior_assessed'])
        for field,value in [('stdout','wrong\n'),('stderr','warning\n'),('returncode',1)]:
            actual=dict(expected,**{field:value})
            p,data,_=self.assess(checks,{'schema_version':1,'literals':{'named-file':actual}})
            self.assertNotEqual(p.returncode,0)
            self.assertEqual(data['status'],'Checks failed')

    def test_empty_or_invalid_evidence_cannot_pass(self):
        for evidence in [{},{'schema_version':1,'literals':{}},{'schema_version':1,'literals':{'x':1},'agentPassed':True}]:
            p,_,_=self.assess([{'id':'x','kind':'literal','key':'x','expected':1}],evidence)
            self.assertNotEqual(p.returncode,0)
        p,_,_=self.assess([])
        self.assertNotEqual(p.returncode,0)

    def test_git_evidence_reads_actual_state(self):
        data,_=self.ok(self.assess([{'id':'clean','kind':'git','field':'staged_paths','expected':[]}]))
        (self.repo/'owned.txt').write_text('changed\n')
        git(self.repo,'add','owned.txt')
        p,data,_=self.assess([{'id':'clean','kind':'git','field':'staged_paths','expected':[]}])
        self.assertNotEqual(p.returncode,0)
        self.assertEqual(data['checks'][0]['status'],'Failed')

    def test_task_ownership_excludes_historical_evidence_and_rejects_duplicates(self):
        dev=self.repo/'docs/dev'
        dev.mkdir(parents=True)
        (dev/'TASKS.md').write_text('- [ ] T-1 implement\n')
        history=dev/'reviews/old'
        history.mkdir(parents=True)
        (history/'TASKS.md').write_text('- [ ] T-1 historical\n')
        self.ok(self.assess([{'id':'ownership','kind':'task_ownership'}]))
        (dev/'FEATURE-TASKS.md').write_text('- [ ] T-1 duplicate\n')
        p,data,_=self.assess([{'id':'ownership','kind':'task_ownership'}])
        self.assertNotEqual(p.returncode,0)
        self.assertEqual(data['status'],'Checks failed')

    def test_empty_task_collection_and_path_escape_fail(self):
        p,_,_=self.assess([{'id':'ownership','kind':'task_ownership'}])
        self.assertNotEqual(p.returncode,0)
        p,_,_=self.assess([{'id':'file','kind':'file','path':'../outside','exists':False}])
        self.assertNotEqual(p.returncode,0)

    def test_without_contract_is_not_run(self):
        data,_=self.ok(self.invoke('assess',state=self.state))
        self.assertEqual(data['status'],'Not run')
        self.assertFalse(data['agent_behavior_assessed'])

    def task_documents(self, documents):
        dev = self.repo / 'docs/dev'
        dev.mkdir(parents=True, exist_ok=True)
        for name, content in documents.items():
            path = dev / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

    def test_custom_ids_are_recognized_and_duplicates_fail(self):
        self.task_documents({'TASKS.md': '- [ ] F-001 feature\n- [ ] TASK_001 work\n- [ ] ABC42 other\n'})
        self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))
        self.task_documents({'TASKS.md': '- [ ] T-001 main\n- [ ] F-001 feature\n',
                             'FEATURE-TASKS.md': '- [ ] F-001 duplicate\n'})
        proc, data, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(data['checks'][0]['reason'], 'duplicate_task_ownership')

    def test_linked_reports_and_specs_are_not_task_owners(self):
        self.task_documents({'TASKS.md': '- [x] T-001 work\n[Report](report.md)\n[Spec](SPEC.md)\n',
                             'report.md': '- [x] T-001 historical evidence\n',
                             'SPEC.md': '| ID | Status |\n| --- | --- |\n| T-001 | Specified |\n'})
        self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))

    def test_backtick_and_tilde_examples_are_not_owners(self):
        for fence in ['```markdown', '~~~~markdown', '        ```markdown']:
            marker = fence.strip().split('markdown')[0]
            indent = fence[:len(fence) - len(fence.lstrip())]
            self.task_documents({'TASKS.md': '- [ ] T-001 actual\n' + fence + '\n- [ ] T-001 example\n' + indent + marker + '\n'})
            with self.subTest(fence=fence):
                self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))

    def test_fence_closers_require_matching_marker_length_and_plain_suffix(self):
        self.task_documents({'TASKS.md': '- [ ] T-001 actual\n````markdown\n'
                             '```\n~~~\n```` trailing text\n- [ ] T-001 example\n`````\n'
                             '- [ ] F-001 executable after close\n'})
        self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))
        self.task_documents({'FEATURE-TASKS.md': '- [ ] F-001 duplicate after fence\n'})
        proc, data, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(data['checks'][0]['reason'], 'duplicate_task_ownership')

    def test_ids_preserve_case_and_markdown_token_identity(self):
        self.task_documents({'TASKS.md': '- [ ] `TASK_001` main\n- [ ] **task_001** distinct\n'})
        self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))
        self.task_documents({'FEATURE-TASKS.md': '- [ ] **TASK_001** duplicate\n'})
        proc, data, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(data['checks'][0]['reason'], 'duplicate_task_ownership')

    def test_incomplete_fences_and_unsupported_tasks_fail_closed(self):
        for content in ['- [ ] T-001 actual\n```markdown\n- [ ] F-001 hidden\n',
                        '- [ ] T-001 actual\n- [ ] F- invalid identifier\n',
                        '- [ ] T-001 actual\n- [ ] prose without an ID\n']:
            self.task_documents({'TASKS.md': content})
            with self.subTest(content=content):
                proc, _, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
                self.assertNotEqual(proc.returncode, 0)

    def test_explicit_child_documents_are_additive_and_unique(self):
        self.task_documents({'TASKS.md': '- [ ] T-001 root\n[Child](tasks/slice.md)\n',
                             'tasks/slice.md': '- [ ] F-001 child\n'})
        check = {'id': 'owners', 'kind': 'task_ownership', 'documents': ['docs/dev/tasks/slice.md', 'docs/dev/TASKS.md']}
        self.ok(self.assess([check]))
        self.task_documents({'tasks/slice.md': '- [ ] T-001 duplicate root\n'})
        proc, data, _ = self.assess([check])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(data['checks'][0]['reason'], 'duplicate_task_ownership')

    def test_invalid_explicit_documents_cannot_pass(self):
        self.task_documents({'TASKS.md': '- [ ] T-001 root\n', 'reviews/old/slice.md': '- [ ] F-001 history\n'})
        invalid = [[], 'docs/dev/TASKS.md', [False], ['../outside.md'], ['/outside.md'],
                   ['gh.tkn'], ['docs/dev/missing.md'], ['docs/dev/reviews/old/slice.md'],
                   ['docs/dev/TASKS.md', 'docs/dev/TASKS.md'], ['docs//dev/TASKS.md'],
                   ['docs/./dev/TASKS.md'], ['docs\\dev\\TASKS.md']]
        for documents in invalid:
            with self.subTest(documents=documents):
                proc, _, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership', 'documents': documents}])
                self.assertNotEqual(proc.returncode, 0)
        (self.repo / 'docs/dev/linked').symlink_to(self.repo / 'docs/dev', target_is_directory=True)
        proc, _, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership', 'documents': ['docs/dev/linked/TASKS.md']}])
        self.assertNotEqual(proc.returncode, 0)

    def test_hierarchy_parents_and_custom_table_ids(self):
        self.task_documents({'TASKS.md': '## Phase 1 — Delivery\n\n- [ ] Phase 1 — Delivery\n'
                             '    - [ ] Milestone 1.1 — Capability\n        - [ ] ABC42 task\n',
                             'FEATURE-TASKS.md': '| Task ID | Status |\n| --- | --- |\n| TASK_001 | Pending |\n'})
        self.ok(self.assess([{'id': 'owners', 'kind': 'task_ownership'}]))
        self.task_documents({'FEATURE-TASKS.md': '| Task ID | Status |\n| --- | --- |\n| ABC42 | Pending |\n'})
        proc, data, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(data['checks'][0]['reason'], 'duplicate_task_ownership')

    def test_malformed_table_rows_do_not_hide_behind_valid_tasks(self):
        for table in ['| ID | Status |\n| --- | --- |\n| F- | Pending |\n',
                      '| ID | Status |\n| --- | --- |\n| F-001 | |\n',
                      '| ID | Status |\n| --- | --- |\n| F-001 | Pending | extra |\n',
                      '| IDs | Status |\n| --- | --- |\n| F-001 | Pending |\n',
                      '| ID | Status |\n| F-001 | Pending |\n']:
            self.task_documents({'TASKS.md': '- [ ] T-001 actual\n\n' + table})
            with self.subTest(table=table):
                proc, _, _ = self.assess([{'id': 'owners', 'kind': 'task_ownership'}])
                self.assertNotEqual(proc.returncode, 0)

    def test_boolean_is_not_integer_and_validated_runtime_ref_binding(self):
        p,data,_=self.assess([{'id':'type','kind':'literal','key':'x','expected':True}],{'schema_version':1,'literals':{'x':1}})
        self.assertNotEqual(p.returncode,0)
        self.state['checkpoint_refs']['product_commit']=git(self.repo,'rev-parse','HEAD').stdout.strip()
        self.ok(self.assess([{'id':'head','kind':'git','field':'head','expected_ref':'checkpoint_refs.product_commit'}]))
        p,_,_=self.assess([{'id':'bad','kind':'git','field':'head','expected_ref':'checkpoint_refs.missing'}])
        self.assertNotEqual(p.returncode,0)
        p,_,_=self.assess([{'id':'both','kind':'git','field':'head','expected_ref':'checkpoint_refs.product_commit','expected':'x'}])
        self.assertNotEqual(p.returncode,0)
