from pathlib import Path
import subprocess,re,hashlib
base='795f3a3542c9981f8d43c8e182876f3efa5b5f16'
changed=subprocess.check_output(['git','diff','--name-only',base],text=True).splitlines();assert changed==['docs/dev/TASKS-REVIEW-REPORT.md','docs/dev/TASKS.md']
s=Path('docs/dev/TASKS.md').read_text();old=subprocess.check_output(['git','show',base+':docs/dev/TASKS.md'],text=True)
entries=re.findall(r'^        - \[([x ])\] (T-\d{3})',s,re.M);assert len(entries)==24 and len(set(x[1] for x in entries))==24 and sum(x[0]=='x' for x in entries)==19
assert entries==re.findall(r'^        - \[([x ])\] (T-\d{3})',old,re.M)
assert s[s.index('## Completion and persistence rules'):]==old[old.index('## Completion and persistence rules'):]
assert re.findall(r'^- \[.*|^    - \[.*',s,re.M)==re.findall(r'^- \[.*|^    - \[.*',old,re.M)
for p in changed:
    t=Path(p).read_text();prior=subprocess.check_output(['git','show',base+':'+p],text=True)
    def issues(text):
        lines=text.splitlines();return [line for i,line in enumerate(lines) if line.startswith('#') and i+1<len(lines) and lines[i+1]!='']
    assert issues(t)==issues(prior),'new heading issue'
    for link in re.findall(r'\]\(([^)]+)\)',t):
        if not ':' in link and not link.startswith('#'): assert (Path(p).parent/link.split('#')[0]).exists(),(p,link)
    print(p,'sha256='+hashlib.sha256(Path(p).read_bytes()).hexdigest(),'blob='+subprocess.check_output(['git','hash-object',p],text=True).strip())
print('PASS: 24 unique owners, 19 checked/5 pending; all checkbox states/parentage/history preserved; only selected docs changed; no new heading issues, links pass')
print('CORRECTION: prior broad heading check failed on unchanged historical TASKS heading at line 387; bounded changed-document comparison preserves that history and adds no defect')
print('specimen-results sha256='+hashlib.sha256(Path('/workspace/scratch/46b31bb4dff6/037-a022-specimen-results.json').read_bytes()).hexdigest())