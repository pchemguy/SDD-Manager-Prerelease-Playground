"""Exercise synthetic staging, merge, push, ignore and zero-test failure primitives. This does not authenticate clients or enforce agent instructions."""

from pathlib import Path
import subprocess,tempfile,os,json
root=Path(tempfile.mkdtemp(prefix='sdd008-')); repo=root/'repo';repo.mkdir();remote=root/'remote.git'; results=[]
def run(args,cwd=repo,env=None,ok=True):
 p=subprocess.run(args,cwd=cwd,env=env,text=True,capture_output=True)
 if ok: assert p.returncode==0,(args,p.stdout,p.stderr)
 return p
def git(*args,**kw):return run(['git',*args],**kw).stdout.strip()
def write(name,data): (repo/name).write_text(data)
def commit(msg):git('add','.');git('commit','-qm',msg);return git('rev-parse','HEAD')
git('init','-qb','main');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid');run(['git','init','--bare','-q',str(remote)]);git('remote','add','origin',str(remote));write('owned.txt','base\n');write('unrelated.txt','base\n');base=commit('base');git('push','-u','origin','main')
# Temporary index leaves unrelated staged content out of owned commit.
write('unrelated.txt','unrelated staged\n');git('add','unrelated.txt');unrelated=git('ls-files','-s','unrelated.txt');write('owned.txt','owned changed\n');env=os.environ.copy();env['GIT_INDEX_FILE']=str(root/'temporary-index');git('read-tree','HEAD',env=env);git('add','owned.txt',env=env);git('commit','-qm','owned only',env=env);assert git('show','--format=','--name-only','HEAD')=='owned.txt';git('reset','-q','HEAD','--','owned.txt');assert git('ls-files','-s','unrelated.txt')==unrelated;assert git('diff','--cached','--name-only')=='unrelated.txt';git('commit','-qm','persist unrelated fixture');git('push','origin','main');results.append('temporary-index commit excludes unrelated staging and owned-entry reconciliation preserves it')
# Conflicting merge stays uncommitted; no target publication after failed check.
git('switch','-c','revision/001_'+base[:7]+'-change');write('owned.txt','revision\n');working=commit('revision');git('push','-u','origin',git('branch','--show-current'));git('switch','main');write('owned.txt','target\n');commit('target');git('push','origin','main');target=git('rev-parse','HEAD');p=run(['git','merge','--no-ff','--no-commit',working],ok=False);assert p.returncode!=0;assert git('rev-parse','HEAD')==target and git('ls-files','-u');assert git('ls-remote','origin','refs/heads/main').split()[0]==target
failed=run(['python','-c','raise SystemExit(1)'],ok=False);assert failed.returncode==1;assert git('rev-parse','HEAD')==target;write('owned.txt','combined accepted\n');git('add','owned.txt');git('commit','-qm','verified synthetic merge');merge=git('rev-parse','HEAD');assert len(git('show','-s','--format=%P','HEAD').split())==2;results.append('conflict and failed check preserve merge state/target; scoped resolution creates two-parent merge')
# Remote advanced independently; rejected publication preserves local merge.
other=root/'other';run(['git','clone','-q','-b','main',str(remote),str(other)],cwd=root);git('config','user.name','Other',cwd=other);git('config','user.email','other@example.invalid',cwd=other);(other/'remote.txt').write_text('remote advance\n');git('add','remote.txt',cwd=other);git('commit','-qm','advance',cwd=other);git('push','origin','main',cwd=other);remote_tip=git('ls-remote','origin','refs/heads/main').split()[0];p=run(['git','push','origin','main'],ok=False);assert p.returncode!=0;assert git('rev-parse','HEAD')==merge and git('ls-remote','origin','refs/heads/main').split()[0]==remote_tip;results.append('non-fast-forward push rejection retains verified local merge and remote history')
# Synthetic token only, ignored/untracked versus tracked are distinct.
write('.gitignore','*.tkn\n!gh.tkn\n');write('gh.tkn','SYNTHETIC-NOT-A-CREDENTIAL\n');assert run(['git','check-ignore','-q','gh.tkn'],ok=False).returncode==1;write('.gitignore','*.tkn\n!gh.tkn\n*.tkn\n');assert run(['git','check-ignore','-q','gh.tkn'],ok=False).returncode==0;git('add','-f','gh.tkn');assert git('ls-files','gh.tkn')=='gh.tkn';results.append('negating ignore rule detected; effective ignore does not untrack an already staged synthetic credential')
# Zero selected tests can still exit successfully; coverage needs counts.
p=run(['python','-m','unittest','discover','-s',str(root)],cwd=root,ok=False);assert p.returncode!=0 and 'Ran 0 tests' in p.stderr;results.append('current unittest discovery rejects zero tests; actual counts and status expose absent evidence')
output=dict(directory=str(root),passed=results,limits='Controlled Git/file/runner primitives and explicit caller decisions; no installed agent enforcement, credential authentication, product tests, hosted APIs or automatic recovery exercised.')
Path('/tmp/sdd008-failure-results.json').write_text(json.dumps(output,indent=2));print(json.dumps(output,indent=2))
