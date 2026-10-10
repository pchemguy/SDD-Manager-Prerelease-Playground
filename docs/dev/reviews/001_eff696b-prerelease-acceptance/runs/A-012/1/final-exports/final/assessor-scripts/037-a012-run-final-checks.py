import pathlib,subprocess,json,sys,os,zipfile,hashlib
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else base/'037-a012-final-artifacts/final';product=out/'product-export';results=out/'runtime';results.mkdir()
env={k:v for k,v in os.environ.items() if k not in {'PYTHONPATH','PYTHONHOME','PYTHONSTARTUP'}};env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');records=[]
def run(name,cmd,cwd=product):
 r=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,timeout=180);(results/(name+'.stdout')).write_bytes(r.stdout);(results/(name+'.stderr')).write_bytes(r.stderr);records.append({'name':name,'cmd':cmd,'cwd':str(cwd),'env_controlled':{k:env[k] for k in ['PYTHONDONTWRITEBYTECODE','PYTHONNOUSERSITE']},'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()});(results/'commands.json').write_text(json.dumps(records,indent=2)+'\n');return r
script=base/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/cases/assessor/capture.py'
for suite in ['api','baseline','ranges','removal']:
 run('capture-'+suite,[sys.executable,'-B',str(script),'--product-root',str(product),'--suite',suite,'--output',str(results/(suite+'.json')),'--provenance',str(results/(suite+'-provenance.json'))])
run('independent-semantics',[sys.executable,'-B',str(base/'037-a012-semantic-checks.py'),str(product)])
run('nonempty-product-tests',[sys.executable,'-B',str(product/'tools/check_tests.py')])
run('distribution-exits',[sys.executable,'-B',str(product/'tools/check_distribution.py')])
archive=product/'dist/textstats-source.zip';extract=results/'actual-extracted';extract.mkdir()
with zipfile.ZipFile(archive) as z:z.extractall(extract)
exroot=extract/'textstats-source'
(results/'archive-provenance.json').write_text(json.dumps({'archive':str(archive),'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'extracted_root':str(exroot),'members':[{'name':str(p.relative_to(exroot)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in exroot.rglob('*') if p.is_file()]},indent=2)+'\n')
run('capture-distribution',[sys.executable,'-B',str(script),'--product-root',str(exroot),'--suite','distribution','--output',str(results/'distribution.json'),'--provenance',str(results/'distribution-provenance.json')],exroot)
run('extracted-independent-semantics',[sys.executable,'-B',str(base/'037-a012-semantic-checks.py'),str(exroot)],exroot)
merged={'schema_version':1,'literals':{}}
for suite in ['api','baseline','ranges','removal','distribution']:
 path=results/(suite+'.json')
 if path.exists():merged['literals'].update(json.loads(path.read_text())['literals'])
(results/'literal-evidence.json').write_text(json.dumps(merged,indent=2)+'\n');print(json.dumps([{k:r[k] for k in ['name','returncode']} for r in records]))
