import importlib.util,sys,json,time,re
from pathlib import Path
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
spec=importlib.util.spec_from_file_location('host',Path(str(base)+'.hosted.py'));host=importlib.util.module_from_spec(spec);spec.loader.exec_module(host)
ops=json.loads(Path(str(base)+'.hosted-plan.corrected.json').read_text());before=json.loads(Path(str(base)+'.hosted-before.json').read_text());commit=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',commit)
results=json.loads(Path(str(base)+'.hosted-results.json').read_text())
assert len(results)==5
for op in ops[len(results):]:
 current=host.api(op['endpoint'])
 payload=op['payload'].copy()
 if op['endpoint'].startswith('issues/'):
  old=next(i for i in before['issues'] if i['number']==current['number']);tid=op['task'];marker='sdd-forge:task-id='+tid
  pattern=r'## Task brief <!-- '+re.escape(marker)+r' -->.*?<!-- /'+re.escape(marker)+r' -->'
  assert current['title']==old['title'] and current['body']==old['body'],('Concurrent managed/manual change',tid)
  assert current['state']==old['state'] and current['state_reason']==old['state_reason']
  assert current['milestone']['number']==old['milestone']['number']
  assert re.sub(pattern,'',payload['body'],flags=re.S)==re.sub(pattern,'',current['body'],flags=re.S)
  label_ids=[l['id'] for l in current['labels']]
 response=host.api(op['endpoint'],'PATCH',payload)
 endpoint='labels/'+payload['new_name'] if 'new_name' in payload else op['endpoint']
 readback=host.api(endpoint)
 for field,value in payload.items():assert readback['name' if field=='new_name' else field]==value,(endpoint,field)
 if op['endpoint'].startswith('issues/'):
  assert readback['state']==current['state'] and readback['state_reason']==current['state_reason']
  assert readback['milestone']['number']==current['milestone']['number']
  assert [l['id'] for l in readback['labels']]==label_ids
 if op['endpoint'].startswith('milestones/'):assert readback['state']==current['state']
 results.append(dict(endpoint=endpoint,status='patched and exact fields read back',id=readback['id'],state=readback.get('state'),state_reason=readback.get('state_reason')))
 Path(str(base)+'.hosted-results.json').write_text(json.dumps(results,indent=2)+'\n')
 print(endpoint,'verified',flush=True)
 time.sleep(1)
# Explicit foreign preservation and final full associations.
foreign_issue=host.api('issues/2');original=next(i for i in before['issues'] if i['number']==2)
for field in ['title','body','labels','milestone','state','state_reason','assignees','comments']:assert foreign_issue[field]==original[field],field
foreign_mile=host.api('milestones/1');original_mile=next(m for m in before['milestones'] if m['number']==1)
assert foreign_mile==original_mile,'milestone1 modified'
comments=host.api('issues/2/comments?per_page=100');assert comments==json.loads(Path(str(base)+'.issue2-comments-before.json').read_text()),'issue2 comments modified'
Path(str(base)+'.foreign-preservation-after.json').write_text(json.dumps({'issue2':foreign_issue,'milestone1':foreign_mile,'issue2_comments':comments,'preserved':True},indent=2)+'\n')
allissues=host.api('issues?state=all&per_page=100');assert len(allissues)<100
allmiles=host.api('milestones?state=all&per_page=100');assert len(allmiles)<100
label=host.api('labels/sdd-phase-2-Ranges-and-stdin')
for n in range(10,25):
 tid=f'T-{n:03}';matches=[i for i in allissues if i['title'].startswith('['+tid+'] ') and f'sdd-forge:task-id={tid} -->' in (i['body'] or '') and 'pull_request' not in i];assert len(matches)==1,tid
 i=matches[0];old=next(i for i in before['issues'] if i['number']==n+1)
 assert i['state']==old['state'] and i['state_reason']==old['state_reason'];assert i['milestone']['number']==old['milestone']['number'];assert label['id'] in [l['id'] for l in i['labels']]
Path(str(base)+'.hosted-after.json').write_text(json.dumps({'issues':allissues,'milestones':allmiles,'phase_label':label},indent=2)+'\n')
print('All19 managed operations/readbacks verified; historical completion reasons and five pending open tasks preserved; issue2/comments/milestone1 unchanged.')
