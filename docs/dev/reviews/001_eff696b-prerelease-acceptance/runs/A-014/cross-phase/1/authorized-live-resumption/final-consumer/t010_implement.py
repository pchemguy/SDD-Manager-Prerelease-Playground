from pathlib import Path
path=Path('textstats/cli.py')
text=path.read_text().replace('Named-file CLI parsing and exact text presentation.', 'Named-file CLI parsing, exact text and integer-only JSON presentation.',1).replace('import argparse\n','import argparse\nimport json\n',1)
text=text.replace('Parse one named file and emit its completed counts.', 'Parse one named file and emit completed counts as text or JSON.',1)
text=text.replace("    parser.add_argument('--keep-bom'", "    parser.add_argument('--json', action='store_true', help='emit one JSON object with integer lines and words')\n    parser.add_argument('--keep-bom'",1)
text=text.replace("    print(f'lines={stats.lines} words={stats.words}')", "    if args.json:\n        print(json.dumps({'lines': stats.lines, 'words': stats.words}))\n    else:\n        print(f'lines={stats.lines} words={stats.words}')",1)
path.write_text(text)
path=Path('README.md')
text=path.read_text().replace('JSON, stdin and line ranges remain planned.', 'Named-file JSON output is also delivered; stdin and line ranges remain planned.',1)
anchor='## Python API\n'
insert='''## JSON output

Use `--json` to emit one object with exactly integer `lines` and `words` fields, followed by a newline. Counts match the default text format and the API. The option composes with `--keep-bom`, before or after INPUT:

```bash
python -m textstats --json sample.txt
python -m textstats sample.txt --json
python -m textstats --json --keep-bom bom.txt
```

The sample produces `{"lines": 3, "words": 5}`; retained BOM-only input produces `{"lines": 1, "words": 1}`. JSON key order and spacing are unrestricted. Text stays the default, and input/usage failures retain their statuses and empty stdout. Stdin remains planned; literal `-` is still a named file.

'''
text=text.replace(anchor,insert+anchor,1)
text=text.replace('The checker verifies the extracted package import location and 36 real module cases with inherited Python import paths removed and user-site packages disabled.', 'The checker verifies the extracted package import location and 36 retained named-file text/help/error module cases with inherited Python import paths removed and user-site packages disabled. Dedicated extracted-source JSON acceptance is planned in T-011; this T-010 checkpoint verifies JSON from the checkout.',1)
path.write_text(text)
path=Path('docs/public-api.md')
text=path.read_text().replace('Use `python -m textstats [--keep-bom] INPUT`', 'Use `python -m textstats [--json] [--keep-bom] INPUT`',1)
text=text.replace('In Phase 1, literal `-` is a named file.', 'Until stdin delivery, literal `-` is a named file.',1)
text=text.replace('| Count success | 0 | Exactly `lines=<N> words=<N>` plus newline | Empty |', '| Default text success | 0 | Exactly `lines=<N> words=<N>` plus newline | Empty |\n| JSON success (`--json`) | 0 | One object with only integer `lines`/`words` and a final newline | Empty |',1)
text=text.replace('JSON, stdin and ranges are future work.', 'The `--json` option composes with `--keep-bom` and retains the same counts/statuses. JSON key order and spacing are unrestricted; booleans and extra fields are excluded. Stdin and ranges are future work.',1)
text=text.replace('expected failure translation and exact text rendering.', 'expected failure translation and text/JSON rendering.',1)
path.write_text(text)
path=Path('AGENTS.md')
text=path.read_text()+'''\n## Current selected checkpoint\n\nThe current T-009 through T-010 request supersedes historical Phase-1-only stops. Phase 1 was reviewed, integrated into local main and published to the explicitly authorized trial main ref before Phase 2 activation. T-010 adds named-file `--json` with retained text/BOM/error/API behavior. Current fork hosted tracking is explicitly disabled; historical issue identities are protected and not maintained here. Stop after T-010 on `phase/2-json-and-stdin`; T-011 and later tasks, stdin/range/release work and Phase 2 main integration are unselected. Source-distribution checker currently covers 36 retained text/help/error cases; extracted-source JSON acceptance belongs to T-011.\n'''
path.write_text(text)
