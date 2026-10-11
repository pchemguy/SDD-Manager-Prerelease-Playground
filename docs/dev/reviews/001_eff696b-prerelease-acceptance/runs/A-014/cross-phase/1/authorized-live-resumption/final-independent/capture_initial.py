import os, sys, subprocess, hashlib, json, pathlib, importlib.util, datetime
R=pathlib.Path('/workspace/scratch/46b31bb4dff6'); W=R/'037-a014-cross-phase'; O=R/'037-a014-authorized-independent'/'initial'; O.mkdir(exist_ok=True)
C=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
spec=importlib.util.spec_from_file_location('pinned_core',C); core=importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
def write(p,b):
 core.clean_bytes(b)
 try: v=json.loads(b)
 except (ValueError,UnicodeError): pass
 else: core.no_secret(v)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def run(name,args):
 cp=subprocess.run(args,cwd=W,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','GIT_TERMINAL_PROMPT':'0','GIT_ASKPASS':str(R/'playground-askpass.sh')})
 write(O/(name+'.stdout'),cp.stdout);write(O/(name+'.stderr'),cp.stderr)
 meta={'argv':args,'status':cp.returncode,'time':datetime.datetime.now(datetime.timezone.utc).isoformat()};write(O/(name+'.json'),json.dumps(meta,indent=2).encode());return cp
for name,args in [('head',['git','rev-parse','HEAD']),('status',['git','status','--porcelain=v2']),('index',['git','ls-files','--stage']),('refs',['git','show-ref']),('log',['git','log','--all','--format=%H %P %s']),('diff',['git','diff','--binary']),('index-diff',['git','diff','--cached','--binary']),('live',['git','ls-remote','origin','refs/heads/trial/037-a014-cross-phase','refs/heads/trial/037-a014-cross-main','refs/heads/trial/037-a014-cross-json']),('index-tree',['git','write-tree'])]:run(name,args)
files=run('tracked',['git','ls-files','-z']).stdout.split(b'\0'); hashes={}
for raw in files:
 if not raw:continue
 rel=raw.decode();p=W/rel
 if p.is_file(): b=p.read_bytes();write(O/'files'/rel,b);hashes[rel]=hashlib.sha256(b).hexdigest()
manifest=json.loads((W/'textstats-run-resources/PLUGIN-SOURCE.json').read_text()); expected=manifest['package_file_sha256'] if 'package_file_sha256' in manifest else manifest['package_sha256'] if 'package_sha256' in manifest else None
if expected is None: expected=next(v for k,v in manifest.items() if isinstance(v,dict) and len(v)==133 and 'SKILL.md' in ''.join(v) and k!='package_file_modes')
actual={p.relative_to(W/'textstats-run-resources/plugin').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (W/'textstats-run-resources/plugin').rglob('*') if p.is_file()}
summary={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tracked_file_count':len(hashes),'tracked_sha256':hashes,'pinned_core_sha256':hashlib.sha256(C.read_bytes()).hexdigest(),'plugin_revision':manifest['revision'],'plugin_file_count':len(actual),'plugin_manifest_match':actual==expected,'plugin_sha256':actual,'baseline_expected_head':'7b9f570aa4452d2ca9d6105479640528cb113f0e','limits':['Concurrent consumer read activity; captures are observations, not atomic isolation.','Shared filesystem remains accessible; no native transcript or multi-runtime certification.']}
write(O/'BASELINE.json',json.dumps(summary,indent=2).encode());print(json.dumps({k:v for k,v in summary.items() if k not in ('tracked_sha256','plugin_sha256')},indent=2))
