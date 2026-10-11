"""Bounded fixture eligibility and cooperative actual-operation hold controls.

These controls retain observed state, never fabricate consumer actions. A caller
must separately establish actor, authorized scope, selected protocol and fresh
continuation. They do not certify native termination or live recovery.
"""
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
import subprocess
import sys

sys.path.insert(0,str(Path(__file__).parent))
import core


def digest(value):
    """Hash a canonical nonsecret record for command/state drift detection."""
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()


def facilities(variant, available):
    """Classify missing declared facilities without downgrading required checks."""
    missing=[x for x in variant['facilities'] if x not in available]
    return {'status':('Not run' if variant['requirement']=='optional' else 'Blocked') if missing else 'Eligible','missing':missing,'requirement':variant['requirement']}


def eligibility(root, document, task_ids):
    """Read actual committed task completion for an explicitly selected prerequisite.

    The coordinator derives the entire prerequisite/phase ID set from accepted
    owners and separately checks review/closure/exit/publication evidence. This
    helper only proves named rows are present/checked at a retained clean commit.
    """
    root=Path(root).resolve();path=core.relative(root,document)
    if not task_ids or len(task_ids)!=len(set(task_ids)):raise ValueError('empty/duplicate prerequisite selection')
    head=core.git(root,'rev-parse','HEAD').stdout.strip()
    committed=core.git(root,'show',head+':'+document,required=False)
    if committed.returncode or not path.is_file() or path.read_text()!=committed.stdout:raise ValueError('missing or uncommitted task owner')
    if core.git(root,'diff','--cached','--quiet','--',document,required=False).returncode:raise ValueError('staged task owner')
    rows={}
    for _,identifier,status in core.task_rows(committed.stdout):
        if identifier in rows:raise ValueError('duplicate task owner')
        rows[identifier]=status
    if any(x not in rows for x in task_ids):raise ValueError('missing prerequisite')
    if any(rows[x] not in {'Checked','Complete','Completed','Done'} for x in task_ids):raise ValueError('incomplete prerequisite')
    return {'status':'Eligible','commit':head,'document':document,'task_ids':list(task_ids),'claim':'Committed named task rows only; other exit evidence assessed separately'}


def snapshot(root, watched):
    """Capture Git/index/merge and selected file identity without exporting contents."""
    root=Path(root).resolve();files={}
    for name in watched:
        p=core.relative(root,name)
        if p.is_symlink():raise ValueError('symlink watch')
        files[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mode':p.stat().st_mode & 0o777} if p.is_file() else None
    merge=core.git(root,'rev-parse','--git-path','MERGE_HEAD').stdout.strip();merge=Path(merge) if Path(merge).is_absolute() else root/merge
    return {'head':core.git(root,'rev-parse','HEAD').stdout.strip(),'branch':core.git(root,'symbolic-ref','--quiet','--short','HEAD',required=False).stdout.strip(),'index_sha256':hashlib.sha256(core.git(root,'ls-files','--stage','-z',binary=True).stdout).hexdigest(),'merge_heads':merge.read_text().splitlines() if merge.exists() else [],'files':files}


def execute(root, actions, watched, receipt, hold_after=None, resume=False, pending_paths=()):
    """Run an explicit operation sequence and hold after observed partial work.

    Args:
        root: Authorized disposable Git checkout; never chosen by this helper.
        actions: Nonempty argv lists provided by the authorized actor, no shell.
        watched: Explicit nonsecret relative file names for preservation evidence.
        receipt: Caller-owned nonsecret gate record outside watched product files.
        hold_after: Operation count at which to hold, strictly before the end.
        resume: Continue the same held sequence after exact snapshot comparison.
        pending_paths: Selected transfer paths that must still match start at hold.

    A failed/unknown action is retained and requires independent reconciliation,
    rather than automatic replay. Held is cooperative control, not native kill.
    """
    root=Path(root).resolve();receipt=Path(receipt).absolute();core.no_secret(actions)
    # Preserve the caller's lexical path until link checks have run. Resolving
    # first would hide both a dangling receipt link and symlinked parents.
    if any(path.is_symlink() for path in (receipt,*receipt.parents)):
        raise ValueError('symlink receipt path')
    receipt=receipt.resolve()
    if not isinstance(actions,list) or not actions or any(not isinstance(a,list) or not a or any(not isinstance(x,str) or not x or '\x00' in x for x in a) for a in actions):raise ValueError('invalid action argv')
    if not watched or len(watched)!=len(set(watched)) or any(p not in watched for p in pending_paths):raise ValueError('invalid watch/pending selection')
    if any(receipt==(root/p).resolve() for p in watched):raise ValueError('receipt overlaps product')
    identity=digest({'root':str(root),'actions':actions,'watched':watched,'pending_paths':list(pending_paths)})
    current=snapshot(root,watched)
    if resume:
        record=core.load(receipt)
        if record.get('status')!='Held' or record.get('identity')!=identity or record.get('held_snapshot')!=current:raise ValueError('not held or changed continuation state')
        start=record['completed']
    else:
        if receipt.exists():raise ValueError('receipt occupied')
        if hold_after is not None and (type(hold_after) is not int or not 0<hold_after<len(actions)):raise ValueError('hold must precede pending operation')
        record={'schema_version':1,'identity':identity,'status':'Started','completed':0,'start_snapshot':current,'commands':[],'evidence_class':'controlled','agent_behavior_assessed':False};start=0
    def save():
        core.no_secret(record);receipt.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(mode='w',dir=receipt.parent,prefix=receipt.name+'.',suffix='.tmp',delete=False) as stream:
            json.dump(record,stream,indent=2);stream.write('\n');temporary=stream.name
        os.replace(temporary,receipt)
    save()
    for i in range(start,len(actions)):
        record['status']='Running';record['pending_action']=i;save()
        try:
            proc=subprocess.run(actions[i],cwd=root,capture_output=True,timeout=60)
            row={'argv':actions[i],'returncode':proc.returncode}
            try:row.update(stdout=core.clean_bytes(proc.stdout).decode(errors='replace'),stderr=core.clean_bytes(proc.stderr).decode(errors='replace'))
            except core.Stop:row['channels']='Withheld: sensitive content'
        except (OSError,subprocess.TimeoutExpired) as error:
            row={'argv':actions[i],'returncode':None,'status':'Interrupted','failure':type(error).__name__}
            if isinstance(error,subprocess.TimeoutExpired):
                try:
                    row.update(stdout=core.clean_bytes(error.stdout or b'').decode(errors='replace'),stderr=core.clean_bytes(error.stderr or b'').decode(errors='replace'))
                except core.Stop:
                    row['channels']='Withheld: sensitive content'
            record['commands'].append(row)
            record['status']='Uncertain';record['failure']=type(error).__name__;save();raise ValueError('operation incomplete; reconcile before retry') from error
        record['commands'].append(row)
        if proc.returncode:record['status']='Failed';save();return record
        record['completed']=i+1;record.pop('pending_action',None)
        if not resume and hold_after==i+1:
            held=snapshot(root,watched)
            if held==record['start_snapshot']:
                record['status']='Trigger missing';save();raise ValueError('no actual partial change')
            if any(held['files'][p]!=record['start_snapshot']['files'][p] for p in pending_paths):
                record['status']='Trigger missing';save();raise ValueError('pending transfer already changed')
            record.update(status='Held',held_snapshot=held);save();return record
        save()
    record['status']='Completed';record['final_snapshot']=snapshot(root,watched);save();return record


def main():
    """Execute a caller-authorized manifest; report control facts, never case grades."""
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,required=True);parser.add_argument('--manifest',type=Path);parser.add_argument('--receipt',type=Path);parser.add_argument('--check-document');parser.add_argument('--tasks',nargs='+');parser.add_argument('--hold-after',type=int);parser.add_argument('--resume',action='store_true');args=parser.parse_args()
    try:
        if args.check_document:
            if args.manifest or args.resume or not args.tasks:raise ValueError('eligibility arguments')
            print(json.dumps(eligibility(args.root,args.check_document,args.tasks)));return 0
        if not args.manifest or not args.receipt:raise ValueError('manifest and receipt required')
        manifest=core.load(args.manifest);record=execute(args.root,manifest['actions'],manifest['watched'],args.receipt,args.hold_after,args.resume,manifest.get('pending_paths',[]));print(json.dumps({'status':record['status'],'completed':record['completed'],'agent_behavior_assessed':False}));return 0 if record['status'] in {'Held','Completed'} else 1
    except (ValueError,OSError,KeyError,core.Stop) as error:print(json.dumps({'error':str(error)}));return 2


if __name__=='__main__':raise SystemExit(main())
