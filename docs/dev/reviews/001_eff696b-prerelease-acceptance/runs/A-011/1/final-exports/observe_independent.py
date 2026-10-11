import os,json,hashlib,subprocess,stat,datetime
from pathlib import Path
BASE=Path('/workspace/scratch/46b31bb4dff6'); PRODUCT=BASE/'037-textstats-product'; OUT=BASE/'037-a011-final-artifacts'; RUN=BASE/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-011/1'
commands=[]
def run(args,cwd=PRODUCT):
 p=subprocess.run(args,cwd=cwd,capture_output=True,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1'})
 commands.append({'argv':args,'cwd':str(cwd),'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()});return p.stdout.decode()
def snapshot(label):
 d={'schema_version':1,'case_id':'A-011','head':run(['git','--no-optional-locks','rev-parse','HEAD']).strip(),'branch':run(['git','--no-optional-locks','branch','--show-current']).strip(),'refs':run(['git','--no-optional-locks','show-ref']),'status':run(['git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all']),'index_entries':run(['git','--no-optional-locks','ls-files','--stage']),'index_sha256':hashlib.sha256((PRODUCT/'.git/index').read_bytes()).hexdigest(),'tracked_files':{}}
 for name in run(['git','--no-optional-locks','ls-files','-z']).split('\0'):
  if name:
   p=PRODUCT/name;d['tracked_files'][name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mode':oct(stat.S_IMODE(p.stat().st_mode))}
 (OUT/(label+'.json')).write_text(json.dumps(d,indent=2)+'\n')
 start=json.loads((RUN/'START.json').read_text());cmp={k:{'equal':d[k]==start[k]} for k in ['head','branch','refs','status','index_entries','index_sha256','tracked_files']};cmp['tracked_file_count']=len(d['tracked_files']);cmp['changed_tracked']=[n for n,v in d['tracked_files'].items() if start['tracked_files'].get(n)!=v]
 (OUT/(label+'-comparison.json')).write_text(json.dumps(cmp,indent=2)+'\n');return cmp
if __name__=='__main__':
 import sys
 print(json.dumps(snapshot(sys.argv[1])))
 run(['git','--no-optional-locks','log','-1','--format=%H%n%P%n%D'])
 (OUT/(sys.argv[1]+'-commands.json')).write_text(json.dumps(commands,indent=2)+'\n')
