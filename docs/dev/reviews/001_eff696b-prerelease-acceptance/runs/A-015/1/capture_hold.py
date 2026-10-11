"""Caller-owned cooperative gate; no product edits or commit synthesis."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/workspace/scratch/46b31bb4dff6/037-a015-staged')
FACILITY = Path('/workspace/scratch/46b31bb4dff6/037-a015-setup')

def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(ROOT), *args])

def capture():
    index = []
    for item in git('ls-files', '--stage', '-z').split(b'\0'):
        if not item:
            continue
        meta, path = item.split(b'\t', 1)
        mode, oid, stage = meta.decode('ascii').split()
        index.append({'path': os.fsdecode(path), 'mode': mode, 'object': oid, 'stage': int(stage)})
    tracked = []
    for raw in git('ls-files', '-z').split(b'\0'):
        if not raw:
            continue
        path = ROOT / os.fsdecode(raw)
        if path.is_symlink():
            payload = os.fsencode(os.readlink(path))
        elif path.exists():
            payload = path.read_bytes()
        else:
            payload = None
        tracked.append({'path': os.fsdecode(raw), 'mode': oct(path.lstat().st_mode & 0o7777) if path.exists() or path.is_symlink() else None, 'sha256': hashlib.sha256(payload).hexdigest() if payload is not None else None})
    return {'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': git('rev-parse', 'HEAD').decode().strip(), 'branch': git('branch', '--show-current').decode().strip(), 'refs': git('show-ref').decode().splitlines(), 'status_porcelain': git('status', '--porcelain=v1', '--untracked-files=all').decode(), 'index': index, 'tracked': tracked, 'index_file_sha256': hashlib.sha256((ROOT / '.git/index').read_bytes()).hexdigest()}

if __name__ == '__main__':
    if sys.argv[1:] == ['--hook']:
        control = json.loads((FACILITY / 'CONTROL.json').read_text())
        if not control['hold_active']:
            sys.exit(0)
        state = capture()
        state.update({'facility': 'A015 native Git pre-commit cooperative hold', 'hook_exit_status': 73, 'product_commit_created': False})
        target = FACILITY / 'HOLD.json'
        temporary = target.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(state, indent=2) + '\n')
        temporary.replace(target)
        print('Caller control holds this operation. Stop and report retained state.', file=sys.stderr)
        sys.exit(73)
    print(json.dumps(capture(), indent=2))
