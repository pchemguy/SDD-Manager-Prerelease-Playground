from pathlib import Path
import tempfile,shutil,subprocess,os,re,json,time
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
records=[]
with tempfile.TemporaryDirectory() as d:
 dest=Path(d)/'checkout';shutil.copytree(Path.cwd(),dest,ignore=shutil.ignore_patterns('.git','dist','__pycache__','*.tkn','textstats-run-resources','.github'))
 for name in ['README.md','docs/public-api.md']:
  for index,(lang,code) in enumerate(re.findall(r'```(bash|python)\n(.*?)```',Path(name).read_text(),re.S),1):
   command=['bash','-c',code] if lang=='bash' else ['python','-B','-c',code]
   r=subprocess.run(command,cwd=dest,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
   expected=1 if 'bad-range.txt' in code else 0
   records.append(dict(document=name,fence=index,command=command,expected_final_status=expected,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,time=time.time()))
   Path(str(base)+'.examples.json').write_text(json.dumps(records,indent=2)+'\n')
   assert r.returncode==expected,(name,index,r.returncode,r.stderr)
   print(name,index,lang,'status',r.returncode,flush=True)
print('Executed all',len(records),'runnable documented fences in isolated temporary checkout.')
