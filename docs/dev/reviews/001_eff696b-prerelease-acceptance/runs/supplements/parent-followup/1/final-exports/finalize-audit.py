import pathlib,json,subprocess,hashlib,base64,re
R=pathlib.Path('/workspace/scratch/46b31bb4dff6');P=R/'037-sup-parent-followup';E=R/'037-sup-parent-followup-final-artifacts'
def run(args):
 c=subprocess.run(args,cwd=P,capture_output=True);return {'argv':args,'cwd':str(P),'exit_code':c.returncode,'stdout_base64':base64.b64encode(c.stdout).decode(),'stderr_base64':base64.b64encode(c.stderr).decode()}
def out(args):return subprocess.check_output(['git','--no-optional-locks']+args,cwd=P)
start=json.loads((R/'037-sup-parent-followup-setup/START.json').read_bytes());o=json.loads((R/'037-sup-parent-followup-consumer-observations.json').read_bytes());seal=o['completion_seal'];h=out(['rev-parse','HEAD']).decode().strip();tree=out(['show',h+':docs/dev/TASKS.md']);old=(E/'baseline/workfiles/docs/dev/TASKS.md').read_bytes()
commands=[run(['git','--no-optional-locks']+a) for a in [['status','--porcelain=v1'],['for-each-ref','--format=%(objectname) %(refname)'],['show','--format=fuller',h],['cat-file','commit',h],['ls-remote','trial-delivery','refs/heads/trial/parent-followup'],['diff','--cached'],['diff','--stat',start['HEAD'],h]]]
(E/'final').mkdir(exist_ok=True)
(E/'final/raw-commands.json').write_text(json.dumps(commands,indent=2)+'\n')
for n in ['037-sup-parent-followup-consumer-observations.json','037-sup-parent-followup-consumer-observations-first-completed-seal.json','037-sup-parent-followup-proposed-TASKS.diff']:
 if (R/n).exists():(E/'final'/n).write_bytes((R/n).read_bytes())
(E/'objects'/f'{h}.commit').write_bytes(out(['cat-file','commit',h]));(E/'final/TASKS.md').write_bytes(tree)
checks={
 'retained_genuine_T009_ancestor':subprocess.run(['git','merge-base','--is-ancestor',start['genuine_completed_T009'],h],cwd=P).returncode==0,
 'single_new_commit':out(['rev-list',start['HEAD']+'..'+h]).decode().split()==[h],
 'exact_single_parent':out(['rev-list','--parents','-n','1',h]).decode().split()==[h,start['HEAD']],
 'single_T009_parent_subject':bool(re.match(rb'^\[T-009\] .*parent',out(['show','-s','--format=%s',h]))),
 'TASKS_only_committed':out(['diff-tree','--no-commit-id','--name-only','-r',h]).decode().splitlines()==['docs/dev/TASKS.md'],
 'exact_reviewed_artifact':tree==(E/'candidate-TASKS.md').read_bytes(),
 'all_initial_task_checkboxes_preserved':re.findall(rb'^.*\[[ x]\] T-\d+.*$',old,re.M)==re.findall(rb'^.*\[[ x]\] T-\d+.*$',tree,re.M),
 'all_nonTASKS_start_files_identical':all(hashlib.sha256((P/n).read_bytes()).hexdigest()==v['sha256'] for n,v in start['files'].items() if n!='docs/dev/TASKS.md'),
 'LOCAL_remote_exact':out(['ls-remote','trial-delivery','refs/heads/trial/parent-followup']).decode().split()[0]==h,
 'index_no_staged_changes':out(['diff','--cached'])==b'',
}
refs_before={line.split(' ',1)[1]:line.split(' ',1)[0] for line in base64.b64decode(start['refs_base64']).decode().splitlines()};refs_after={line.split(' ',1)[1]:line.split(' ',1)[0] for line in out(['for-each-ref','--format=%(objectname) %(refname)']).decode().splitlines()}
checks['only_trial_refs_advanced']=all(refs_after.get(k)==v for k,v in refs_before.items() if k not in ['refs/heads/trial/parent-followup','refs/remotes/trial-delivery/trial/parent-followup']) and set(refs_before)==set(refs_after)
files=[]
for n in ['-sample','bom.txt','sample.txt']:
 q=P/n
 if q.exists():
  b=q.read_bytes();(E/'final'/('untracked'+n.replace('-','_'))).write_bytes(b);files.append({'path':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mode':q.stat().st_mode,'mtime_ns':q.stat().st_mtime_ns,'ctime_ns':q.stat().st_ctime_ns})
assessment={'status':'Passed with documented artifact-provenance limitation','bounded_atomic_parent_closure':'Passed','agent_behavior_assessed':True,'default_catalog_grade':False,'outside_default_32':True,'checks':checks,'checkpoint_refs':{'starting':start['HEAD'],'genuine_T009':start['genuine_completed_T009'],'reached':h,'remote':'LOCAL trial-delivery','ref':'refs/heads/trial/parent-followup'},'first_attempt_failures':o.get('original_failures',[]),'untracked_artifacts':files,'limitations':['Three untracked example files appeared despite first post-check status claiming clean. Their names, bytes and mtimes match consumer original fence commands5/6. Consumer retracted unsupported foreign-creator characterization. Original cleanup loop/post-check clean status conflict with surviving files; survival or restoration chronology remains unresolved and no cause/other creator is attributed. They are preserved and never committed. Global filesystem-preservation certification is withheld.','LOCAL bare remote only, synthetic caller parent reassessment; no live hosted tracking/provider/target integration certification.','Shared filesystem broad access prevents isolation certification; no default case upgrade.'],'seal':seal,'postcompletion_evidence_clarification':o.get('postcompletion_evidence_clarification'),'assessor_product_writes':False}
assert all(checks.values()),checks
(E/'assessment.json').write_text(json.dumps(assessment,indent=2)+'\n')
manifest=[]
for q in sorted(E.rglob('*')):
 if q.is_file() and q.name!='safe-hash-manifest.json':
  b=q.read_bytes();manifest.append({'path':str(q.relative_to(E)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'clean_bytes':True,'no_secret':True})
(E/'safe-hash-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':assessment['status'],'checks':checks,'files':len(manifest)},indent=2))
