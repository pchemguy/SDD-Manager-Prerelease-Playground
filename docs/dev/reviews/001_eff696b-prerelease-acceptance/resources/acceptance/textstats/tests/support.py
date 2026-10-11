"""Disposable Git fixtures and subprocess assertions for helper sensitivity tests.

Sandbox owns temporary repositories/local remotes and cleanup; no hosted writes
or consumer workflow acceptance occur here. Inputs and checkpoints are synthetic."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
SOURCE = Path(__file__).resolve().parents[3]

def git(root, *args, check=True):
    return subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True, check=check)

class Sandbox(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote = self.root / 'remote.git'
        git(self.root, 'init', '--bare', str(self.remote))
        self.repo = self.root / 'consumer'
        git(self.root, 'init', '-b', 'main', str(self.repo))
        git(self.repo, 'config', 'user.name', 'Fixture')
        git(self.repo, 'config', 'user.email', 'fixture@example.invalid')
        (self.repo / 'owned.txt').write_text('baseline\n')
        git(self.repo, 'add', 'owned.txt')
        git(self.repo, 'commit', '-m', 'baseline')
        git(self.repo, 'remote', 'add', 'origin', str(self.remote))
        git(self.repo, 'push', '-u', 'origin', 'main')
        self.inputs = {'schema_version': 1, 'test_repository': str(self.remote), 'local_checkout': str(self.repo), 'profile': 'local-only'}
        self.state = {'schema_version': 1, 'run_id': '001_fixture', 'phase': 'P0', 'case_id': None, 'attempt': 1, 'role': 'coordinator', 'last_completed_action': 'fixture', 'pending_operation': None, 'next_action': 'inspect', 'checkpoint_refs': {}, 'evidence_paths': []}
        self.seq = 0

    def invoke(self, name, inputs=None, state=None, extra=()):
        self.seq += 1
        inp = self.root / ('inputs%d.json' % self.seq)
        out = self.root / ('output%d.json' % self.seq)
        inp.write_text(json.dumps(self.inputs if inputs is None else inputs))
        argv = [sys.executable, str(SCRIPTS / (name + '.py')), '--inputs', str(inp), '--output', str(out)]
        if state is not None:
            path = self.root / ('state%d.json' % self.seq)
            path.write_text(json.dumps(state))
            argv += ['--run-state', str(path)]
        argv += list(map(str, extra))
        proc = subprocess.run(argv, capture_output=True, text=True)
        data = json.loads(out.read_text()) if out.exists() else None
        return proc, data, out

    def ok(self, result):
        proc, data, out = result
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        self.assertIsInstance(data, dict)
        return data, out
