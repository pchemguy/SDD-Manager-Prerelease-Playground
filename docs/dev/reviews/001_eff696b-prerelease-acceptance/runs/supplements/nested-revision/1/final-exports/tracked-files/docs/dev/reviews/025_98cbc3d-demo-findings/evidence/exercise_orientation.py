from pathlib import Path
import subprocess, os, hashlib, re, json
B=Path('/workspace/scratch/revision025-fixtures')
results={}
env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
def run(p,*cmd):
    x=subprocess.run(cmd,cwd=p,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return {'command':' '.join(cmd),'exit':x.returncode,'output':x.stdout.strip()}
def put(p,name,text):
    q=p/name;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(text)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def init(name,manual=''):
    p=B/name;p.mkdir()
    put(p,'README.md','# Counter CLI\n\nCounts integer arguments and prints their sum.\n\nSource: [src/main.py](src/main.py). Tests: [tests/test_main.py](tests/test_main.py).\n\nRun from repository root with Python 3:\n\n```text\npython src/main.py 2 3\npython -m unittest discover -s tests\n```\n\n[Usage notice](SDD-MANAGER.md) and [AI disclosure](AI_DISCLOSURE.md).\n')
    put(p,'src/main.py','"""Sum integer CLI arguments."""\nimport sys\n\ndef count(values):\n    return sum(map(int, values))\n\nif __name__ == "__main__":\n    print(count(sys.argv[1:]))\n')
    put(p,'tests/test_main.py','"""Counter CLI contract checks."""\nimport unittest\nfrom src.main import count\n\nclass CounterTest(unittest.TestCase):\n    def test_sum(self):\n        self.assertEqual(count(["2", "3"]), 5)\n    def test_empty(self):\n        self.assertEqual(count([]), 0)\n')
    put(p,'SDD-MANAGER.md','# Usage notice\n\nSDD Manager is used to maintain project orientation.\n')
    put(p,'AI_DISCLOSURE.md','# AI disclosure\n\nAn AI assistant prepared the maintained orientation.\n')
    put(p,'.gitignore','__pycache__/\n')
    if manual:put(p,'AGENTS.md',manual)
    for cmd in [('git','init','-q'),('git','add','.'),('git','-c','user.name=Fixture Owner','-c','user.email=fixture@example.invalid','commit','-qm','Fixture baseline')]:
        z=run(p,*cmd);assert z['exit']==0,z
    return p
start='<!-- SDD maintained orientation: start -->'
end='<!-- SDD maintained orientation: end -->'
def maintained(p, tests='tests',owner=None,archive=None,interrupted=False):
    ownertext=('Active execution owner: ['+owner+']('+owner+').\n' if owner else 'No task execution owner is declared for this minimal CLI; no task list is fabricated.\n')
    if archive:ownertext+='Historical selected feature source: ['+archive+']('+archive+'); retained evidence only, with current executable entries in [docs/dev/TASKS.md](docs/dev/TASKS.md).\n'
    return f'''{start}
## Project orientation

[README.md](README.md) establishes this counter CLI's purpose. Source: [src/main.py](src/main.py). Tests: [{tests}/test_main.py]({tests}/test_main.py).

{ownertext}
[SDD-MANAGER.md](SDD-MANAGER.md) and [AI_DISCLOSURE.md](AI_DISCLOSURE.md) are project usage/disclosure records.

## Checks and working rules

From repository root using Python 3, run:

```text
python src/main.py 2 3
python -m unittest discover -s {tests}
```

These commands were exercised in this fixture: the CLI printed 5 and both unit tests passed. No installation or broader platform compatibility was verified.

Read applicable nested AGENTS.md before working on their paths. If the host does not discover root AGENTS.md, explicitly load this file. Preserve controlling manual instructions and unrelated changes. Keep edits within the authorized scope and stop at the requested boundary; commit/publication authority comes from the user and governing workflow. This disposable exercise stops at verified local files, with no publication.
{end}
'''
def update(p,body):
    q=p/'AGENTS.md';old=q.read_text() if q.exists() else ''
    if start in old:
        a=old.index(start);b=old.index(end,a)+len(end)
        new=old[:a]+body.rstrip()+old[b:]
    else:new=old+('\n' if old and not old.endswith('\n\n') else '')+body
    if new==old:return False
    q.write_text(new);return True

def check(p,tests='tests'):
    text=(p/'AGENTS.md').read_text()
    links=re.findall(r'\]\(([^)]+)\)',text)
    missing=[x for x in links if not (p/x).is_file()]
    checks=[run(p,'python','src/main.py','2','3'),run(p,'python','-m','unittest','discover','-s',tests)]
    assert not missing,missing
    assert all(x['exit']==0 for x in checks),checks
    return {'links':links,'missing_links':missing,'checks':checks,'git_status':run(p,'git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all')}

p=init('o1-minimal-adoption');update(p,maintained(p));results['O1']={'path':str(p),'AGENTS_sha256':digest(p/'AGENTS.md'),**check(p)}
p=init('o2-manual-maintenance','# Human instructions\n\nNever change data fixtures without explicit permission.\n\n'+maintained(None))
put(p,'tests/AGENTS.md','# Test instructions\n\nRun tests from repository root\n')
# Authorized preparation changes command location and execution-owner navigation.
(p/'tests').rename(p/'checks')
put(p,'docs/dev/FEATURE-TASKS.md','# Counter formatting feature\n\nThis is the active feature owner.\n\n- [ ] F1: define formatting acceptance.\n')
readme=(p/'README.md').read_text().replace('tests/','checks/').replace('-s tests','-s checks');put(p,'README.md',readme)
manual_before=(p/'AGENTS.md').read_text().split(start)[0];nested_before=(p/'checks/AGENTS.md').read_bytes()
update(p,maintained(p,tests='checks',owner='docs/dev/FEATURE-TASKS.md'))
assert (p/'AGENTS.md').read_text().startswith(manual_before)
assert (p/'checks/AGENTS.md').read_bytes()==nested_before
results['O2']={'path':str(p),'manual_rule_preserved':True,'nested_rule_preserved':True,'nested_rule_path':str(p/'checks/AGENTS.md'),**check(p,'checks')}
q=p/'AGENTS.md';before=q.read_bytes();statbefore=q.stat().st_mtime_ns
mutated=update(p,maintained(p,tests='checks',owner='docs/dev/FEATURE-TASKS.md'))
results['O3']={'path':str(q),'write_performed':mutated,'bytes_equal':before==q.read_bytes(),'mtime_equal':statbefore==q.stat().st_mtime_ns,'sha256_before':hashlib.sha256(before).hexdigest(),'sha256_after':digest(q)}
assert not mutated and before==q.read_bytes()
# Selected source transfer recorded under descriptive package; archived snapshot is non-executable.
p=init('o4-owner-transfer')
put(p,'docs/dev/FEATURE-TASKS.md','# Counter formatting feature tasks\n\nActive feature execution owner.\n\n- [ ] F1: define formatting acceptance.\n')
update(p,maintained(p,owner='docs/dev/FEATURE-TASKS.md'))
archive='docs/dev/features/counter-formatting/FEATURE-TASKS.md'
original=(p/'docs/dev/FEATURE-TASKS.md').read_bytes()
put(p,archive,original.decode())
put(p,'docs/dev/features/counter-formatting/README.md','# Counter formatting archive\n\nSelected source [FEATURE-TASKS.md](FEATURE-TASKS.md) is historical evidence only. Ownership transferred to [main TASKS](../../TASKS.md). Historical checkboxes are not executable owners.\n')
put(p,'docs/dev/TASKS.md','# Main tasks\n\nSole current executable owner after accepted counter-formatting transfer.\n\n- [ ] F1: define formatting acceptance.\n\n[Transfer record](features/counter-formatting/README.md).\n')
(p/'docs/dev/FEATURE-TASKS.md').unlink()
update(p,maintained(p,owner='docs/dev/TASKS.md',archive=archive))
assert '[ ]' not in (p/'AGENTS.md').read_text()
assert (p/archive).read_bytes()==original
results['O4']={'path':str(p),'current_owner':str(p/'docs/dev/TASKS.md'),'archived_source':str(p/archive),'transfer_record':str(p/'docs/dev/features/counter-formatting/README.md'),'archive_bytes_preserved':True,'AGENTS_executable_checklist_count':0,'active_FEATURE_TASKS_exists':False,**check(p)}
p=init('o5-interrupted-resume','# Human instructions\n\nNever change data fixtures without explicit permission.\n')
put(p,'user-notes.txt','User working notes baseline.\n')
z=run(p,'git','add','user-notes.txt');assert z['exit']==0
z=run(p,'git','-c','user.name=Fixture Owner','-c','user.email=fixture@example.invalid','commit','-qm','User baseline');assert z['exit']==0
put(p,'user-notes.txt','User unrelated pending edit: preserve exactly.\n')
put(p,'AGENTS.md',(p/'AGENTS.md').read_text()+'\n'+start+'\n## Project orientation\n\nInterrupted owned maintenance: src/main.py navigation still pending.\n'+end+'\n')
pre=run(p,'git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all');userbefore=(p/'user-notes.txt').read_bytes()
rootbefore=(p/'AGENTS.md').read_text().split(start)[0]
update(p,maintained(p))
assert (p/'user-notes.txt').read_bytes()==userbefore
assert (p/'AGENTS.md').read_text().startswith(rootbefore)
results['O5']={'path':str(p),'status_before_resume':pre,'user_sha256_before':hashlib.sha256(userbefore).hexdigest(),'user_sha256_after':digest(p/'user-notes.txt'),'manual_prefix_preserved':True,**check(p)}
(B/'orientation-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
