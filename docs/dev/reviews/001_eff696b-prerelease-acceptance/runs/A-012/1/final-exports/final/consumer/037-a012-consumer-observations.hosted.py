import json,urllib.request,urllib.error,subprocess,sys,time
from pathlib import Path
repo='pchemguy/SDD-Manager-Prerelease-Playground'
credroot='/workspace/scratch/46b31bb4dff6/SDD-Manager-Prerelease-Playground'
assert subprocess.run(['git','-C',credroot,'check-ignore','-q','gh.tkn']).returncode==0
assert not subprocess.check_output(['git','-C',credroot,'ls-files','gh.tkn'],text=True).strip()
token=Path(credroot,'gh.tkn').read_text().strip()
log=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.hosted.jsonl')
def api(path,method='GET',payload=None):
 url='https://api.github.com/repos/'+repo+'/'+path
 req=urllib.request.Request(url,data=None if payload is None else json.dumps(payload).encode(),method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'textstats-steering'})
 try:
  with urllib.request.urlopen(req,timeout=30) as r:status=r.status;raw=r.read().decode();headers={k:v for k,v in r.headers.items() if k.lower() in ['x-ratelimit-remaining','x-ratelimit-reset','retry-after','link']}
 except urllib.error.HTTPError as r:
  status=r.code;raw=r.read().decode();headers={}
 except urllib.error.URLError as e:
  with log.open('a') as f:f.write(json.dumps(dict(method=method,endpoint=path,payload=payload,status=None,transport_error=str(e),time=time.time()))+'\n')
  raise
 result=json.loads(raw)
 with log.open('a') as f:f.write(json.dumps(dict(method=method,endpoint=path,payload=payload,status=status,response=result,headers=headers,time=time.time()))+'\n')
 assert status<300,(status,path)
 return result
if sys.argv[1]=='read':
 objects={}
 for kind in ['issues','milestones','labels']:
  objects[kind]=[]
  for page in range(1,10):
   data=api(kind+'?state=all&per_page=100&page='+str(page))
   objects[kind]+=data
   if len(data)<100:break
 Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.hosted-before.json').write_text(json.dumps(objects,indent=2)+'\n')
 for i in objects['issues']:
  if 'pull_request' not in i:print(i['number'],i['title'],i['state'],i.get('state_reason'),i['milestone']['number'] if i['milestone'] else None,[l['name'] for l in i['labels']])
 for m in objects['milestones']:print('milestone',m['number'],m['title'],m['state'])
 comments=api('issues/2/comments?per_page=100')
 Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.issue2-comments-before.json').write_text(json.dumps(comments,indent=2)+'\n')
