# TextStats support revision report

## Campaign and scope

Campaign `017_54d55ed`; [implementation plan](REVISION-PLAN.md), [canonical findings](REVIEW-REPORT.md). Reviewed baseline: `54d55edebd8a7af6499d625bdbb357f864a4db1d`. Execution checkpoint: `3bc079018922bc84774b58c36fd7c1482adcf9e0`. Working branch: revision/017_54d55ed-comprehensive-review; target: feature/architecture-revision.

The human commanded revision execution on 2026-10-04. Authorized repairs cover R-001/R-002 ownership checking and R-003 helper documentation, with routine scoped commits/pushes and verified integration. Campaign 011 QC implementation and live/client acceptance remain outside this revision.

## V-001 — Regression and contract checkpoint

Added independently expected regressions for custom/mixed IDs, linked reports/specifications, backtick/tilde/indented examples, incomplete fences, unsupported candidates, explicit additive child documents, unsafe/malformed options, hierarchy parents and custom table IDs. Added catalog validation sensitivity for the optional ownership field. HELPER-INTERFACES.md now defines the intended bounded parsing contract.

Actual RED command: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=acceptance/textstats python -m unittest tests.test_checkers tests.test_catalog.CatalogIntegrity.test_optional_ownership_documents_contract_validation -v`. [Raw output](evidence/revision-red.txt). Observed result: 16 tests ran, with 12 failing subtests/tests and one error from rejection of the new optional DSL field; exit 1. Existing checker controls run alongside new regression cases. The failures demonstrate missing behavior; production parser and validator remain unchanged at this checkpoint. This is an intentionally failing, incomplete revision checkpoint, not a completed repair. V-002 must establish GREEN before repair completion.

## TODO — pending separate later review

- **TODO-017-001:** Campaign 011 QC implementation / P-001. Pending for a separate later review against then-current source and its retained campaign plan.
- **TODO-017-002:** Live/client acceptance / E-001/E-002. Pending for a separate later review with an explicitly supplied dedicated repository, supported client/independent contexts/interruption facilities and protected credentials only when classified access failure requires them.

Neither TODO is an exit requirement or executed action in this revision. No installation refresh, live acceptance or hosted test object creation is claimed.

## V-002 — Ownership correction and GREEN

V-001 RED checkpoint: `bfb2454`, pushed on the campaign branch before production changes. The runtime checker now parses case-sensitive stable IDs without a T-prefix assumption; validates malformed checkbox/table candidates; skips properly closed backtick/tilde examples and rejects incomplete fences. Default active task roots remain authoritative; arbitrary linked Markdown is not traversed. Optional additive child documents are validated for safe normalized paths/history exclusions and checked against actual files/symlink parents. Runtime and catalog DSL validation share the option syntax validator. PurePosixPath keeps the declared slash-separated option syntax independent of the host OS.

Focused GREEN: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=acceptance/textstats python -m unittest tests.test_checkers tests.test_catalog -v` ran 39 tests, exit 0 ([output](evidence/revision-green-focused.txt)). Subsequent closing-fence, decorated/case-sensitive ID and malformed-path/table regressions were added during code inspection. Full GREEN: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v` ran **79 tests**, exit 0, 23.012 seconds, no reported skips/failures ([output](evidence/revision-green-full.txt)). Catalog validation: 27 valid static cases, exit 0 ([output](evidence/revision-catalog.json)).

All four original probe expectations now hold; the corrected result is a separate [artifact](evidence/ownership-probes-corrected.json) recording the tested pending source hashes. Original review observations are unchanged. R-001/R-002 behavior is rechecked; final composed review/integration remains V-004. Helper package pinning/recovery/capture regressions also pass; this is local support verification, not live/client acceptance.

## V-003 — Helper documentation

V-002 repair checkpoint: `0024d20`, pushed before documentation work. Added module responsibilities to core.py and the four identified support/test modules. All 32 top-level core interfaces now have local documentation, including new ownership parsing helpers. Consequential interfaces use Google-style Args/Returns/Raises sections where useful; small pure predicates retain concise contracts. No module split or dependency was introduced.

Semantic review checked package pinning and mode-sensitive fingerprints, prepare's new-clone mutation/partial-failure limits, export_recovery's declared completeness/protected-history/retained-root limits, reconciliation's exact-destination and retry-safe-false behavior, assessment's deterministic-only status, and callers' error propagation. Documentation describes observed implementation rather than promising arbitrary secret detection, atomic JSON writes, automatic restoration, complete task coverage or live authentication. HELPER-INTERFACES remains the canonical operational contract.

[Documentation verification](evidence/documentation-verification.json) confirms module coverage, all core interface docstrings and identical executable ASTs against V-002 for all five edited Python files after stripping documentation. Python 3.11 syntax parsing succeeds; actual runtime remains Python 3.12.14. Prior 79-test GREEN evidence remains applicable to unchanged executable behavior. R-003 is rechecked by API/caller inspection; docstring counts alone are supporting inventory, not the semantic review.

## V-004 — Composed code and documentation review

Reviewed the complete execution-checkpoint-to-working-tip difference, including all preceding action commits. The checker has one shared document-option syntax owner; runtime alone checks consumer files. Explicit children supplement rather than replace discovered roots; each document is parsed once while actual task IDs still fail on duplication. Stable IDs retain case/decorated identity, parent labels are excluded, malformed candidates/fences fail, and history/unsafe paths cannot be supplied as active children. Independent list-coverage/agent assessment remains required; this is a deliberately bounded task-document model, not a general Markdown parser.

Test inspection confirmed independently chosen expected outcomes and positive controls for real duplicates. Tests exercise actual helper CLI/collection failures, child roots, tables, fenced examples and both DSL consumers. All 27 shipped contracts remain unchanged and validate. Recovery/pinning/capture code changed only in documentation, confirmed by executable AST comparison; related existing regressions pass. Final document review found and corrected the older DSL summary row that still said ownership had no additional fields; it now agrees with the optional additive documents contract.

| Finding | Current disposition | Evidence |
| --- | --- | --- |
| R-001 | Verified on the repaired local source | Custom/mixed IDs and table/checkbox regressions; real duplicate controls; corrected original probes. |
| R-002 | Verified on the repaired local source | Linked reports/specifications excluded; fences/closing rules checked; explicitly selected child owners preserved. |
| R-003 | Verified by source/API review | Core interface and five module documentation coverage; actual contracts/callers reviewed; unchanged executable AST for documentation action. |

Required local checks and working scope are established. Explicit integration and target publication remain pending until their observed evidence below is recorded. Neither pending separate-review TODO is resolved by these dispositions.

## Integrated result and publication

**Result:** R-001, R-002 and R-003 are repaired and verified within the planned local support boundary. Revision execution is complete. The original review evidence and failing RED run are retained; no baseline failure was rewritten as a pass.

Action checkpoints bfb2454 (RED), 0024d20 (repair/GREEN), 75a23ee (documentation) and a55d2ec (composed review) were committed/pushed on the campaign branch. Final working tip: `a55d2ec7471f947ae082842316dab3db4498efb6`. Refreshed target parent: `3bc079018922bc84774b58c36fd7c1482adcf9e0`.

Explicit merge: `d8432963fe6417590c3169a0f5cd25d61a885b88`, with exactly those two parents. Before its commit, the prospective merged state ran the complete support suite: **79 tests passed**, exit 0, 24.556 seconds, no reported skips/failures ([raw merged output](evidence/revision-merged-tests.txt)). Catalog validation returned 27 valid static cases. Merged helper/test/document hashes match [boundary evidence](evidence/revision-boundary-validation.json); no conflict resolution or extra source change was needed.

The full staged diff whitespace check reported eight trailing-whitespace lines generated by unittest in the retained raw RED log. That evidence remains byte-preserved. A scoped staged diff check excluding only that raw log passed; source, documentation and other evidence have no reported whitespace errors. This is a recorded log-format exception, not an ignored source/test failure.

The merge was pushed to origin/feature/architecture-revision. Actual ls-remote readback confirmed target d8432963fe6417590c3169a0f5cd25d61a885b88 and working branch a55d2ec7471f947ae082842316dab3db4498efb6. This final evidence follow-up is persisted on the target after observing that publication.

Remaining TODOs are unchanged: **TODO-017-001 campaign 011 QC implementation** and **TODO-017-002 live/client acceptance**, both pending for a separate later review. No current in-scope blocker or additional deferred repair was established. Python 3.12.14 was executed; Python 3.11 syntax was checked but its runtime and other platforms were not executed. Passing helper/catalog checks establish neither fresh-agent workflow execution nor installed/live-provider acceptance.

Stop boundary: completed, verified and published campaign 017 support revision. Retain the working branch. Do not start either pending TODO or merge main automatically.

## Later TODO disposition — campaign 019

TODO-017-001 is completed by the separately authorized [Campaign 019 QC implementation](../019_609d084/REVISION-REPORT.md). This updates its current disposition without changing campaign 017's original scope or evidence. TODO-017-002 live/client acceptance remains pending separately.
