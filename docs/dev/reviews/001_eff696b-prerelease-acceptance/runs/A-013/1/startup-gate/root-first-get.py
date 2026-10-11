"""GET-only final hosted snapshot; credential and response bodies stay in memory."""
import datetime
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path('/workspace/scratch/46b31bb4dff6')
STORE = ROOT / 'SDD-Manager-Prerelease-Playground'
assert subprocess.check_output(['git', 'check-ignore', 'gh.tkn'], cwd=STORE, text=True).strip() == 'gh.tkn'
assert not subprocess.check_output(['git', 'ls-files', '--', 'gh.tkn'], cwd=STORE)
access = (STORE / 'gh.tkn').read_text().strip()
records = []


def get(route):
    request = urllib.request.Request(
        'https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground/' + route,
        headers={'Authorization': 'Bearer ' + access, 'Accept': 'application/vnd.github+json',
                 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'campaign-037-read-only-assessor'},
        method='GET')
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            obj = json.loads(response.read())
            records.append({'route': route, 'method': 'GET', 'status': response.status,
                            'utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
    except urllib.error.HTTPError as error:
        records.append({'route': route, 'method': 'GET', 'status': error.code})
        raise RuntimeError('Hosted GET failed; response body excluded') from None
    time.sleep(1)
    return obj


def listing(route):
    values = []
    page = 1
    while True:
        batch = get(route + ('&' if '?' in route else '?') + f'per_page=100&page={page}')
        assert isinstance(batch, list)
        values.extend(batch)
        if len(batch) < 100:
            return values
        page += 1


def digest(text):
    return hashlib.sha256((text or '').encode()).hexdigest()


def issue(obj):
    return {'number': obj['number'], 'id': obj['id'], 'title': obj['title'],
            'state': obj['state'], 'state_reason': obj.get('state_reason'),
            'milestone': obj['milestone']['number'] if obj.get('milestone') else None,
            'labels': sorted(label['name'] for label in obj.get('labels', [])),
            'body_sha256': digest(obj.get('body'))}


issues = [issue(obj) for obj in listing('issues?state=all') if 'pull_request' not in obj]
milestones = [{'number': obj['number'], 'id': obj['id'], 'title': obj['title'],
               'state': obj['state'], 'open_issues': obj['open_issues'],
               'closed_issues': obj['closed_issues'],
               'body_sha256': digest(obj.get('description'))}
              for obj in listing('milestones?state=all')]
labels = [{'id': obj['id'], 'name': obj['name'], 'color': obj['color'],
           'description_sha256': digest(obj.get('description'))}
          for obj in listing('labels')]
comments = {str(number): [{'id': obj['id'], 'body_sha256': digest(obj['body'])}
                         for obj in listing(f'issues/{number}/comments')]
            for number in [1, 2, *range(19, 26)]}
snapshot = {'evidence_class': 'Fresh authenticated paginated GET-only hosted snapshot',
            'issues': issues, 'milestones': milestones, 'labels': labels,
            'comments': comments, 'operations': records,
            'coverage_limit': 'No write or full historical chronology asserted; bodies excluded, hashes retained.'}
out = ROOT / '037-a013-start-hosted-readback.json'
out.write_text(json.dumps(snapshot, indent=2) + '\n')
print('Final safe GET snapshot:', len(issues), 'issues,', len(milestones), 'milestones,', len(records), 'GET operations')
