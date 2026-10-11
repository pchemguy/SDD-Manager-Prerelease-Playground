"""Discover independent nonempty product suites and propagate test failures.

Execute from any cwd with the selected Python runtime. Workflow fixtures are
excluded: only tests/unit and tests/integration are product collection roots.
"""

import sys
import unittest
from pathlib import Path


def main() -> int:
    """Report actual collection counts, reject empty suites and run both suites."""
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))
    suites = []
    for name in ('unit', 'integration'):
        suite = unittest.TestLoader().discover(str(root / 'tests' / name), top_level_dir=str(root))
        count = suite.countTestCases()
        print(f'{name}: {count} tests', flush=True)
        suites.append((name, count, suite))
    if any(count == 0 for _, count, _ in suites):
        print('empty product suite: unit and integration must each collect tests', file=sys.stderr)
        return 1
    success = True
    for _, _, suite in suites:
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        success = result.wasSuccessful() and success
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
