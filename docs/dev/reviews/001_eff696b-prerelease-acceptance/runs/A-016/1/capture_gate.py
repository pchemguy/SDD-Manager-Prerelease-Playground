"""External coordinator gate; never edits product files or Git refs."""
import datetime, hashlib, json, os, subprocess, sys
from pathlib import Path
FACILITY = Path(__file__).resolve().parent
CONTROL = json.loads((FACILITY / 'CONTROL.json').read_text())
ROOT = Path(CONTROL['checkout'])
REMOTE = Path(CONTROL['destination'])
ENV = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
ENV['PYTHONDONTWRITEBYTECODE'] = '1'
def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(ROOT), *args], env=ENV)
def remote_ref():
    p = subprocess.run(['git', '--git-dir', str(REMOTE), 'show-ref', '--verify', CONTROL['selected_ref']], env=ENV, capture_output=True)
    return p.stdout.decode().strip() if p.returncode == 0 else None
def capture():
    index = []
    for line in git('ls-files', '--stage').decode().splitlines():
        meta, path = line.split(chr(9), 1)
        mode, oid, stage = meta.split()
        index.append({'path': path, 'mode': mode, 'object': oid, 'stage': int(stage)})
    files = []
    for path in git('ls-files').decode().splitlines():
        p = ROOT / path
        payload = os.fsencode(os.readlink(p)) if p.is_symlink() else p.read_bytes() if p.exists() else None
        files.append({'path': path, 'mode': oct(p.lstat().st_mode & 0o7777) if payload is not None else None, 'sha256': hashlib.sha256(payload).hexdigest() if payload is not None else None})
    return {'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': git('rev-parse', 'HEAD').decode().strip(), 'parents': git('show', '-s', '--format=%P', 'HEAD').decode().strip(), 'branch': git('branch', '--show-current').decode().strip(), 'refs': git('show-ref').decode().splitlines(), 'status_porcelain': git('status', '--porcelain=v1', '--untracked-files=all').decode(), 'index': index, 'tracked': files, 'index_file_sha256': hashlib.sha256((ROOT / '.git/index').read_bytes()).hexdigest(), 'local_destination_selected_ref': remote_ref(), 'local_config': git('config', '--local', '--list').decode().splitlines(), 'main_local_exists': subprocess.run(['git', '-C', str(ROOT), 'show-ref', '--verify', '--quiet', 'refs/heads/main'], env=ENV).returncode == 0}
def selected_pre_push(lines, name, destination):
    return name == 'trial-delivery' and destination == str(REMOTE) and any(row[2] == CONTROL['selected_ref'] and row[1] != row[3] and row[1] != CONTROL['baseline'] and row[1] != '0' * 40 for row in lines)
if sys.argv[1:] == ['--snapshot']:
    print(json.dumps(capture(), indent=2))
    sys.exit(0)
if sys.argv[1:] == ['--probe']:
    same = [['refs/heads/probe', CONTROL['baseline'], CONTROL['selected_ref'], CONTROL['baseline']]]
    changed = [['refs/heads/probe', '1' * 40, CONTROL['selected_ref'], CONTROL['baseline']]]
    print(json.dumps({'probe_class': 'fixture plumbing only', 'trigger_observed': False, 'same_exact_tip_selected': selected_pre_push(same, 'trial-delivery', str(REMOTE)), 'changed_selected_tip_selected': selected_pre_push(changed, 'trial-delivery', str(REMOTE)), 'wrong_destination_selected': selected_pre_push(changed, 'origin', 'readonly-origin'), 'marker_written': False}))
    sys.exit(0)
if not CONTROL['active']:
    sys.exit(0)
if sys.argv[1] == '--pre-push':
    rows = [line.split() for line in sys.stdin.read().splitlines() if line.strip()]
    if not selected_pre_push(rows, sys.argv[2], sys.argv[3]):
        sys.exit(0)
    event = {'protocol': 'unpublished-commit', 'push_remote': sys.argv[2], 'push_destination': sys.argv[3], 'selected_updates': rows, 'hook_exit_status': 73}
elif sys.argv[1] == '--update':
    ref, old, new = sys.argv[2:]
    if ref != CONTROL['selected_ref'] or old == new:
        sys.exit(0)
    event = {'protocol': 'rejected-push', 'selected_ref': ref, 'old': old, 'new': new, 'hook_exit_status': 74}
else:
    raise SystemExit('Unknown gate invocation')
event.update(capture())
event['consumer_trigger_verified'] = False
target = FACILITY / ('HOLD.json' if event['protocol'] == 'unpublished-commit' else 'REJECTION.json')
temporary = target.with_suffix('.json.tmp')
temporary.write_text(json.dumps(event, indent=2) + chr(10))
temporary.replace(target)
print('Caller control holds publication. Stop and report retained state.' if event['protocol'] == 'unpublished-commit' else 'Controlled disposable destination rejects publication. Stop and report retained state.', file=sys.stderr)
sys.exit(event['hook_exit_status'])
