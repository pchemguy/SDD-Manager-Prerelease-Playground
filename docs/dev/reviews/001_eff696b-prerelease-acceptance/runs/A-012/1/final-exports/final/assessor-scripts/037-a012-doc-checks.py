import pathlib,subprocess,sys,os,re,json,shutil,tempfile,hashlib
out=pathlib.Path(sys.argv[1]).resolve();root=out/'product-export';dest=out/'runtime/docs';dest.mkdir();env={k:v for k,v in os.environ.items() if k not in {'PYTHONPATH','PYTHONHOME','PYTHONSTARTUP'}};env['PATH']=str(pathlib.Path(sys.executable).parent)+os.pathsep+env.get('PATH','');env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');rows=[]
with tempfile.TemporaryDirectory(prefix='a012-docs-exact-') as tmp:
 copy=pathlib.Path(tmp)/'checkout';shutil.copytree(root,copy)
 for name in ['README.md','docs/public-api.md']:
  text=(root/name).read_text()
  for number,m in enumerate(re.finditer(r'```(bash|python)\n(.*?)\n```',text,re.S),1):
   lang,code=m.groups();label=name.replace('/','-')+'-'+str(number);cmd=['bash','-c',code] if lang=='bash' else [sys.executable,'-B','-'];r=subprocess.run(cmd,input=code.encode() if lang=='python' else None,cwd=copy,env=env,capture_output=True,timeout=180);(dest/(label+'.source')).write_text(code+'\n');(dest/(label+'.stdout')).write_bytes(r.stdout);(dest/(label+'.stderr')).write_bytes(r.stderr);expected=1 if 'bad-range.txt' in code else 0;rows.append({'document':name,'fence':number,'language':lang,'source_sha256':hashlib.sha256(code.encode()).hexdigest(),'cmd':cmd,'returncode':r.returncode,'expected_returncode':expected,'passed':r.returncode==expected});(dest/'commands.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows));sys.exit(0 if all(r['passed'] for r in rows) else 1)
