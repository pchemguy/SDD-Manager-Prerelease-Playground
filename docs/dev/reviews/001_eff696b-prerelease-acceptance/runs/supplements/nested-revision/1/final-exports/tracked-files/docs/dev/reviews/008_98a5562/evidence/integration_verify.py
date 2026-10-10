"""Verify scoped source revision evidence and preserved pinned package."""
from pathlib import Path
import argparse,subprocess,json,hashlib,re
parser=argparse.ArgumentParser();parser.add_argument('repo',type=Path);parser.add_argument('output',type=Path);args=parser.parse_args();r=args.repo
base='98a083b555a211e45f8a16bfd3ea83829b9aa25e';prov=json.loads(Path('/workspace/scratch/AgentPlayground-sdd-008/vendor/PROVENANCE.json').read_text())
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
for path,h in prov['hashes'].items():assert hashlib.sha256((r/path).read_bytes()).hexdigest()==h,path
notices=[]
for name in ['EXPLORE_DRIVE_V1.md','EXPLORE_DRIVE_V2.md']:
 text=(r/name).read_text();old=subprocess.check_output(['git','show',base+':'+name],cwd=r,text=True);line=next(x for x in text.splitlines() if x.startswith('> **Historical exploration transcript.**'));assert text.replace(line+'\n\n','',1)==old;assert text.index(line)<text.index('## ');assert '[README.md](README.md)' in line and '(docs/dev/CAPABILITY-MAP.md)' in line;notices.append(name)
changed=git('diff','--name-only',base).splitlines();allowed=lambda p:p in {'README.md','EXPLORE_DRIVE_V1.md','EXPLORE_DRIVE_V2.md','docs/dev/reviews/README.md'} or p.startswith('docs/dev/reviews/008_98a5562/');assert all(allowed(p) for p in changed),changed
links=[]
for name in changed:
 p=r/name
 if p.suffix!='.md':continue
 text=p.read_text()
 if name.startswith('EXPLORE_'):text=next(x for x in text.splitlines() if x.startswith('> **Historical exploration transcript.**'))
 for label,target in re.findall(r'\[([^]\n]+)\]\(([^)]+)\)',text):
  local=target.split('#',1)[0]
  if not local or ':' in local or local.startswith('/'):continue
  assert (p.parent/local).resolve().exists(),(name,target);links.append([name,target])
cmd=['python','/root/.codex/skills/remote-skills/skill-6ab91e941cbc8191a00ce5e8e34d83fd/scripts/validate_plugin.py',str(r)];v=subprocess.run(cmd,capture_output=True,text=True);assert v.returncode==0,v.stdout+v.stderr
subprocess.run(['git','diff','--check'],cwd=r,check=True)
result={'head':git('rev-parse','HEAD'),'branch':git('branch','--show-current'),'pinned_source':'529e98d4d3cd7002e3a49e34394552a44bf0a8d0','pinned_files_identical':len(prov['hashes']),'historical_notice_only_preservation':notices,'changed_paths':changed,'local_links_checked':len(links),'links':links,'package_validator':{'argv':cmd,'returncode':v.returncode,'stdout':v.stdout,'stderr':v.stderr},'diff_check_passed':True,'limits':'Source metadata/docs verification, not installed-client execution.'};args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','package_validator']},indent=2));print(v.stdout)
