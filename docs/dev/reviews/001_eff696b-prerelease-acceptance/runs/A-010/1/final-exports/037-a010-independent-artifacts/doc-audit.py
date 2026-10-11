import re,json,hashlib,subprocess,unicodedata
from pathlib import Path
r=Path('/workspace/scratch/46b31bb4dff6/037-textstats-product');o=Path(__file__).parent;f=r/'docs/dev/features/002_e7cae5b-named-file-ranges';head='795f3a3542c9981f8d43c8e182876f3efa5b5f16';transfer='6f1614480687f5978023df1122ec8b2567ff19d9'
def git(*a):return subprocess.check_output(['git',*a],cwd=r).decode()
links=[]
selected=[r/'AGENTS.md',r/'docs/dev/SPEC.md',r/'docs/dev/PLAN.md',r/'docs/dev/TASKS.md',r/'docs/dev/SPEC-REVIEW-REPORT.md',r/'docs/dev/PLAN-REVIEW-REPORT.md',r/'docs/dev/TASKS-REVIEW-REPORT.md',*sorted(f.rglob('*.md'))]
for p in selected:
 text=p.read_text()
 for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',text):
  dest=m.group(1)
  if re.match(r'[a-z]+://',dest):continue
  path,_,anchor=dest.partition('#');q=(p.parent/path).resolve() if path else p
  exists=q.is_file();valid=exists
  if anchor and exists:
   target=q.read_text();heads=re.findall(r'^#{1,6}\s+(.+)$',target,re.M);anchors=[]
   for h in heads:
    h=re.sub(r'[`*_]','',h).strip().lower();h=''.join(c for c in h if c.isalnum() or c in ' _-');anchors.append(h.replace(' ','-'))
   valid=anchor in anchors or bool(re.search(r'(?:id|name)=["\']'+re.escape(anchor)+r'["\']',target))
  links.append({'source':str(p.relative_to(r)),'target':dest,'exists':exists,'anchor_valid':valid})
archive=[]
for name in ['FEATURE-SPEC.md','FEATURE-PLAN.md','FEATURE-TASKS.md','FEATURE-SPEC-REVIEW-REPORT.md','FEATURE-PLAN-REVIEW-REPORT.md','FEATURE-TASKS-REVIEW-REPORT.md']:
 old=git('show',transfer+'^:docs/dev/'+name);new=(f/name).read_text();body=new[new.index('# '):]
 # compare ordinary words/history exactly, permitting authorized hyperlink path rebasing only.
 strip=lambda s:re.sub(r'(\[[^\]]+\]\()[^)]+(\))',r'\1TARGET\2',s)
 archive.append({'name':name,'original_sha256':hashlib.sha256(old.encode()).hexdigest(),'archived_sha256':hashlib.sha256(new.encode()).hexdigest(),'historical_header':'Historical archived source/QC snapshot' in new.split('# ')[0],'original_body_retained_except_links':strip(old)==strip(body),'root_active_absent':not (r/'docs/dev'/name).exists()})
main=(r/'docs/dev/TASKS.md').read_text();original=git('show',transfer+'^:docs/dev/FEATURE-TASKS.md')
def entries(text):
 lines=text.splitlines(keepends=True);out={}
 for i,line in enumerate(lines):
  m=re.match(r'        - \[[ x]\] (T-\d{3}) — ',line)
  if m:
   j=i+1
   while j<len(lines) and (not lines[j].strip() or lines[j].startswith('            ')):j+=1
   out[m.group(1)]=''.join(lines[i:j]).rstrip()
 return out
oldentries,newentries=entries(original),entries(main)
transfer_checks=[{'id':i,'same_entry_status_outcome_scope_dependencies_evidence_report':oldentries[i]==newentries[i]} for i in oldentries]
qc=[]
for name in ['SPEC','PLAN','TASKS']:
 text=(r/('docs/dev/'+name+'-REVIEW-REPORT.md')).read_text();latest=text.rsplit('\n## Revision ',1)[-1];root_hash=hashlib.sha256((r/('docs/dev/'+name+'.md')).read_bytes()).hexdigest();qc.append({'root':name,'root_sha256':root_hash,'latest_revision':latest.splitlines()[0],'current_root_hash_in_latest':root_hash in latest,'preserves_initial_and_history':'Initial' in text or 'initial' in text,'current_gate_ready':'Ready' in text[:1400]})
reports=[]
for p in [f/'phases/2/2.4.md',f/'phases/2/2.5.md',f/'phases/2/PHASE-REPORT.md',f/'IMPLEMENTATION-REPORT.md']:
 t=p.read_text();reports.append({'path':str(p.relative_to(r)),'committed_blob':git('rev-parse',head+':'+str(p.relative_to(r))).strip(),'contains_review':bool(re.search('review',t,re.I)),'contains_tests':bool(re.search('tests|test',t,re.I)),'contains_todo':bool(re.search('TODO',t)),'pending_main_scope_retained':bool(re.search('stdin|T-013|Phase 2',t))})
result={'local_links':links,'bad_links':[z for z in links if not z['anchor_valid']],'archive':archive,'transferred_entries':transfer_checks,'main_current_qc':qc,'reports':reports};(o/'document-audit.json').write_text(json.dumps(result,indent=2)+'\n');print({'links':len(links),'bad_links':result['bad_links'],'archive_body_pass':all(x['original_body_retained_except_links'] for x in archive),'transfer_entry_pass':all(x['same_entry_status_outcome_scope_dependencies_evidence_report'] for x in transfer_checks),'current_qc':qc})
