"""Exact-candidate package publisher; dispatch data never becomes shell code."""
import hashlib
import json
import re

FIELDS = {'source', 'tag', 'notes_source', 'notes', 'notes_sha256', 'publish',
          'prerelease', 'make_latest', 'request_id'}


def validate_handoff(data):
    """Validate source-associated curated notes and explicit publication policy."""
    if not isinstance(data, dict) or set(data) != FIELDS:
        raise ValueError('Handoff fields do not match the declared contract')
    if len(json.dumps(data, ensure_ascii=False).encode('utf-8')) > 60000:
        raise ValueError('Handoff exceeds the supported transfer size')
    for key in ('source', 'notes_source'):
        if not isinstance(data[key], str) or not re.fullmatch(r'[0-9a-f]{40}', data[key]):
            raise ValueError('Source must be a full lowercase commit SHA')
    if data['notes_source'] != data['source']:
        raise ValueError('Curated notes belong to a different source')
    for key in ('publish', 'prerelease', 'make_latest'):
        if type(data[key]) is not bool:
            raise ValueError('Publication policies must be Boolean')
    if data['prerelease'] and data['make_latest']:
        raise ValueError('A prerelease cannot be selected as latest')
    if not isinstance(data['tag'], str) or not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?', data['tag']):
        raise ValueError('Tag must be a version tag')
    if not isinstance(data['request_id'], str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', data['request_id']):
        raise ValueError('Invalid request correlation ID')
    notes = data['notes']
    if not isinstance(notes, str) or not notes.strip() or notes.lstrip().startswith('---') or '\x00' in notes:
        raise ValueError('Curated Markdown body is missing or contains control metadata')
    if hashlib.sha256(notes.encode('utf-8')).hexdigest() != data['notes_sha256']:
        raise ValueError('Curated notes digest differs')
    return data


PACKAGE_PATHS = ('assets', 'skills', '.codex-plugin', 'LICENSE', 'plugin.json',
                 'README.md', 'AGENTS.md', 'Greenfield Project Prompt Template.md',
                 'SDD-MANAGER.md', 'AI_DISCLOSURE.md')


def git(root, *args):
    import subprocess
    return subprocess.check_output(['git', '-C', str(root), *args])


def tree_inventory(root, source):
    """Enumerate only shipped committed regular files, retaining blob identities."""
    records = git(root, 'ls-tree', '-rz', source, '--', *PACKAGE_PATHS).split(b'\0')
    files = {}
    for record in filter(None, records):
        metadata, name = record.split(b'\t', 1)
        mode, kind, oid = metadata.decode('ascii').split()
        path = name.decode('utf-8')
        if mode not in ('100644', '100755') or kind != 'blob':
            raise ValueError('Package contains non-regular committed content')
        files[path] = oid
    for selected in PACKAGE_PATHS:
        if not any(path == selected or path.startswith(selected + '/') for path in files):
            raise ValueError('Required package path is absent: ' + selected)
    return files


def inspect_archive(root, source, archive):
    """Verify actual archive paths and every member against the pinned Git tree."""
    import stat
    import zipfile
    from pathlib import PurePosixPath
    expected = tree_inventory(root, source)
    seen = set(); folded = set()
    with zipfile.ZipFile(archive) as zipped:
        for item in zipped.infolist():
            path = PurePosixPath(item.filename)
            if '\\' in item.filename or path.is_absolute() or '..' in path.parts or not item.filename.startswith('sdd-manager/'):
                raise ValueError('Unsafe archive member')
            if item.filename in seen or item.filename.casefold() in folded:
                raise ValueError('Duplicate archive member')
            seen.add(item.filename); folded.add(item.filename.casefold())
            mode = item.external_attr >> 16
            if stat.S_ISLNK(mode): raise ValueError('Archive symlink is forbidden')
            if item.is_dir():
                directory = item.filename[len('sdd-manager/'):].rstrip('/')
                if directory and not any(p.startswith(directory + '/') for p in expected):
                    raise ValueError('Unexpected archive directory')
                continue
            name = item.filename[len('sdd-manager/'):]
            if name not in expected or zipped.read(item) != git(root, 'cat-file', 'blob', expected[name]):
                raise ValueError('Archive member differs from exact candidate')
        actual = {name[len('sdd-manager/'):] for name in seen if not name.endswith('/')}
        if actual != set(expected): raise ValueError('Archive inventory is incomplete')
    return expected


def build_package(root, data, output):
    """Build and verify exact committed bytes before any publisher access."""
    from pathlib import Path
    validate_handoff(data)
    source = data['source']
    if git(root, 'rev-parse', 'HEAD').decode().strip() != source:
        raise ValueError('Candidate checkout differs from selected source')
    manifest = git(root, 'show', source + ':plugin.json')
    if manifest != git(root, 'show', source + ':.codex-plugin/plugin.json'):
        raise ValueError('Legacy manifest differs from canonical manifest')
    if data['tag'] != 'v' + json.loads(manifest)['version']:
        raise ValueError('Tag does not match candidate manifest version')
    tree_inventory(root, source)
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    archive = output / 'sdd-manager.zip'
    git(root, 'archive', '--format=zip', '--prefix=sdd-manager/',
        '--output=' + str(archive.resolve()), source, '--', *PACKAGE_PATHS)
    inspect_archive(root, source, archive)
    if not archive.stat().st_size: raise ValueError('Package archive is empty')
    checksum = output / 'sdd-manager.zip.sha256'
    checksum.write_text(hashlib.sha256(archive.read_bytes()).hexdigest() + '  sdd-manager.zip\n', encoding='ascii')
    return {archive.name: archive, checksum.name: checksum}


def verify_release(api, release, data, files, complete):
    """Read and compare owned fields and every available asset's actual bytes."""
    if (release['tag_name'] != data['tag'] or release['name'] != 'SDD Manager ' + data['tag']
            or release['body'] != data['notes'] or release['prerelease'] != data['prerelease']):
        raise ValueError('Release fields conflict with selected handoff')
    assets = release['assets']
    names = [asset['name'] for asset in assets]
    if len(names) != len(set(names)) or not set(names) <= set(files):
        raise ValueError('Duplicate or foreign release assets')
    for asset in assets:
        raw = files[asset['name']]
        if asset['state'] != 'uploaded' or asset['size'] != len(raw):
            raise ValueError('Incomplete or mismatching release asset')
        if api.download(asset) != raw:
            raise ValueError('Downloaded release bytes differ')
    if complete and set(names) != set(files):
        raise ValueError('Release asset inventory is incomplete')
    return set(names)


def reconcile_release(api, data, files):
    """Reconcile matching drafts without destructive or blind mutation replay."""
    validate_handoff(data)
    if not data['publish']:
        return None
    if api.tag_source(data['tag']) != data['source']:
        raise ValueError('Existing tag differs from selected source')
    before_latest = api.latest_id()
    release = api.find_release(data['tag'])
    if release is not None:
        verify_release(api, release, data, files, complete=not release['draft'])
    else:
        acknowledged = api.create_draft(data)
        if not isinstance(acknowledged, dict):
            raise ValueError('Draft creation acknowledgement is missing')
        release = read_release(api, acknowledged.get('id'))
        verify_release(api, release, data, files, complete=False)
    release_id = release['id']
    if release['draft']:
        for name, raw in files.items():
            # Read before each effect; uncertainty exits, later runs re-read first.
            release = read_release(api, release_id)
            if not release['draft']:
                raise ValueError('Draft changed during upload')
            present = verify_release(api, release, data, files, complete=False)
            if name not in present:
                api.upload(release, name, raw)
        release = read_release(api, release_id)
        verify_release(api, release, data, files, complete=True)
    if release['draft']:
        api.publish(release, data)
    release = read_release(api, release_id)
    if release['draft']:
        raise ValueError('Published release readback is missing or still draft')
    verify_release(api, release, data, files, complete=True)
    if api.tag_source(data['tag']) != data['source']:
        raise ValueError('Published tag source changed')
    expected_latest = release['id'] if data['make_latest'] else before_latest
    if api.latest_id() != expected_latest:
        raise ValueError('Actual latest release differs from requested policy')
    return release


def read_release(api, release_id):
    """Read the acknowledged identity without relying on inventory visibility."""
    if type(release_id) is not int or release_id <= 0:
        raise ValueError('Release acknowledgement has an invalid identity')
    release = api.get_release(release_id)
    if release is None or release.get('id') != release_id:
        raise ValueError('Acknowledged release readback is missing or differs')
    return release


class GitHub:
    """REST boundary with complete inventories and no automatic write retries."""
    def __init__(self, repository, token=None, request=None):
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
            raise ValueError('Invalid repository identity')
        self.repository = repository
        self.base = 'https://api.github.com/repos/' + repository
        self.token = token
        self.request = request or self._request

    def _request(self, method, url, data=None, binary=False, content_type='application/json'):
        import urllib.error
        import urllib.request
        if not url.startswith((self.base + '/', 'https://uploads.github.com/repos/' + self.repository + '/')):
            raise ValueError('Provider request escapes selected repository')
        headers = {'Accept': 'application/octet-stream' if binary else 'application/vnd.github+json',
                   'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'SDD-Manager-publisher'}
        if self.token: headers['Authorization'] = 'Bearer ' + self.token
        if data is not None:
            data = data if isinstance(data, bytes) else json.dumps(data, ensure_ascii=False).encode('utf-8')
            headers['Content-Type'] = content_type
        class SafeRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, hdrs, newurl):
                if not newurl.startswith('https://'):
                    raise ValueError('Insecure asset redirect')
                redirected = super().redirect_request(req, fp, code, msg, hdrs, newurl)
                if redirected is not None: redirected.remove_header('Authorization')
                return redirected
        opener = urllib.request.build_opener(SafeRedirect())
        try:
            with opener.open(urllib.request.Request(url, data=data, headers=headers, method=method), timeout=60) as response:
                raw = response.read()
        except urllib.error.HTTPError as error:
            if method == 'GET' and error.code == 404: return None
            # Never include provider body or credentials in exception evidence.
            raise RuntimeError('GitHub request failed: HTTP ' + str(error.code)) from None
        return raw if binary else (json.loads(raw) if raw else None)

    def pages(self, path):
        result = []
        for page in range(1, 1001):
            separator = '&' if '?' in path else '?'
            items = self.request('GET', path + separator + 'per_page=100&page=' + str(page))
            if not isinstance(items, list): raise ValueError('Incomplete provider inventory')
            result.extend(items)
            if len(items) < 100: return result
        raise ValueError('Provider inventory exceeds supported pagination bound')

    def tag_source(self, tag):
        from urllib.parse import quote
        item = self.request('GET', self.base + '/git/ref/tags/' + quote(tag, safe=''))
        if item is None: return None
        obj = item['object']
        for _ in range(10):
            if obj['type'] == 'commit': return obj['sha']
            if obj['type'] != 'tag': raise ValueError('Tag does not resolve to commit')
            obj = self.request('GET', self.base + '/git/tags/' + obj['sha'])['object']
        raise ValueError('Annotated tag chain exceeds supported bound')

    def latest_id(self):
        release = self.request('GET', self.base + '/releases/latest')
        return None if release is None else release['id']

    def find_release(self, tag):
        matches = [r for r in self.pages(self.base + '/releases') if r['tag_name'] == tag]
        if len(matches) > 1: raise ValueError('Ambiguous provider release identity')
        if not matches: return None
        release = matches[0]
        release['assets'] = self.pages(self.base + '/releases/' + str(release['id']) + '/assets')
        return release

    def create_draft(self, data):
        return self.request('POST', self.base + '/releases', data={
            'tag_name': data['tag'], 'target_commitish': data['source'],
            'name': 'SDD Manager ' + data['tag'], 'body': data['notes'],
            'draft': True, 'prerelease': data['prerelease'], 'make_latest': 'false'})

    def get_release(self, release_id):
        release = self.request('GET', self.base + '/releases/' + str(release_id))
        if release is None: return None
        release['assets'] = self.pages(self.base + '/releases/' + str(release_id) + '/assets')
        return release

    def upload(self, release, name, raw):
        from urllib.parse import quote
        url = ('https://uploads.github.com/repos/' + self.repository + '/releases/'
               + str(release['id']) + '/assets?name=' + quote(name, safe=''))
        return self.request('POST', url, data=raw, content_type='application/octet-stream')

    def download(self, asset):
        raw = self.request('GET', self.base + '/releases/assets/' + str(asset['id']), binary=True)
        if not isinstance(raw, bytes): raise ValueError('Asset download is missing')
        return raw

    def publish(self, release, data):
        return self.request('PATCH', self.base + '/releases/' + str(release['id']), data={
            'draft': False, 'prerelease': data['prerelease'],
            'make_latest': 'true' if data['make_latest'] else 'false'})


def read_event(path):
    from pathlib import Path
    event = json.loads(Path(path).read_text(encoding='utf-8'))
    raw = event['inputs']['handoff']
    if not isinstance(raw, str) or len(raw.encode('utf-8')) > 60000:
        raise ValueError('Invalid structured dispatch handoff')
    return validate_handoff(json.loads(raw))


def main():
    import argparse
    import os
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event', required=True)
    parser.add_argument('--root', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--build-only', action='store_true')
    parser.add_argument('--expected-sha256')
    args = parser.parse_args()
    data = read_event(args.event)
    root = Path(args.root)
    paths = build_package(root, data, Path(args.output))
    archive_hash = hashlib.sha256(paths['sdd-manager.zip'].read_bytes()).hexdigest()
    if args.expected_sha256 and archive_hash != args.expected_sha256:
        raise ValueError('Publisher rebuild differs from verified build job')
    result = None if args.build_only else reconcile_release(
        GitHub(os.environ['GITHUB_REPOSITORY'], os.environ.get('GITHUB_TOKEN')),
        data, {name: path.read_bytes() for name, path in paths.items()})
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as outputs:
            outputs.write('archive_sha256=' + archive_hash + '\n')
    observation = {'source': data['source'], 'request_id': data['request_id'],
                   'workflow_source': os.environ.get('GITHUB_SHA'),
                   'run_id': os.environ.get('GITHUB_RUN_ID'),
                   'published': result is not None,
                   'release_id': None if result is None else result['id'],
                   'assets': {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in paths.items()}}
    (Path(args.output) / 'release-observation.json').write_text(json.dumps(observation, indent=2) + '\n')
    print(json.dumps(observation, sort_keys=True))


if __name__ == '__main__':
    main()
