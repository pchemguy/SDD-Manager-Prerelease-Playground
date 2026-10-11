"""Independent range probes with chosen literal expectations, read-only product import."""
import sys,os,json,tempfile,subprocess,hashlib,itertools
from pathlib import Path
root=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]); rows=[]
env=dict(os.environ,PYTHONPATH=str(root),PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='0',LC_ALL='C')
with tempfile.TemporaryDirectory(prefix='a010-independent-') as d:
 cwd=Path(d); file=cwd/'sample.txt'
 def run(name,data,args,rc,stdout=None,jobj=None):
  file.write_bytes(data); before=hashlib.sha256(data).hexdigest()
  cmd=[sys.executable,'-B','-m','textstats',*args]
  p=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,timeout=30)
  after=hashlib.sha256(file.read_bytes()).hexdigest()
  expected=dict(returncode=rc,stdout=stdout,json=jobj)
  success=p.returncode==rc and before==after
  if rc==0:
   success=success and p.stderr==b''
   if jobj is None: success=success and p.stdout==stdout.encode()
   else:
    try: actual=json.loads(p.stdout);success=success and actual==jobj and all(type(x) is int for x in actual.values()) and p.stdout.endswith(b'\n')
    except ValueError: success=False
  else: success=success and p.stdout==b'' and bool(p.stderr.strip()) and b'Traceback (most recent call last)' not in p.stderr
  rows.append(dict(name=name,command=cmd,cwd=d,expected=expected,returncode=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace'),input_sha256=before,after_sha256=after,passed=bool(success)))
 anchors=[('normal',b'alpha beta\nbeta\nlast two','2:3',2,3),('partial',b'alpha beta\nbeta\nlast two','2:99',2,3),('one',b'alpha beta\nbeta\nlast two','1:1',1,2),('zeroes',b'alpha beta\nbeta\nlast two','0001:0001',1,2),('past',b'alpha beta\nbeta\nlast two','4:99',0,0),('blank',b'a\n\n','2:9',1,0),('mixed',b'a\r\nb c\rd\n','2:3',2,3),('interior','a\n\ufeff'.encode(),'2:2',1,1),('empty',b'','1:99',0,0),('doublebom','\ufeff\ufeff'.encode(),'1:1',1,1),('separator','alpha\u2028beta'.encode(),'1:1',1,2),('lf',b'\n','1:1',1,0)]
 for name,data,r,l,w in anchors:
  for keep,j in itertools.product([False,True],repeat=2):
   flags=['--lines',r]+(['--keep-bom'] if keep else [])+(['--json'] if j else [])
   run(name+str((keep,j)),data,[*flags,'sample.txt'],0,stdout=f'lines={l} words={w}\n',jobj={'lines':l,'words':w} if j else None)
 for keep,j in itertools.product([False,True],repeat=2):
  l=w=1 if keep else 0
  run('bom'+str((keep,j)),'\ufeff'.encode(),['sample.txt','--lines=1:1']+(['--keep-bom'] if keep else [])+(['--json'] if j else []),0,stdout=f'lines={l} words={w}\n',jobj={'lines':l,'words':w} if j else None)
 for spelling in [['--lines','1:1'],['--lines=1:1']]:
  for perm in itertools.permutations([spelling,['--keep-bom'],['--json']]):
   flags=sum((x for x in perm),[])
   for first in [False,True]:
    run('permutation'+str((spelling,perm,first)),'\ufeffalpha beta\nbeta'.encode(),(['sample.txt']+flags if first else flags+['sample.txt']),0,jobj={'lines':1,'words':2})
 huge='9'*4400; zeroes='0'*4400
 for name,r,l,w in [('hugeEND','1:'+huge,2,3),('hugeSTART',huge+':'+huge,0,0),('longzeros',zeroes+'1:'+zeroes+'1',1,2)]:
  for j in [False,True]:run(name+str(j),b'alpha beta\nbeta', ['--lines',r,'sample.txt']+(['--json'] if j else []),0,stdout=f'lines={l} words={w}\n',jobj={'lines':l,'words':w} if j else None)
 invalid=['0:1','1:0','3:2','-1:2','+1:2','1:-2','1:+2',' 1:2','1:2 ','1 :2','1:\t2','١:٢','１:２',':2','1:',':','1:2:3','1','']
 for r in invalid:run('invalid-'+repr(r),b'alpha', ['--lines='+r,'missing.txt'],2)
 for args in [['--lines'],['--lines','--json','missing.txt'],['--lines=1:1','--lines=1:1','missing.txt'],['--lines','1:1','--lines=1:1','missing.txt']]:run('missingrepeat'+str(args),b'alpha',args,2)
 for j in [False,True]:run('decode-afterEND'+str(j),b'alpha\n\xff',['--lines=1:1','sample.txt']+(['--json'] if j else []),1)
 output={'case_id':'A-010','product_root':str(root),'rows':rows,'total':len(rows),'passed':sum(r['passed'] for r in rows),'kind':'independent literal command observations'}
 out.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'total':len(rows),'passed':output['passed'],'output':str(out)}))
