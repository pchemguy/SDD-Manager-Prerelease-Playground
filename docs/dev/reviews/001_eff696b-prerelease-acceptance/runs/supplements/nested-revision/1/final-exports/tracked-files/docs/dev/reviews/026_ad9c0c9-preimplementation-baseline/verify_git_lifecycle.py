"""Exercise preparation ancestry/publication with ordinary Git in a temp repo.

This verifies the Git mechanics used by the instructions, not agent compliance.
"""

from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


def git(root, *args, check=True):
    return subprocess.run(
        ['git', '-C', str(root), *args], check=check,
        capture_output=True, text=True,
    )


def run():
    with TemporaryDirectory(prefix='sdd-preparation-') as directory:
        root = Path(directory)
        remote = root / 'remote.git'
        work = root / 'work'
        subprocess.run(['git', 'init', '--bare', str(remote)], check=True,
                       capture_output=True)
        subprocess.run(['git', 'init', '-b', 'trunk', str(work)], check=True,
                       capture_output=True)
        git(work, 'config', 'user.name', 'Verification')
        git(work, 'config', 'user.email', 'verification@example.invalid')
        (work / 'README.md').write_text('Fixture\n')
        git(work, 'add', 'README.md')
        git(work, 'commit', '-m', 'baseline')
        git(work, 'remote', 'add', 'origin', str(remote))
        git(work, 'push', '-u', 'origin', 'trunk')
        git(remote, 'symbolic-ref', 'HEAD', 'refs/heads/trunk')
        git(work, 'remote', 'set-head', 'origin', '-a')
        assert git(work, 'symbolic-ref', 'refs/remotes/origin/HEAD').stdout.strip() == 'refs/remotes/origin/trunk'

        git(work, 'switch', '-c', 'design-docs/main')
        (work / 'SPEC.md').write_text('Accepted preparation\n')
        git(work, 'add', 'SPEC.md')
        git(work, 'commit', '-m', 'project preparation')
        preparation = git(work, 'rev-parse', 'HEAD').stdout.strip()
        git(work, 'push', '-u', 'origin', 'design-docs/main')
        assert git(work, 'merge-base', '--is-ancestor', preparation, 'origin/trunk', check=False).returncode == 1
        assert not git(work, 'branch', '--list', 'phase/*').stdout.strip()
        print('PASS: preparation-only checkpoint leaves default and phase branches unchanged')

        git(work, 'switch', 'trunk')
        target = git(work, 'rev-parse', 'HEAD').stdout.strip()
        git(work, 'merge', '--no-ff', '--no-commit', preparation)
        git(work, 'diff', '--cached', '--check')
        git(work, 'commit', '-m', 'merge accepted preparation')
        merge = git(work, 'rev-parse', 'HEAD').stdout.strip()
        parents = git(work, 'rev-list', '--parents', '-n', '1', merge).stdout.split()[1:]
        assert parents == [target, preparation]
        assert git(work, 'merge-base', '--is-ancestor', preparation, 'origin/trunk', check=False).returncode == 1
        assert not git(work, 'branch', '--list', 'phase/*').stdout.strip()
        print('PASS: local two-parent merge alone does not satisfy publication')

        git(work, 'push', 'origin', 'trunk')
        git(work, 'merge-base', '--is-ancestor', preparation, 'origin/trunk')
        assert git(work, 'rev-parse', 'origin/trunk').stdout.strip() == merge
        git(work, 'switch', '-c', 'phase/1-mvp', 'origin/trunk')
        assert git(work, 'rev-parse', 'HEAD').stdout.strip() == merge
        print('PASS: implementation starts from published preparation on nonstandard default trunk')

        git(work, 'switch', '-c', 'revision/001-fixture', 'origin/trunk')
        (work / 'REVISION-PLAN.md').write_text('Campaign plan\n')
        git(work, 'add', 'REVISION-PLAN.md')
        git(work, 'commit', '-m', 'campaign plan')
        assert git(work, 'cat-file', '-e', 'origin/trunk:REVISION-PLAN.md', check=False).returncode != 0
        print('PASS: campaign plan remains on revision without preliminary default merge')


if __name__ == '__main__':
    run()
