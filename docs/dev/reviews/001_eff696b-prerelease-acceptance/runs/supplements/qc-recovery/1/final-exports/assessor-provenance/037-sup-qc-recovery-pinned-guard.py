import importlib.util,json,hashlib,shutil,sys
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6');D=R/'037-sup-qc-recovery-final-artifacts';P=R/'037-sup-qc-recovery-rejected-private';P.mkdir(exist_ok=True);P.chmod(0o700)
cpath=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';s=importlib.util.spec_from_file_location('c',cpath);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
records=[];reject=[]
for f in list(D.rglob('*')):
 if not f.is_file():continue
 b=f.read_bytes();n=f.relative_to(D).as_posix();record={'path':n,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
 try:
  c.clean_bytes(b)
  if f.suffix=='.json':c.no_secret(json.loads(b))
 except c.Stop as e:
  record.update({'cause':e.cause,'exported':False,'original_retained_privately':True});reject.append(record);dest=P/n;dest.parent.mkdir(parents=True,exist_ok=True);shutil.move(f,dest)
 else:record.update({'clean_bytes':True,'no_secret':f.suffix=='.json'});records.append(record)
j={'pinned_core_sha256':hashlib.sha256(cpath.read_bytes()).hexdigest(),'all_public_bytes_pass_actual_pinned_core':True,'custom_guard_is_not_publication_authorization':True,'files':records,'omissions':reject};b=(json.dumps(j,indent=2)+'\n').encode();c.clean_bytes(b);c.no_secret(j);(D/(sys.argv[1]+'-pinned-guard.json')).write_bytes(b);print(json.dumps({'rejected':reject,'retained_public_files':len(records)}))
