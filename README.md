# TextStats

Count logical lines and Unicode whitespace words in complete text or a named UTF-8 file. TextStats runs from a source checkout with Python 3.11+ and the standard library; installation and third-party dependencies are unnecessary. The silent API and named-file command support BOM policy, clean errors and optional JSON output. Stdin and line ranges remain planned.

## Quick start

Run from the repository root:

```bash
python -c "from pathlib import Path; Path('sample.txt').write_bytes(b'alpha beta\r\nbeta\rlast two\n')"
python -m textstats sample.txt
python -m textstats --help
```

The counting command prints `lines=3 words=5` followed by a newline, with status 0 and empty stderr. Help returns 0 and explains the input and options without opening a file. Inputs stay unchanged.

```bash
python -c "from pathlib import Path; Path('bom.txt').write_bytes(b'\xef\xbb\xbf')"
python -m textstats bom.txt
python -m textstats --keep-bom bom.txt
python -c "from pathlib import Path; Path('-sample').write_bytes(b'alpha beta\n')"
python -m textstats -- -sample
```

BOM-only input produces `lines=0 words=0` by default and `lines=1 words=1` with `--keep-bom`. The dash-prefixed file produces `lines=1 words=2`. Options can appear before or after INPUT; `--` ends option parsing. At this phase a literal `-` is a filename. Exactly one file is required.

Missing, unreadable, read-failing or invalid UTF-8 input returns status 1 with identifying input/cause stderr, no traceback and empty stdout. Missing/extra inputs or unknown options return status 2 with useful usage/error stderr and empty stdout. Invocation validation precedes file access. No partial statistics are emitted.

Add `--json` for one JSON object plus a newline containing only integer `lines` and `words` fields. Counts and errors follow the same contracts as the default text output; key order and spacing are unrestricted. Both options compose before or after INPUT:

```bash
python -m textstats --json sample.txt
python -m textstats bom.txt --keep-bom --json
```

These produce counts equivalent to `{"lines": 3, "words": 5}` and `{"lines": 1, "words": 1}`, respectively. Text remains the default.

## Python API

```python
from textstats import TextStats, count_text, count_file

assert count_text("alpha beta\r\nbeta\rlast two\n") == TextStats(3, 5)
assert count_file("sample.txt") == TextStats(3, 5)
assert count_text("\ufeff") == TextStats(0, 0)
assert count_text("\ufeff", strip_bom=False) == TextStats(1, 1)
```

All three exports are documented in the [public API and module reference](docs/public-api.md), including line/word semantics, constructor validation, strict decoding, exceptions and handle ownership. API calls write nothing to stdout or stderr.

## Product checks

Run from the repository root with the same Python executable:

```bash
python tools/check_tests.py
python -m unittest discover -s tests/unit -t . -v
python -m unittest discover -s tests/integration -t . -v
```

The runner independently reports unit and integration collection counts, rejects an empty suite and propagates test failures. Workflow fixtures do not count as product tests. Python 3.12.14 is the currently verified runtime; other supported versions have not been exercised here.

## Distribution boundary

Build and check the source archive from the checkout root:

```bash
python tools/package_source.py
python tools/check_distribution.py
```

The archive is `dist/textstats-source.zip`, with root `textstats-source/`. Its explicit allowlist contains the five package modules, README, public API guide, disclosure/usage notices and package builder/checker. It excludes credentials, caches, tests, development records, coordinator resources and workflow fixtures. The checker verifies the extracted package import location and 36 real module cases with inherited Python import paths removed and user-site packages disabled.

A runnable extraction example for a Bash shell on Unix:

```bash
example_dir=$(mktemp -d)
python -m zipfile -e dist/textstats-source.zip "$example_dir"
(
    cd "$example_dir/textstats-source"
    python -c "from pathlib import Path; Path('sample.txt').write_bytes(b'alpha beta\\r\\nbeta\\rlast two\\n')"
    env -u PYTHONPATH -u PYTHONHOME python -s -m textstats sample.txt
)
rm -r "$example_dir"
```

The extracted command prints `lines=3 words=5` and returns 0. From an extracted root, the package builder/checker commands remain usable; the product-test commands above require a development checkout because test implementations and `tools/check_tests.py` are excluded. No installed console script or release publication is required.

## Development

The accepted [project brief](docs/dev/PROJECT.md), [SPEC](docs/dev/SPEC.md), [PLAN](docs/dev/PLAN.md) and canonical [TASKS](docs/dev/TASKS.md) own scope and execution. Development uses [SDD Manager](SDD-MANAGER.md); see the [AI-assisted development disclosure](AI_DISCLOSURE.md).
