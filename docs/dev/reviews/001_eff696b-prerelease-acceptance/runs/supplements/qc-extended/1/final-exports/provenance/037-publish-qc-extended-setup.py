import hashlib, importlib.util, json, shutil
from pathlib import Path
r=Path('/workspace/scratch/46b31bb4dff6');b=r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance'
s=importlib.util.spec_from_file_location('gatecore',b/'resources/acceptance/textstats/scripts/core.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
src=r/'037-sup-qc-extended-setup';dst=b/'runs/supplements/qc-extended/1/setup'; manifest={}
for p in sorted(src.rglob('*')):
    if not p.is_file():continue
    data=p.read_bytes();c.clean_bytes(data)
    if p.suffix=='.json':c.no_secret(json.loads(data))
    name=p.relative_to(src).as_posix();manifest[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    out=dst/name;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
script=(r/'037-prepare-qc-extended.py').read_bytes();c.clean_bytes(script);(dst/'CALLER-AUTHOR.py').write_bytes(script)
provenance={'scope':'Four synthetic caller-authored proposals in isolated actual8036 accepted-preparation Git forks; read-only consumer sensitivity, outside required32 grades. No real completion/production alteration.', 'mutations':{'a':'Ten seam-specific delivery milestones delay first useful range CLI; all original stable identities and retained coverage remain.','b':'Ten delivery tasks retain original four plus six tiny overlapping tasks; dedicated reviews excluded.','c':'Proposed public positional range API changes conflict with unchanged accepted whole-input design/main contracts.','d':'Proposed mandatory runtime third-party benchmark/throughput work outside accepted feature strategy.'}, 'manifest':manifest,'root_setup_errors':'Initial readonly git-show used archived rather than active FEATURE paths and failed without edits; corrected actual docs/dev FEATURE paths. Ordinary input pinned path corrected before dispatch to existing per-checkout textstats-run-resources/plugin.','limits':'Shared filesystem/batched context exposure and local synthetic-proposal limits; no technical Ready/runtime certification implied.'}
data=(json.dumps(provenance,indent=2)+'\n').encode();c.clean_bytes(data);c.no_secret(provenance);(dst/'PROVENANCE.json').write_bytes(data)
print(len(manifest),'setup artifacts screened')
