"""Playground-only controlled fault wrapper; ordinary publisher remains sole owner."""
import importlib.util
import json
import os
from pathlib import Path

spec = importlib.util.spec_from_file_location('publisher', Path(__file__).with_name('release.py'))
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)
data = publisher.read_event(os.environ['GITHUB_EVENT_PATH'])
if data['request_id'].startswith('037-cp014-partial-'):
    original_upload = publisher.GitHub.upload
    def upload_then_interrupt(self, release, name, raw):
        result = original_upload(self, release, name, raw)
        print(json.dumps({'controlled_injection': 'stop after acknowledged real provider upload', 'release_id': release['id'], 'asset_id': result['id'], 'asset_name': name}), flush=True)
        raise RuntimeError('Campaign 037 controlled post-upload response suppression; next run must reconcile actual effect')
    publisher.GitHub.upload = upload_then_interrupt
publisher.main()
