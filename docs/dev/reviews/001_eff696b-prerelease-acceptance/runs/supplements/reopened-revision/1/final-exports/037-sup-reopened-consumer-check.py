import subprocess,pathlib,hashlib,json,re,os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
b='cedb509eb224ff4798349a924dd2e5d9235f18f7'
prefix='docs/dev/reviews/042_5e4d990-task-publication-continuation-review/'
owned={prefix+'README.md',prefix+'REVIEW-REPORT.md'}
def git(*args):return subprocess.check_output(['git','--no-optional-locks',*args],text=True)
changed=set(git('diff',b,'--name-only').splitlines());assert changed==owned,(changed,owned)
files=git('ls-tree','-r','--name-only',b).splitlines(); hashes={}
for name in files:
 p=pathlib.Path(name);old=subprocess.check_output(['git','show',b+':'+name]);new=p.read_bytes()
 if name in owned:assert new.startswith(old),name
 else:assert new==old,name
 if name in owned:
  lines=new.decode().splitlines()
  for i,line in enumerate(lines):
   if line.startswith('#'):assert i+1<len(lines) and not lines[i+1].strip(),(name,i)
  for target in re.findall(r'\]\(([^)]+)\)',new[len(old):].decode()):
   target=target.split('#')[0]
   if target:assert (p.parent/target).exists(),target
  hashes[name]={'sha256':hashlib.sha256(new).hexdigest(),'blob':git('hash-object',name).strip()}
assert not git('ls-files','-u')
git('diff','--check')
print(json.dumps({'status':'Passed','scope':sorted(changed),'checks':['all baseline tracked files outside two selected package artifacts byte-identical','both historical artifact byte prefixes retained','selected artifact heading separation','added local link file targets exist','no unmerged index entries','git diff --check'],'tracked_file_count':len(files),'artifact_hashes':hashes},indent=2))
