"""Read-only checks of the final evidence integration, never a merge driver."""
from pathlib import Path
import argparse
import json
import sys
sys.path.insert(0, str(Path(__file__).parent))
import core


def verify(root, commit, product_tip, evidence_tip, campaign_path):
    """Verify exact two parents, evidence-only delta and retained final report.

    Publication, assessment authenticity and source pins are independently checked.
    This helper only examines actual Git objects; it never creates or repairs them.
    """
    root = Path(root).resolve()
    core.relative(root, campaign_path)
    if not campaign_path.startswith('docs/dev/reviews/') or campaign_path.endswith('/'):
        raise ValueError('campaign path required')
    resolved = []
    for ref in (commit, product_tip, evidence_tip):
        if not isinstance(ref, str) or len(ref) != 40 or any(c not in '0123456789abcdef' for c in ref):
            raise ValueError('full object identity required')
        resolved.append(core.git(root, 'rev-parse', '--verify', ref + '^{commit}').stdout.strip())
    actual, product, evidence = resolved
    parents = core.git(root, 'show', '-s', '--format=%P', actual).stdout.strip().split()
    if parents != [product, evidence]:
        raise ValueError('unexpected merge parents')
    paths = core.git(root, 'diff', '--name-only', '-z', product, actual, binary=True).stdout.split(b'\0')
    names = [p.decode('utf-8') for p in paths if p]
    if not names or any(not p.startswith(campaign_path + '/') for p in names):
        raise ValueError('integration changes product or foreign evidence')
    report = core.git(root, 'cat-file', '-e', actual + ':' + campaign_path + '/DIAGNOSTIC-REPORT.md', required=False)
    if report.returncode:
        raise ValueError('final diagnostic report missing')
    return {'commit': actual, 'parents': parents, 'changed_paths': names,
            'product_preserved': True, 'agent_behavior_assessed': False,
            'publication_verified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('root', 'commit', 'product-tip', 'evidence-tip', 'campaign-path'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.root, args.commit, args.product_tip, args.evidence_tip, args.campaign_path)))
        return 0
    except (ValueError, core.Stop, OSError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
