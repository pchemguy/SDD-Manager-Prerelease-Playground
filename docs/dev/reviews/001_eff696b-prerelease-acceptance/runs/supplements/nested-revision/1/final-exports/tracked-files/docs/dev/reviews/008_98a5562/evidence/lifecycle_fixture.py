"""Exercise synthetic workflow Git/file transitions with a local bare remote. Caller decisions are explicit; this does not test installed-agent enforcement."""

from pathlib import Path
import subprocess,tempfile,json,re
root=Path(tempfile.mkdtemp(prefix='sdd007-'));r=root/'repo';r.mkdir();remote=root/'remote.git'
def git(*args,ok=True):
 p=subprocess.run(['git',*args],cwd=r,text=True,capture_output=True)
 if ok:assert p.returncode==0,(args,p.stderr)
 return p.stdout.strip()
def write(name,text):
 p=r/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def commit(msg):git('add','.');git('commit','-qm',msg);return git('rev-parse','HEAD')
def push(branch):git('push','-u','origin',branch);assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==git('rev-parse',branch)
git('init','-q','-b','main');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid');subprocess.run(['git','init','--bare','-q',str(remote)],check=True);git('remote','add','origin',str(remote))
write('code.txt','foundation\n');base=commit('baseline');push('main')
for name in ['phase/2-archives','phase/3-polish','revision/001_'+base[:7]+'-trim','feature/002_'+base[:7]+'-zip']:
 git('check-ref-format','--branch',name)
git('switch','-c','phase/2-archives');write('code.txt','partial capability\n');commit('task subset');push('phase/2-archives');assert git('rev-parse','main')==base;assert not git('branch','--list','phase/3-*')
# Complete phase; integration is explicitly performed only at this boundary.
write('code.txt','phase 2 accepted capability\n');phase=commit('phase complete');push('phase/2-archives');git('switch','main');git('merge','--no-ff','--no-commit',phase);git('commit','-qm','phase 2 boundary');merged=git('rev-parse','HEAD');assert len(git('show','-s','--format=%P','HEAD').split())==2;push('main');git('switch','-c','phase/3-polish');assert git('rev-parse','HEAD')==merged
# Steering: minimal durable identity, merge to paused phase, not main.
id='001_'+merged[:7];branch='revision/'+id+'-trim';git('switch','-c',branch);write('docs/dev/reviews/'+id+'/REVISION-REPORT.md','# Amendment\n\nObjective: trim option. Target: phase/3-polish.\n');write('code.txt','retained capability\n');steer=commit('steering');push(branch);git('switch','phase/3-polish');git('merge','--no-ff','--no-commit',steer);git('commit','-qm','steering boundary');push('phase/3-polish');assert git('rev-parse','main')==merged
# Feature archive primitives, with active root files until complete incorporation.
featurebase=git('rev-parse','HEAD');fid='002_'+featurebase[:7];fb='feature/'+fid+'-zip';git('switch','-c',fb);archive='docs/dev/features/'+fid
write('docs/dev/FEATURE-SPEC.md','# ZIP delta\n\nZIP behavior.\n');write('docs/dev/FEATURE-TASKS.md','# Feature tasks\n\n- [ ] T-010 — ZIP\n');write(archive+'/README.md','# Package\n\n[Active spec](../../FEATURE-SPEC.md)\n\n[Active tasks](../../FEATURE-TASKS.md)\n');commit('feature preparation')
write('docs/dev/SPEC.md','# Specification\n\nZIP behavior incorporated.\n');commit('SPEC-only incorporation');assert (r/'docs/dev/FEATURE-SPEC.md').exists() and '[ ] T-010' in (r/'docs/dev/FEATURE-TASKS.md').read_text()
write('docs/dev/TASKS.md','# Tasks\n\n- [x] T-010 — ZIP\n');write('docs/dev/FEATURE-TASKS.md','# Feature tasks\n\n- [x] T-010 — ZIP\n');commit('complete task disposition')
git('mv','docs/dev/FEATURE-SPEC.md',archive+'/FEATURE-SPEC.md');assert (r/archive/'FEATURE-SPEC.md').exists() and (r/'docs/dev/FEATURE-TASKS.md').exists()
# Finish selected archive without reallocating package identity.
git('mv','docs/dev/FEATURE-TASKS.md',archive+'/FEATURE-TASKS.md');write(archive+'/FEATURE-TASKS.md','# Historical feature task snapshot\n\nNot executable; current owner: [TASKS](../../TASKS.md).\n\n- [x] T-010 — ZIP\n');write(archive+'/README.md','# Historical package\n\n[Spec snapshot](FEATURE-SPEC.md)\n\n[Task snapshot](FEATURE-TASKS.md)\n\n[Current spec](../../SPEC.md)\n\n[Current tasks](../../TASKS.md)\n')
for path in (r/archive).glob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):assert (path.parent/link).exists(),link
assert not (r/'docs/dev/FEATURE-TASKS.md').exists();assert '[x] T-010' in (r/'docs/dev/TASKS.md').read_text();assert 'Not executable' in (r/archive/'FEATURE-TASKS.md').read_text()
ftip=commit('incorporated archive');push(fb);git('switch','phase/3-polish');git('merge','--no-ff','--no-commit',ftip);git('commit','-qm','feature boundary');push('phase/3-polish');assert git('rev-parse','main')==merged
# Allocation combines actual collections; collisions retain identity with distinct slug.
identities=[p.name for coll in ['reviews','features'] for p in (r/'docs/dev'/coll).iterdir() if p.is_dir()];assert max(int(x.split('_')[0]) for x in identities)+1==3
assert git('branch','--list',fb);git('check-ref-format','--branch',fb+'-2')
result={'directory':str(root),'passed':['valid convention branch names and combined allocation','partial phase push leaves main unchanged and creates no next phase','two-parent complete phase integration and remote containment','next phase starts from published main tip','minimal steering record and merge to paused phase only','SPEC-only incorporation retains active unchecked task owner','interrupted archive paths inspected then finished under same identity','archive link repair and historical snapshot with main task owner','feature integrates to active phase without completing main phase','local bare remote with no hosting backend and distinct collision slug'],'limits':'Executed Git/file primitives and explicitly selected fixture workflow; no installed-agent enforcement, concurrent allocator race, real exit-test failure, or live hosting API tested.'}
Path('/tmp/sdd008-lifecycle-results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
