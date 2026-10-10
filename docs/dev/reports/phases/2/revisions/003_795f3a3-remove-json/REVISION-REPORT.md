# JSON-removal checkpoint amendment

## Objective and scope

Remove JSON output while retaining exact text, counting, BOM policy, complete strict decoding, resource ownership, unchanged API and named-file ranges. Removed options fail before acquisition; a literal `--json` filename works after `--`. Stdin/final T-013–T-017 remain paused; no default integration or release.

Campaign: 003_795f3a3-remove-json. Full baseline: `795f3a3542c9981f8d43c8e182876f3efa5b5f16`. Working branch: `revision/003_795f3a3-remove-json`; paused target: `phase/2-json-and-stdin`, origin `pchemguy/SDD-Manager-Prerelease-Playground`. Main remains `fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`. Pinned plugin: `ea515f5624c8a34cc4572731a2590223a5eb27f4`. Accepted external assessment: `037-a011-fresh-consumer-observations.json`.

## Preparation and affected ownership

PROJECT/design/SPEC/PLAN/layout/TASKS describe text-only current scope. R-009, milestone 2.1 and T-010–T-012 retain retired historical identities without replacement or new checked completion. Future stdin/final dependencies use the retained Phase 1/range checkpoint. T-018 pure semantics remain valid; T-019–T-024 retained text/range completion passes the current checks below, without replaying task execution. Adjacent affected owner QC is appended, preserving original evidence. Closed feature and phase reports stay unchanged.

## Review and implemented result

First candidate acceptance was withheld for stale current QC hashes and obsolete alternate-output/agreement wording. Exact first eleven artifact bytes were preserved externally; the correction retains historical gate prose separately. Corrected preparation was accepted through coordinator `3b7e7abef970ca6132aa4fe34f075d550f0ab0ba`, committed as campaign opening `636b46d8daf1455c940c98f4d535c9936c0f1733`, immediately pushed to the authorized revision branch and exactly read back before production consumption.

Production removes only the JSON import, option registration and serialization branch from `textstats/cli.py`, retaining the shared exact text renderer. The parser still validates before acquisition; core/I/O/API/entry/builder interfaces are unchanged. README/public guide/help and maintained root orientation agree with the reduced scope. Existing JSON callers receive a breaking usage error; there is no alias or alternate JSON path.

Separate coherent code review inspected parser/controller, complete acquisition and decode, pure normalize/select/count boundaries, public facade, resource/error translation, mixed tests, documentation and isolated distribution checker against retained contracts. No unresolved code/contract blocker was found. Mixed JSON tests preserve complete-decode/read-failure/owned-close evidence in text. Range matrices retain both spellings, both BOM policies, all retained option permutations/INPUT placements, huge/leading-zero endpoints, EOF/blank/mixed/Unicode/exposed-BOM and byte-preservation anchors. Extraction retains allowlist/import provenance and the silent unchanged API/signature probe. Checker mutations reject broken text, ignored ranges, second BOM normalization and silently accepted removed options.

## Actual verification

All commands use `PYTHONDONTWRITEBYTECODE=1 python -B` from the product root, with inherited child bytecode suppression, on Python 3.12.14.

| Check | Observed result |
| --- | --- |
| Two focused removal tests before production | Initial run: two assertion failures and three mock-serialization errors. Corrected realistic doubles, then same two tests: five intended behavioral failures, no errors. JSON remained accepted/acquired input. |
| `python -B -m unittest tests.unit.test_cli tests.integration.test_cli -v` | 28 tests pass after removal. |
| `python -B tools/check_tests.py` | Independent nonempty 31 unit / 28 integration tests pass, no skips/warnings. |
| `python -B -m unittest tests.integration.test_cli.RangeModuleTests -v` | Five tests pass after removing empty-list refactor remnants. |
| `python -B tools/package_source.py` and `python -B tools/check_distribution.py` | Allowlisted archive builds; 241 real isolated extracted module cases pass, plus silent API/signature probe. |
| All README/public guide runnable fences in temporary checkout | Ten fences execute; exact count/help/error/test/extraction/API outputs inspected. Invalid range examples intentionally produce four usage diagnostics and final strict-decode status 1; no unexpected failure. |
| Scoped current documents/links/task structure/hashes and full delta | Twenty current QC source hashes match before execution; whitespace/local links/16 checked active/five pending/three retired identities pass; protected resources, closed packages, core/I/O/API/entry/builder/bootstrap paths unchanged. |

Retained T-006/T-007 and T-018–T-024 acceptance is verified at this amended checkpoint; original historical reports/results remain preserved. T-010–T-012/2.1 are retired historical work, with no newly verified JSON completion. All five pending stdin/final tasks and whole Phase 2 remain paused. Broader supported runtimes/platforms are unverified; no performance/streaming/release claim is made.

## Publication, hosted disposition and integration boundary

Implementation/report candidate awaits concrete delegated conclusion review before its verified non-task commit/publication and eligible explicit two-parent paused-phase integration. Hosted read-only discovery resolved every exact stable task marker and parent association. A concrete managed-field reconciliation plan covers retired JSON and affected live briefs, phase-label/milestone scope; it preserves historical closed/completed reasons and pending open tasks. No issue is reopened solely because JSON was removed and no task is closed solely because its checkbox was retired. Writes/readbacks follow implementation publication. Unrelated issue2 body/label/comments and milestone1 content remain protected.

Raw actual commands, separate stdout/stderr/status, first candidate bytes, acceptance provenance, original failures and hosted original operations/readbacks are retained in the externally required `037-a012-consumer-observations` seal and sidecars. Initial orientation tool captures predate the separate-stream runner and some were truncated; they are not represented as complete raw separate-channel captures. One wrong manifest key and one shell quote parse failure were corrected and remain original failures. No `/pyenv` or coordinator resource change occurs.

## TODO

None outside the selected amendment. Pending stdin/final tasks remain outside its execution scope.
