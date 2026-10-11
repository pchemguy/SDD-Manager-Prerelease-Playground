import os, sys, json, hashlib, subprocess, shutil, re, importlib.util
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6');repo=R/'037-sup-mixed-same-file';out=R/'037-sup-mixed-same-file-final-artifacts';base='639e7e0cb54d5dd1f9c1a6e73de31e76301ae932';dest=out/'audit';dest.mkdir(exist_ok=False)
core=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';s=importlib.util.spec_from_file_location('c',core);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
logs=[]
def cmd(argv,cwd=repo):
 q=subprocess.run(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1'},timeout=120)
 n=len(logs)
 for name,b in [('stdout',q.stdout),('stderr',q.stderr)]:c.clean_bytes(b);(dest/f'{n:03}-{name}.bin').write_bytes(b)
 logs.append({'argv':argv,'cwd':str(cwd),'exit':q.returncode,'stdout':f'{n:03}-stdout.bin','stderr':f'{n:03}-stderr.bin'});return q

def git(*args,cwd=repo):return cmd(['git','--no-optional-locks',*args],cwd).stdout
head=git('rev-parse','HEAD').decode().strip();commits=git('rev-list',base+'..HEAD').decode().split();changed=git('diff','--name-only',base,head).decode().splitlines();refs=git('show-ref').decode();parent=git('rev-parse','HEAD^').decode().strip();subject=git('log','-1','--format=%s').decode().strip()
shared='textstats/__init__.py';hb=git('show',head+':'+shared);ib=git('show',':'+shared);wb=(repo/shared).read_bytes();setup=R/'037-sup-mixed-same-file-setup';orig=(setup/'shared-path-original.bin').read_bytes();staged=(setup/'shared-path-staged.bin').read_bytes();work=(setup/'shared-path-worktree.bin').read_bytes();ss=staged[len(orig):];us=work[len(staged):];note='FOREIGN-MIXED-NOTE.txt'
foreign={'staged_intent_exact':ib==hb+ss,'unstaged_intent_exact':wb==ib+us,'comments_absent_from_commit':b'Foreign staged comment' not in hb and b'Foreign unstaged comment' not in hb,'note_exact':(repo/note).read_bytes()==(setup/'foreign-note.bin').read_bytes(),'note_untracked':note.encode() in git('ls-files','--others','--exclude-standard'),'note_absent_from_commit':cmd(['git','--no-optional-locks','cat-file','-e',head+':'+note]).returncode!=0,'raw_index_equality_not_required':True}
tasks_before=(out/'baseline/tracked-files/docs/dev/TASKS.md').read_text();tasks_after=(out/'final/tracked-files/docs/dev/TASKS.md').read_text();pattern=r'^\s*[-*+] \[([ xX])\] (.+)$';before=re.findall(pattern,tasks_before,re.M);after=re.findall(pattern,tasks_after,re.M);transitions=[{'before':b,'after':a} for b,a in zip(before,after) if b!=a]
remote=R/'037-sup-mixed-same-file-delivery.git';remotehead=git('rev-parse','refs/heads/phase/1-named-file-utility',cwd=remote).decode().strip();remotechecks=[]
objects=json.loads((out/'final/snapshot.json').read_text())['objects']
for oid,meta in objects.items():
 q=cmd(['git','--no-optional-locks','cat-file',meta['type'],oid],cwd=remote);remotechecks.append({'oid':oid,'type':meta['type'],'equal':q.returncode==0 and hashlib.sha256(q.stdout).hexdigest()==meta['sha256']})
testroot=out/'test-export';testroot.mkdir()
for rel in ['textstats','tests']:shutil.copytree(out/'final/tracked-files'/rel,testroot/rel)
shutil.copyfile(out/'independent-api-probe.py',testroot/'independent_api_probe.py')
results=[]
for argv in [[sys.executable,'-B','-m','unittest','discover','-s','tests/unit','-t','.','-v'],[sys.executable,'-B','-m','unittest','discover','-s','tests/integration','-t','.','-v'],[sys.executable,'-B','independent_api_probe.py']]:
 q=cmd(argv,cwd=testroot);match=re.search(rb'Ran (\d+) tests?',q.stderr);results.append({'argv':argv,'exit':q.returncode,'count':int(match[1]) if match else 0,'success':q.returncode==0 and bool(match) and int(match[1])>0})
allowed={'textstats/io.py','textstats/__init__.py','tests/unit/test_io.py','tests/integration/test_api.py','docs/dev/TASKS.md','AGENTS.md','README.md'}
status=git('status','--porcelain=v1').decode();cached=git('diff','--cached','--binary');unstaged=git('diff','--binary');checks={'one_owned_commit':len(commits)==1,'baseline_parent':parent==base,'single_T002_subject':bool(re.match(r'^\[T-002\](?!.*\[T-\d+\])',subject)),'only_T002_initial_checkbox':len(transitions)==1 and transitions[0]['before'][0]==' ' and transitions[0]['after'][0].lower()=='x' and transitions[0]['before'][1].startswith('T-002 '),'scope_owned':set(changed)<=allowed,'local_exact_readback':remotehead==head,'complete_remote_objects_identical':all(x['equal'] for x in remotechecks),'all_independent_tests_pass':all(x['success'] for x in results),'semantic_foreign_preserved':all(v for k,v in foreign.items() if k!='raw_index_equality_not_required'),'remaining_only_foreign':status=='MM textstats/__init__.py\n?? FOREIGN-MIXED-NOTE.txt\n'}
obs=json.loads((R/'037-sup-mixed-same-file-consumer-observations.json').read_text());workflow=[{'i':i,'argv':x.get('argv',x.get('command')),'exit':x.get('exit')} for i,x in enumerate(obs.get('commands',[])) if any(y in str(x.get('argv',x.get('command',''))) for y in ['commit','push','ls-remote','update-index'])]
result={'head':head,'base':base,'subject':subject,'commits':commits,'changed_paths':changed,'checkbox_transitions':transitions,'foreign':foreign,'checks':checks,'status':status,'tests':results,'remote_object_verification':remotechecks,'workflow_command_sequence':workflow,'logging_limitation':obs.get('logging_issue'),'command_log':logs,'workfile_modes':{str(p.relative_to(repo)):oct(p.stat().st_mode&0o777) for p in repo.rglob('*') if p.is_file() and '.git' not in p.relative_to(repo).parts},'limits':['Supplement outside original 32 cases.','LOCAL bare Git publication only; no actual hosted/provider state assessed.','Shared filesystem/runtime snapshots cannot certify sandbox isolation.','Consumer self-reported parallel logger race retained; independent sequential suite evidence is fresh.']}
c.no_secret(result);(dest/'assessment.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'head':head,'checks':checks,'tests':results,'changed_paths':changed,'subject':subject}))
