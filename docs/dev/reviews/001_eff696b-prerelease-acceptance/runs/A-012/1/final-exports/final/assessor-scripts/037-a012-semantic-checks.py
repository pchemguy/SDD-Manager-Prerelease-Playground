import os,sys,pathlib,json,tempfile,subprocess,contextlib,io as pyio,unittest.mock as mock,inspect,hashlib
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root))
import textstats
from textstats import cli,io,TextStats,count_text,count_file
assert pathlib.Path(textstats.__file__).resolve()==root/'textstats/__init__.py'
rows=[]
def record(name,actual,expected):
 rows.append({'name':name,'actual':actual,'expected':expected,'passed':actual==expected})
for args in [['--json','missing'],['missing','--json'],['--json'],['--json','--lines','1:1','missing'],['--json=1','missing'],['--j','missing'],['--lines','0:1','missing'],['--lines','١:٢','missing'],['--lines','1:2','--lines','1:2','missing']]:
 with mock.patch.object(cli,'count_file',side_effect=AssertionError('acquired')) as whole,mock.patch.object(cli,'_read_file_text',side_effect=AssertionError('acquired')) as ranged,contextlib.redirect_stdout(pyio.StringIO()) as out,contextlib.redirect_stderr(pyio.StringIO()) as err:
  code=cli.main(args)
  record('usage-before-acquisition:'+repr(args),[code,out.getvalue(),whole.call_count,ranged.call_count,bool(err.getvalue()),'Traceback' in err.getvalue()],[2,'',0,0,True,False])
with mock.patch.object(cli,'count_file',side_effect=AssertionError('acquired')) as whole,mock.patch.object(cli,'_read_file_text',side_effect=AssertionError('acquired')) as ranged,contextlib.redirect_stdout(pyio.StringIO()) as out,contextlib.redirect_stderr(pyio.StringIO()) as err:
 code=cli.main(['--help']);record('help',[code,whole.call_count,ranged.call_count,err.getvalue(),'--json' in out.getvalue(),'--keep-bom' in out.getvalue(),'--lines' in out.getvalue()],[0,0,0,'',False,True,True])
class Owned:
 def __init__(self,data=None,error=None):self.data=data;self.error=error;self.closed=False
 def __enter__(self):return self
 def __exit__(self,*args):self.closed=True
 def read(self):
  if self.error:raise self.error
  return self.data
for name,data,error,expected in [('success',b'a\r\nb c',None,TextStats(2,3)),('decode',b'a\n\xff',None,'UnicodeDecodeError'),('read',None,OSError('controlled read'),'OSError')]:
 stream=Owned(data,error)
 with mock.patch('builtins.open',return_value=stream) as opened,contextlib.redirect_stdout(pyio.StringIO()) as out,contextlib.redirect_stderr(pyio.StringIO()) as err:
  try:r=count_file('owned');r=[r.lines,r.words]
  except Exception as e:r=type(e).__name__
  want=[expected.lines,expected.words] if isinstance(expected,TextStats) else expected
  record('owned-resource:'+name,[r,stream.closed,opened.call_args.args,out.getvalue(),err.getvalue()],[want,True,('owned','rb'),'',''])
record('public-exports',sorted(textstats.__all__),sorted(['TextStats','count_file','count_text']))
for f in [count_file,count_text]:
 sig=inspect.signature(f);record('public-signature:'+f.__name__,[list(sig.parameters),sig.parameters['strip_bom'].kind.name,sig.parameters['strip_bom'].default],[[('path' if f is count_file else 'text'),'strip_bom'],'KEYWORD_ONLY',True])
with tempfile.TemporaryDirectory(prefix='a012-independent-') as tmp:
 tmp=pathlib.Path(tmp);sample=tmp/'sample';dash=tmp/'--json';dash.write_bytes(b'one two\n');
 def invoke(args):
  env={k:v for k,v in os.environ.items() if k not in {'PYTHONPATH','PYTHONHOME','PYTHONSTARTUP'}};env['PYTHONPATH']=str(root);env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONNOUSERSITE']='1';p=subprocess.run([sys.executable,'-B','-s','-m','textstats',*args],cwd=tmp,env=env,capture_output=True);return [p.returncode,p.stdout.decode(),p.stderr.decode()]
 record('literal-json-filename',invoke(['--','--json']),[0,'lines=1 words=2\n',''])
 for name,raw,flags,expected in [('interior-bom',b'a\n'+ '\ufeff'.encode(),['--lines','2:2'],'lines=1 words=1\n'),('bom-only','\ufeff'.encode(),['--lines','1:1'],'lines=0 words=0\n'),('kept-bom','\ufeff'.encode(),['--keep-bom','--lines','1:1'],'lines=1 words=1\n'),('double-bom','\ufeff\ufeff'.encode(),['--lines','1:1'],'lines=1 words=1\n'),('mixed',b'a\r\nb c\rd\n',['--lines','2:3'],'lines=2 words=3\n')]:
  sample.write_bytes(raw);record(name,invoke([*flags,str(sample)]),[0,expected,'']);record(name+'-immutable',sample.read_bytes().hex(),raw.hex())
 sample.write_bytes(b'a b\nc\nd');huge='9'*5001
 for name,endpoints,output in [('huge-end','2:'+huge,'lines=2 words=2\n'),('huge-start',huge+':'+huge,'lines=0 words=0\n'),('huge-zeros','0'*5000+'2:'+'0'*5000+'3','lines=2 words=2\n')]:record(name,invoke(['--lines='+endpoints,str(sample)]),[0,output,''])
 guard=sys.get_int_max_str_digits()
 with contextlib.redirect_stdout(pyio.StringIO()) as out,contextlib.redirect_stderr(pyio.StringIO()) as err:
  code=cli.main(['--lines=2:'+huge,str(sample)]);record('integer-digit-guard',[code,sys.get_int_max_str_digits(),out.getvalue(),err.getvalue()],[0,guard,'lines=2 words=2\n',''])
 sample.write_bytes(b'a\n\xff');r=invoke(['--lines','1:1',str(sample)]);record('decode-after-end',[r[0],r[1],str(sample) in r[2],'Traceback' in r[2]],[1,'',True,False])
 sample.write_bytes(b'a b\nc');record('public-file-whole-input',[count_file(sample).lines,count_file(sample).words],[2,3])
print(json.dumps({'import_origin':str(textstats.__file__),'checks':rows,'passed':all(x['passed'] for x in rows)},indent=2));sys.exit(0 if all(x['passed'] for x in rows) else 1)
