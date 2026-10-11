import sys,contextlib,io,json,inspect,tempfile,subprocess,os
from pathlib import Path
from unittest.mock import patch
root=Path(sys.argv[1]).resolve();sys.path.insert(0,str(root));import textstats;import textstats.cli as cli;import textstats.io as acquisition
rows=[]
invalid=[['--lines='+r,'absent.txt'] for r in ['0:1','1:0','3:2','+1:2','-1:2','1:+2','1:-2',' 1:2','1:2 ','1 :2','1:\t2','١:٢','１:２',':2','1:',':','1:2:3','1','']]+[['--lines'],['--lines','--json','absent.txt'],['--lines','1:2','--lines=1:2','absent.txt'],['absent.txt','extra.txt'],['--unknown','absent.txt'],['--lin=1:2','absent.txt']]
for args in invalid:
 out,err=io.StringIO(),io.StringIO()
 with patch.object(cli,'count_file',side_effect=AssertionError('acquisition reached')) as c,patch.object(cli,'_read_file_text',side_effect=AssertionError('acquisition reached')) as r,contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):code=cli.main(args)
 rows.append({'name':'usage-before-acquisition','args':args,'returncode':code,'stdout':out.getvalue(),'stderr':err.getvalue(),'acquisition_calls':c.call_count+r.call_count,'passed':code==2 and out.getvalue()=='' and bool(err.getvalue()) and c.call_count+r.call_count==0})
for payload,expected_error in [(b'alpha\n',None),(b'alpha\n\xff','UnicodeDecodeError')]:
 stream=io.BytesIO(payload);out,err=io.StringIO(),io.StringIO();error=None;result=None
 with patch('builtins.open',return_value=stream),contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
  try:stats=textstats.count_file('owned.txt');result=[stats.lines,stats.words]
  except Exception as e:error=type(e).__name__
 rows.append({'name':'owned-handle-close','payload_hex':payload.hex(),'exception':error,'result':result,'closed':stream.closed,'stdout':out.getvalue(),'stderr':err.getvalue(),'passed':stream.closed and error==expected_error and out.getvalue()==err.getvalue()=='' and (expected_error or result==[1,1])})
class Broken(io.BytesIO):
 def read(self,*a,**kw):raise OSError('controlled owned read failure')
stream=Broken(b'data');out,err=io.StringIO(),io.StringIO()
with patch('builtins.open',return_value=stream),contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):code=cli.main(['--lines=1:1','owned.txt'])
rows.append({'name':'read-error-cleanup','returncode':code,'closed':stream.closed,'stdout':out.getvalue(),'stderr':err.getvalue(),'passed':code==1 and stream.closed and out.getvalue()=='' and 'owned.txt' in err.getvalue() and 'Traceback' not in err.getvalue()})
rows.append({'name':'API-export-signature','exports':textstats.__all__,'text_signature':str(inspect.signature(textstats.count_text)),'file_signature':str(inspect.signature(textstats.count_file)),'passed':set(textstats.__all__)=={'TextStats','count_text','count_file'} and list(inspect.signature(textstats.count_text).parameters)==['text','strip_bom'] and list(inspect.signature(textstats.count_file).parameters)==['path','strip_bom'] and all(inspect.signature(f).parameters['strip_bom'].kind==inspect.Parameter.KEYWORD_ONLY and inspect.signature(f).parameters['strip_bom'].default is True for f in [textstats.count_file,textstats.count_text])})
with tempfile.TemporaryDirectory(prefix='a010-minus-') as d:
 p=Path(d)/'-';p.write_bytes(b'alpha beta\nbeta');env=dict(os.environ,PYTHONPATH=str(root),PYTHONDONTWRITEBYTECODE='1')
 for name in ['-','./-']:
  cmd=[sys.executable,'-B','-m','textstats','--lines=2:2',name];result=subprocess.run(cmd,cwd=d,env=env,input=b'wrong stdin',capture_output=True)
  rows.append({'name':'literal-minus-named-file','command':cmd,'returncode':result.returncode,'stdout':result.stdout.decode(),'stderr':result.stderr.decode(),'passed':(result.returncode,result.stdout,result.stderr)==(0,b'lines=1 words=1\n',b'') and p.read_bytes()==b'alpha beta\nbeta'})
body={'actual_import':str(Path(textstats.__file__).resolve()),'rows':rows,'total':len(rows),'passed':sum(bool(r['passed']) for r in rows)};Path(sys.argv[2]).write_text(json.dumps(body,indent=2)+'\n');print({'total':body['total'],'passed':body['passed']})
