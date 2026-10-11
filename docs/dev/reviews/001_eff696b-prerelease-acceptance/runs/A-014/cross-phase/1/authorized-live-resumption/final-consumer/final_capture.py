import hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
artifact=Path('/workspace/scratch/46b31bb4dff6/037-a014-authorized-consumer-artifacts')
records=[]
def git(*arguments):
    command=['git','--no-optional-locks',*arguments]
    result=subprocess.run(command,capture_output=True,text=True)
    records.append({'command':command,'cwd':str(Path.cwd()),'status':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    assert result.returncode==0,records[-1]
    return result.stdout.strip()
head=git('rev-parse','HEAD')
assert head=='2d2fbfcc38808104b66267a9179660136c75dc97'
tree=git('rev-parse','HEAD^{tree}')
assert tree=='6fa480a4a168292ec49061e099c05ec02d200fa5'
branch=git('branch','--show-current')
assert branch=='phase/2-json-and-stdin'
status=git('status','--porcelain=v1','--untracked-files=all')
assert all(line.startswith('?? ') for line in status.splitlines())
protected=git('diff','--name-only','88a5c4b4424f4bba76940e40b1d6523b1f6fe191','HEAD','--','textstats-run-resources','.github','docs/testing/publisher-037')
assert protected==''
refs=git('ls-remote','origin','refs/heads/trial/037-a014-cross-phase','refs/heads/trial/037-a014-cross-main','refs/heads/trial/037-a014-cross-json')
assert '2d2fbfcc38808104b66267a9179660136c75dc97\trefs/heads/trial/037-a014-cross-json' in refs
for commit,task in [('dfcd658828d8e326c713683f3cdb9be05e044849','T-009'),(head,'T-010')]:
    subject=git('show','-s','--format=%s',commit)
    assert subject.startswith('['+task+'] ')
    git('show','-s','--format=%H%n%P%n%T',commit)
    diff=git('diff',commit+'^',commit,'--','docs/dev/TASKS.md')
    initial=[line for line in diff.splitlines() if line.startswith('+') and '[x] T-' in line]
    assert len(initial)==1 and task in initial[0]
unknown={name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in ['sample.txt','bom.txt','-sample']}
capture={'time_utc':datetime.now(timezone.utc).isoformat(),'head':head,'tree':tree,'branch':branch,'records':records,'untracked_preserved':unknown,'isolation_certified':False,'stopping_boundary':'T-010 complete; T-011 onward unselected; no Phase 2 main integration','private_current_source_archive_sha256':hashlib.sha256((artifact/'t010-current-source.zip').read_bytes()).hexdigest()}
output=artifact/'final-capture.json'
output.write_text(json.dumps(capture,indent=2)+'\n')
print(output)
print('FINAL CAPTURE SHA256',hashlib.sha256(output.read_bytes()).hexdigest())
print('HEAD',head,'TREE',tree,'BRANCH',branch)
print('REMOTE READBACK\n'+refs)
print('STOPPED; tracked clean; unknown samples preserved; protected paths diff empty')
