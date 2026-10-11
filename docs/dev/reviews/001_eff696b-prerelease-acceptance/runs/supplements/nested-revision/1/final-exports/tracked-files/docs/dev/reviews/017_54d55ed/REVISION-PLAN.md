# TextStats support revision implementation plan

## Campaign, decisions and scope

- Campaign: `017_54d55ed`.
- Reviewed baseline: `54d55edebd8a7af6499d625bdbb357f864a4db1d`.
- Planning checkpoint: `1591b17508d194ebaa55883463f9784831c4e486`.
- Working branch: `revision/017_54d55ed-comprehensive-review`.
- Integration target: `feature/architecture-revision` in pchemguy/Skill-SDD-Manager.
- Canonical findings: [review report](REVIEW-REPORT.md), R-001–R-003.
- State: V-001–V-004 completed, verified, explicitly integrated and published; [REVISION-REPORT.md](REVISION-REPORT.md) records observed evidence. The human commanded this bounded implementation on 2026-10-04. Pending separate-review TODOs remain unexecuted.
- Selected implementation scope: correct R-001/R-002 as one cohesive task-ownership checker change, then document consequential helper interfaces for R-003. Final verification and revision reporting cover that boundary.
- Deferred: P-001 campaign 011 QC implementation and E-001/E-002 live/client acceptance. These are pending TODOs for a separate later review; they are neither prerequisites nor completion requirements for this revision.
- Revision execution will update `REVISION-REPORT.md` in this directory. No empty report is created during preparation.

## Resulting checker contract

The checker must assess actual executable task owners, preserve project-specific stable IDs, and reject duplicate ownership without treating evidence or examples as tasks.

1. Preserve the existing `task_ownership` check kind and version 1 contracts. Default roots are active TASKS.md and FEATURE-TASKS.md discovered within the existing supported project scope, with historical/archive/vendor exclusions retained.
2. Recognize task IDs independently of the `T-` prefix. Document the supported stable-ID syntax with examples covering `T-001`, `F-001`, `TASK_001` and `ABC42`. Preserve exact identity/case. Distinguish phase/milestone parents from tasks using the supported hierarchy and row semantics. An ambiguous or unsupported candidate task must fail with a useful sanitized cause rather than disappear from a successful collection.
3. Treat checkbox and table task representations consistently. Preserve duplicate detection across active roots and designated child lists, meaningful empty-collection failure and malformed-row rejection.
4. Exclude fenced code examples before parsing task rows. Handle both backtick and tilde fences, closing-fence rules and indentation supported by the task format; incomplete/ambiguous syntax must not hide otherwise executable work behind an invented successful result.
5. Replace unrestricted Markdown-link traversal with explicit child-list selection. Add an optional additive `documents` array to a `task_ownership` contract for repository-relative active child lists. It must never suppress the default active roots. Validate nonempty unique safe paths, reject missing/protected/escaping/symlink paths, retain history exclusions and deduplicate a document reached more than once. Other links remain navigation/evidence and confer no ownership. This is assessor configuration; no new metadata or markers are required in consumer product documents.
6. Update both runtime DSL validation and catalog validation to accept exactly this optional field. Existing shipped contracts remain valid. Independent assessment still establishes whether designated lists cover the actual project; deterministic success does not certify agent behavior or an undisclosed task collection.

The implementation may use small internal parsing helpers where responsibility and testing justify them. Keep stdlib-only Python 3.11 compatibility; do not introduce a Markdown dependency, rewrite unrelated recovery logic or split modules solely to reduce file size.

## Authoritative updates and owners

| Owner / artifact | Planned change | Required before |
| --- | --- | --- |
| TextStats helper contract: scripts/HELPER-INTERFACES.md | Supported IDs/representations, fences, explicit additive child documents, validation/errors and evidence limits. | Final checker acceptance |
| Runtime checker: scripts/core.py | Implement the ownership model and matching strict DSL validation. | Regression and composed verification |
| Catalog tooling: cases/assessor/catalog_tools.py | Match optional ownership DSL field and path-validation semantics. | Catalog validation |
| Tests: tests/test_checkers.py and tests/test_catalog.py | Independently expected false-pass/false-failure and compatibility regressions. | R-001/R-002 disposition |
| Documentation: scripts/core.py and four identified test/support modules | Professional module and consequential API documentation checked against callers and behavior. | R-003 disposition |
| Campaign records | Actual action evidence, finding rechecks, pending TODOs and verified publication. | Final integration |

SDD Manager skill policy and main development documents require no change for these harness defects. Campaign 011 owns its separate QC policy implementation. The review's original probe source and JSON remain historical evidence; corrected outcomes are recorded separately rather than replacing baseline observations.

## Ordered implementation actions

| Action | Findings / outcome | Targets and dependencies | Verification / checkpoint |
| --- | --- | --- | --- |
| V-001 | Establish regression sensitivity and the bounded ownership contract. | R-001/R-002; tests/test_checkers.py, tests/test_catalog.py, HELPER-INTERFACES.md. No prerequisite beyond the planning checkpoint. | Observe the intended failures on the existing checker: mixed/custom IDs, linked report and fenced example. Add explicit-child and malformed/unsafe-input cases with independently chosen expectations. Record RED and compatibility controls; persist as an accurately labeled incomplete revision checkpoint, not a completed repair. |
| V-002 | Implement and verify the cohesive ownership correction. | core.py, catalog_tools.py; depends on V-001. | Custom-only and mixed IDs work; real duplicates fail across roots/explicit children; reports/examples do not count; malformed/unsafe/unsupported cases cannot pass. Existing default contracts and archive exclusions remain valid. Run focused checker/catalog tests, then the full support suite and catalog validator. Commit/push repairs and evidence before V-003. |
| V-003 | Document consequential helper interfaces and module responsibilities. | R-003; core.py, tests/support.py, test_checkers.py, test_preflight.py, test_recovery.py; depends on V-002. | Document behavior, arguments/results, Stop/errors, side effects, preconditions and recovery/persistence invariants where material. Review package, prepare, export_recovery, reconcile, assessment and their collaborators against actual callers/tests. Add module purpose docstrings; avoid redundant narration. Confirm the documentation diff preserves executable behavior and repeat affected checks only where needed. Commit/push result and evidence. |
| V-004 | Review, report and integrate the complete bounded revision. | All three findings; depends on V-002/V-003. | Code review and tests are separate obligations. Verify composed parser behavior, helper contracts, catalog compatibility, documentation and scope; fix in-scope defects before completion. Record dispositions, actual tests/limits, TODOs and commits in REVISION-REPORT.md. Verify/publish the working boundary, perform explicit two-parent integration, check the merged state and publish/read back the target. |

These are four revision actions, not fabricated product task IDs or new product phases/milestones. V-001's intentionally failing regressions are a retained RED checkpoint and must not be reported as a successful completed revision. Resume finishes the earliest unfinished action using actual diffs, test evidence and Git/publication state.

## Required verification and exit evidence

From repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v
PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate
```

The reviewed baseline has 68 passing support tests and 27 valid static cases; the revised suite must collect all applicable existing and new tests, with actual counts/results recorded. Do not prescribe a fixed final test count. Include positive controls and sensitivity to skipped custom IDs, traversal of linked evidence, fenced examples, omitted child owners, real duplicates, malformed tables and unsafe child paths. Test both optional-field validation implementations. Inspect affected API documentation for accuracy; a docstring count alone is insufficient.

Before integration, assess the complete branch difference and confirm only planned helper/test/documentation/campaign changes. Package metadata, skill instructions, credentials and unrelated files remain outside repair scope. Record Python/Git versions; running Python 3.12 does not establish a Python 3.11 execution result. Preserve source pinning, recovery, output exclusivity and secret-handling behavior through the full existing regression suite. Use a new corrected-result artifact if rerunning historical review probes.

## Pending TODOs — separate later review

| TODO | Pending work and provenance | Later review entry / prerequisites |
| --- | --- | --- |
| TODO-017-001 | Campaign 011 QC implementation (P-001): SPEC/PLAN/TASKS conformance reviews, fragmentation/overload guidance, adjacent reports/rechecks and readiness gates. | A separate later review must reconcile [campaign 011's existing plan](../011_a3b2ad9/REVISION-PLAN.md) against then-current source, establish the executable scope and proceed under its own implementation authorization. Retain campaign 011 IDs; do not duplicate its policy here. |
| TODO-017-002 | Live/client acceptance (E-001/E-002): installed source/subtitle/icon/routing verification and current lifecycle acceptance on a dedicated repository, including controlled/uncontrolled recovery and live provider readback. | A separate later review must pin then-current source, establish supported client/interruption/independent-assessor facilities and obtain an explicitly supplied dedicated repository plus protected credentials only if classified access failure requires them. Use the live-acceptance prompt in acceptance/textstats/README.md. Missing facilities remain Blocked/Not run. |

Carry both TODOs into the revision report and final handoff as pending. Completion of R-001–R-003 must not close these TODOs, imply campaign 011 implementation, or claim live/client acceptance. Do not refresh installations, change release metadata, create hosted test objects or start a new acceptance campaign as part of this revision.

## Persistence and stopping

On an implementation command, reuse the campaign branch and refresh it from the established target without discarding retained evidence or unrelated work. Follow scoped per-action staging, commits, pushes and remote verification. Source and actual recheck evidence belong together; blocked publication retains local commits and stops dependent execution. Continue an existing merge/push after interruption rather than creating a second boundary merge.

Finish only when R-001/R-002 behavior is rechecked, R-003 documentation is reviewed, required local regressions pass, the revision report is committed and the authorized boundary is verified and published into feature/architecture-revision. Retain the working branch. Stop before the pending separate review TODOs and before any merge to main.
