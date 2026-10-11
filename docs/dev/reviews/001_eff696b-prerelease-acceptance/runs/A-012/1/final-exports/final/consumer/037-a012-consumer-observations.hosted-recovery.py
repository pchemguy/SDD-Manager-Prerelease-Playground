from pathlib import Path
import json,importlib.util,re,shutil
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
p=Path(str(base)+'.hosted.py');q=Path(str(base)+'.hosted.original.py');assert not q.exists();shutil.copyfile(p,q)
s=p.read_text().replace('urllib.request.urlopen(req)','urllib.request.urlopen(req,timeout=30)')
s=s.replace(' result=json.loads(raw)', ''' except urllib.error.URLError as e:
  with log.open('a') as f:f.write(json.dumps(dict(method=method,endpoint=path,payload=payload,status=None,transport_error=str(e),time=time.time()))+'\\n')
  raise
 result=json.loads(raw)''')
p.write_text(s)
spec=importlib.util.spec_from_file_location('host',p);host=importlib.util.module_from_spec(spec);spec.loader.exec_module(host)
ops=json.loads(Path(str(base)+'.hosted-plan.corrected.json').read_text());op=next(o for o in ops if o['endpoint']=='issues/15')
current=host.api('issues/15');old=next(i for i in json.loads(Path(str(base)+'.hosted-before.json').read_text())['issues'] if i['number']==15)
for f,v in op['payload'].items():assert current[f]==v,('issue15 uncertain mismatch',f)
for f in ['state','state_reason','labels','milestone','assignees','comments']:assert current[f]==old[f],f
marker='sdd-forge:task-id='+op['task'];pattern=r'## Task brief <!-- '+re.escape(marker)+r' -->.*?<!-- /'+re.escape(marker)+r' -->'
assert re.sub(pattern,'',current['body'],flags=re.S)==re.sub(pattern,'',old['body'],flags=re.S)
rows=json.loads(Path(str(base)+'.hosted-results.json').read_text());assert len(rows)==4
rows.append(dict(endpoint='issues/15',status='GET-only recovery independently verified successful prior PATCH; no replay',id=current['id'],state=current['state'],state_reason=current['state_reason']))
Path(str(base)+'.hosted-results.json').write_text(json.dumps(rows,indent=2)+'\n')
Path(str(base)+'.issue15-recovery-readback.json').write_text(json.dumps(current,indent=2)+'\n')
print('GET-only same-endpoint recovery verified exact accepted issue15 payload and preserved foreign/history fields; no PATCH replay.')
