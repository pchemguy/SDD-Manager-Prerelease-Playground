from pathlib import Path
import json,re,hashlib,subprocess
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
rows=json.loads(Path(str(base)+'.examples.json').read_text())
expected={2:'lines=0 words=0\nlines=1 words=1\nlines=1 words=2\n',3:'lines=2 words=3\n'*2,4:'lines=1 words=0\nlines=1 words=0\nlines=3 words=3\nlines=1 words=1\nlines=0 words=0\n',5:'',6:'',9:'lines=3 words=5\n'}
for row in rows:
 if row['document']=='README.md':
  n=row['fence']
  if n in expected:assert row['stdout']==expected[n],(n,row['stdout'])
  if n==1:assert row['stdout'].startswith('lines=3 words=5\n') and '--json' not in row['stdout']
  if n==5:assert row['stderr'].count('error:')==4 and 'utf-8' in row['stderr'] and 'Traceback' not in row['stderr']
  if n==7:assert 'unit: 31 tests' in row['stdout'] and 'integration: 28 tests' in row['stdout'] and 'FAILED' not in row['stderr']
  if n==8:assert '241 extracted module cases passed' in row['stdout']
  if n!=5 and n!=7:assert row['stderr']=='',(n,row['stderr'])
 else:assert row['stdout']==row['stderr']==''
print('All documented exact count/help/error/test/extraction/API outputs match contracts, including expected usage/decode failures.')
changed=subprocess.check_output(['git','diff','--name-only','795f3a3542c9981f8d43c8e182876f3efa5b5f16'],text=True).splitlines()
assert not any(p.startswith(('textstats-run-resources/','.github/','docs/testing/','docs/dev/features/')) for p in changed)
assert not any(p in ['textstats/core.py','textstats/io.py','textstats/__init__.py','textstats/__main__.py','tools/package_source.py','AI_DISCLOSURE.md','SDD-MANAGER.md'] for p in changed)
print('Protected resources/closed feature package/pure core/I/O/API/entry/builder/bootstrap paths unchanged by full amendment diff.')
