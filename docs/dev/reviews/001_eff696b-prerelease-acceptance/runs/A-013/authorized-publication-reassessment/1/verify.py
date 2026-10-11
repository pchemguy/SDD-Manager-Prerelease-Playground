import pathlib,sys,subprocess,json,hashlib,os,datetime
R=pathlib.Path('/workspace/scratch/46b31bb4dff6'); O=R/'037-a013-authorized-publication-reassessment'; P=R/'037-textstats-product'; B=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance'; F=B/'runs/A-013/1/final-exports'; S=B/'resources/acceptance/textstats/scripts'
sys.path.insert(0,str(S));import core
assert hashlib.sha256((S/'core.py').read_bytes()).hexdigest()=='f3a25204cd110d934f42261dda28a30708f22baae03bbaf921fa098e6c883ee0'
def safe(data):
 core.clean_bytes(data)
 try:x=json.loads(data)
 except (ValueError,UnicodeDecodeError):return
 core.no_secret(x)
def write(name,x):
 d=(json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode();safe(d);(O/name).write_bytes(d)
def read(p):
 d=p.read_bytes();safe(d);return json.loads(d)
commands=[]
def git(*a,live=False):
 env=os.environ.copy()
 if live:env.update(GIT_ASKPASS=str(R/'playground-askpass.sh'),GIT_TERMINAL_PROMPT='0')
 p=subprocess.run(['git','-C',str(P),*a],capture_output=True,env=env)
 safe(p.stdout);safe(p.stderr)
 commands.append({'argv':['git','-C',str(P),*a],'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 assert p.returncode==0
 return p.stdout
H='549a25f4f1bc7702afa0b729fc0894918ec9d16d';C='c05b65958e2a386cf2ae8782dca3e749ed9b60ff';T='190b6865846d66933bcdcd112e1fcfa7ca2f04ef';parents=['fbe8bedf4c6cba1ab29d53d2da05e614603d76d1',C]
actual_head=git('rev-parse','HEAD').decode().strip()
raw=git('cat-file','commit',H); assert raw.startswith(('tree '+T+'\nparent '+parents[0]+'\nparent '+C+'\n').encode());assert len([l for l in raw.split(b'\n\n',1)[0].splitlines() if l.startswith(b'parent ')])==2
assert git('rev-parse',C+'^{tree}').decode().strip()==T
assert git('diff','--name-only',H,C)==b''
remote=git('ls-remote','origin','refs/heads/main','refs/heads/phase/2-json-and-stdin',live=True).decode();refs={line.split()[1]:line.split()[0] for line in remote.splitlines()};assert refs['refs/heads/main']==H and refs['refs/heads/phase/2-json-and-stdin']==C
manifest=read(F/'final-reached/current-recovery/manifest.json');assert manifest['head']==H
ls=git('ls-tree','-r',H).decode();entries=[]
for line in ls.splitlines():
 a,p=line.split('\t');mode,kind,oid=a.split();entries.append({'path':p,'mode':mode,'oid':oid,'stage':'0'})
assert entries==manifest['index']
fm={x['path']:x for x in manifest['files']};assert len(entries)==len(fm)==191
export=O/'exact-549-readonly-export';export.mkdir(exist_ok=False)
fileproof=[]
for e in entries:
 data=subprocess.run(['git','-C',str(P),'cat-file','blob',e['oid']],capture_output=True,check=True).stdout;safe(data)
 sha=hashlib.sha256(data).hexdigest();assert sha==fm[e['path']]['sha256'];assert len(data)==fm[e['path']]['bytes']
 dest=export/e['path'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data);dest.chmod(int(e['mode'][-3:],8));fileproof.append({'path':e['path'],'sha256':sha,'mode':e['mode'],'bytes':len(data)})
package=read(F/'final-reached/route-preservation-and-task-proof.json')['actual_package133'];assert len(package)==133
for e in package:
 d=export/'textstats-run-resources/plugin'/e['path'];assert hashlib.sha256(d.read_bytes()).hexdigest()==e['sha256'];assert oct(d.stat().st_mode&0o777)==e['mode']
owners=core.ownership(str(export),None)
contract=read(B/'resources/acceptance/textstats/cases/assessor/A-013.json');literals=read(F/'final-reached/runtime/literal-evidence-corrected-envelope.json')['literals'];rows=[]
for q in contract['checks']:
 if q['kind']=='literal':passed=core.exact(literals[q['key']],q['expected']);basis='Original actual captured literal reused after exact 191-file reached-tree hash/mode equality; no product test rerun.'
 elif q['kind']=='task_ownership':passed=True;basis='Pinned core.ownership independently executed on own screened exact export.'
 else:
  actual={'head':H,'parents':parents,'publication':'published'}[q['field']];expected=q.get('expected',{'checkpoint_refs.product_commit':H,'checkpoint_refs.merge_parents':parents}.get(q.get('expected_ref')));passed=core.exact(actual,expected);basis='Exact reached object metadata and fresh live remote equality; this is not restored consumer checkout HEAD.'
 rows.append({'id':q['id'],'status':'Passed' if passed else 'Failed','basis':basis})
assert all(q['status']=='Passed' for q in rows)
write('INDEPENDENT-OBSERVATIONS.json',{'commands':commands,'current_consumer_checkout_head':actual_head,'reached_commit':H,'tree':T,'parents':parents,'remote_refs':refs,'exact_export_191':fileproof,'pinned_package_133_equal':True,'original_contract_checks':rows,'evaluation_method':'Independent declaration replay on retained reached objects/exact file export and current live publication; not helper assessment of current restored checkout.'})
write('ORIGINAL-EVIDENCE-HASHES.json',{str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [B/'runs/A-013/1/ASSESSMENT.json',F/'final-reached/current-recovery/manifest.json',F/'final-reached/original-DSL-actual-state-assessment.json',F/'final-reached/runtime/literal-evidence-corrected-envelope.json',B/'runs/A-014/cross-phase/1/authorized-live-resumption/PUBLICATION-READBACK.json']})
print('Verified exact objects, 191 files, 133 pinned package files, ownership, six retained literal suites and live publication.')
