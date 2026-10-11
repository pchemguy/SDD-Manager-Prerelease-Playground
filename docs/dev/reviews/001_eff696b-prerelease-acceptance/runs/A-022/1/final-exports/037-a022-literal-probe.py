import sys,pathlib,importlib,subprocess,json,hashlib,contextlib,io,itertools
root=pathlib.Path(sys.argv[1]).resolve();out=pathlib.Path(sys.argv[2]);sys.path.insert(0,str(root))
cli=importlib.import_module('textstats.cli');assert pathlib.Path(cli.__file__).resolve()==root/'textstats/cli.py'
acquired=[]
def forbidden(*args,**kw):acquired.append([str(x) for x in args]);raise AssertionError('input acquired before rejection')
cli._read_file_text=forbidden;cli.count_file=forbidden
rows=[]
for equals,bom,fmt in itertools.product((False,True),repeat=3):
 args=(['--lines=²:³'] if equals else ['--lines','²:³'])+(['--keep-bom'] if bom else [])+(['--json'] if fmt else [])+[str(root/'a022-independently-missing-input')]
 before=len(acquired);stdout=io.StringIO();stderr=io.StringIO()
 with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):rc=cli.main(args)
 row=dict(argv=args,status=rc,stdout=stdout.getvalue(),stderr=stderr.getvalue(),acquisition_calls=len(acquired)-before)
 row['passed']=rc==2 and row['stdout']=='' and bool(row['stderr']) and 'Traceback' not in row['stderr'] and row['acquisition_calls']==0
 rows.append(row)
 p=subprocess.run([sys.executable,'-B','-m','textstats',*args],cwd=root,capture_output=True)
 row=dict(argv=[sys.executable,'-B','-m','textstats',*args],cwd=str(root),status=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode())
 row['passed']=p.returncode==2 and p.stdout==b'' and bool(p.stderr) and b'Traceback' not in p.stderr and b'ASCII' in p.stderr
 rows.append(row)
result={'schema_version':1,'import_origin':str(pathlib.Path(cli.__file__).resolve()),'runtime':sys.version,'literal_specimen':'²:³','rows':rows,'passed':all(r['passed'] for r in rows)}
out.write_text(json.dumps(result,indent=2));print(json.dumps({'passed':result['passed'],'observations':len(rows),'acquisition_calls':len(acquired)}));sys.exit(0 if result['passed'] else 1)
