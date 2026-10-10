# TextStats

Count logical lines and Unicode whitespace words in complete text or a named UTF-8 file. TextStats runs from a source checkout with Python 3.11+ and the standard library; installation and third-party dependencies are unnecessary. The silent API and named-file command support BOM policy, clean errors and optional JSON output. Named-file line ranges are delivered; stdin remains planned.

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

## Named-file ranges

Select inclusive one-based logical lines with one `--lines START:END` or
`--lines=START:END`. Both compose with JSON/BOM options before or after INPUT:

```bash
python -m textstats --lines 2:3 sample.txt
python -m textstats sample.txt --json --lines=0002:0099
```

Both produce two lines and three words. Endpoints are nonempty positive ASCII
decimals with START <= END. Leading zeros are decimal; there is no endpoint-size
cap. An end past EOF selects available lines, and a start past EOF selects empty
content (`lines=0 words=0`). Only CRLF, CR and LF terminate logical lines; blank
terminated lines count, and a trailing terminator adds no phantom line. Unicode
whitespace still determines words independently.

Complete strict UTF-8 decode occurs before once-only whole-input BOM policy,
line numbering and selection. Selected characters and terminators are preserved;
an interior BOM exposed by selection is retained. Bad bytes after END still fail
with status 1 and no counts. Input bytes remain unchanged. These examples use
both text/JSON and BOM policies:

```bash
python -c "from pathlib import Path; Path('range.txt').write_bytes(b'\xef\xbb\xbfalpha beta\r\n\r\n\xef\xbb\xbf\nlast two')"
python -m textstats --lines 2:2 range.txt
python -m textstats range.txt --json --keep-bom --lines=2:2
python -m textstats --lines 2:99 range.txt
python -m textstats --keep-bom --lines 3:3 range.txt
python -m textstats range.txt --json --lines 99:100
```

The outputs have counts 1/0, 1/0, 3/3, 1/1 and 0/0, respectively. The selected
third line retains its interior BOM as a word. All commands return 0 with empty
stderr; JSON has the same integer fields as whole-input output.

Malformed, missing or repeated ranges return status 2 before file access, with
empty stdout and useful usage/error stderr. Signs, whitespace, non-ASCII digits,
zero, reversed endpoints and extra colons are invalid:

```bash
python -m textstats --lines 0:2 missing.txt
python -m textstats --lines 3:2 missing.txt
python -m textstats --lines=1:2 --lines 2:3 missing.txt
python -m textstats --lines
python -c "from pathlib import Path; Path('bad-range.txt').write_bytes(b'ok\n\xff')"
python -m textstats --json --lines 1:1 bad-range.txt
```

The first four commands return 2; the last returns 1 for strict decoding, empty
stdout and identifying stderr without a traceback. `--` still permits
range-selected dash-prefixed files, and literal `-` is still a named file.
Omitting `--lines` retains whole-input behavior. Public API functions remain
whole-input with unchanged signatures. Future stdin acquisition is deferred;
the normalized selection semantics do not depend on how complete text is acquired.

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

The archive is `dist/textstats-source.zip`, with root `textstats-source/`. Its explicit allowlist contains the five package modules, README, public API guide, disclosure/usage notices and package builder/checker. It excludes credentials, caches, tests, development records, coordinator resources and workflow fixtures. The checker verifies the extracted package import location and 99 real text/JSON/BOM/error module cases with inherited Python import paths removed and user-site packages disabled.

A runnable extraction example for a Bash shell on Unix:

```bash
example_dir=$(mktemp -d)
python -m zipfile -e dist/textstats-source.zip "$example_dir"
(
    cd "$example_dir/textstats-source"
    python -c "from pathlib import Path; Path('sample.txt').write_bytes(b'alpha beta\\r\\nbeta\\rlast two\\n')"
    env -u PYTHONPATH -u PYTHONHOME python -s -m textstats sample.txt
    env -u PYTHONPATH -u PYTHONHOME python -s -m textstats --json sample.txt
)
rm -r "$example_dir"
```

The extracted commands print `lines=3 words=5` and an equivalent JSON object, each with a final newline and status 0. From an extracted root, the package builder/checker commands remain usable; the product-test commands above require a development checkout because test implementations and `tools/check_tests.py` are excluded. No installed console script or release publication is required.

## Development

The accepted [project brief](docs/dev/PROJECT.md), [SPEC](docs/dev/SPEC.md), [PLAN](docs/dev/PLAN.md) and canonical [TASKS](docs/dev/TASKS.md) own scope and execution. Development uses [SDD Manager](SDD-MANAGER.md); see the [AI-assisted development disclosure](AI_DISCLOSURE.md).
