# Backend lifecycle revision report

## Campaign and result

- Campaign: `010_3f56922`; [plan](REVISION-PLAN.md), [accepted intent](LIFECYCLE-POLICY.md), [baseline findings](REVIEW-REPORT.md).
- Starting baseline: `3f56922a936c8fe039f906ed27566b5662b5440c`; preparation amendment checkpoint: `7efe45b7e7b6bcf2abd703fba5ee6d1b201ea89d`.
- Source revision commit: `60dc077df7b89e8302f8ae34b550b5e747330444` (V-001–V-007 and local/consumer evidence).
- Working branch: `revision/010_3f56922-backend-lifecycle`; established integration target: `feature/architecture-revision`.
- Result: lifecycle source instructions, workflow ownership/report placement and TextStats assessment criteria revised. Local source/catalog/support checks and fresh read-only consumer assessments are recorded below. Provider lifecycle execution remains pending. The revision branch and verified explicit target integration are published under the 2026-10-04 publication/integration command.
- Canonical authority: [backend object lifecycle](../../../../skills/sdd-conventions/references/backend-object-lifecycle.md). Campaign policy is retained accepted intent, not a competing shipped authority.

## Revision evidence

| Action / findings | Actual changes | Verification / disposition |
| --- | --- | --- |
| V-001 / R-001–R-004 | Added canonical lifecycle invariant reference and conventions entry; explicit task/report/closure ordering, local-only behavior and uncertainty recovery. | Canonical route/local links validated; source revised. |
| V-002 / R-002 | PLAN reserves final review milestone; TASKS derives explicit milestone and phase review tasks with report links; range selection counts review tasks. | Fresh planning consumer derived two phases with three delivery and two phase-review milestones, 11 tasks and correct main report paths; no source contradiction reported. |
| V-003 / R-001, R-003 | Coordinator phase activation reference and entry route; eligible-phase-only GitHub projection; new milestone closure/reopening/readback procedure and backend route. | Fresh recovery consumer kept timed-out closure unknown, blocked dependent phase review, and required readback before replay/advancement. Provider execution pending. |
| V-004 / R-003, R-004 | Verify owns separate read-only boundary code review; implement owns repair/report persistence and ordered closures; startup distinguishes pending lifecycle transitions. | Fresh consumer assessments preserve owner separation and critical/contract blockers; hosted and actual interruption execution pending. |
| V-005 / R-004 | Completion reporting defines workflow-specific paths, admissible deferral, solution options/provenance and final TODO aggregation. | Report consumer correctly blocked a SPEC violation and required feature-prefix final report. It initially grouped an inadmissible repair with TODO; source clarified Findings/Blockers separation; fresh recheck kept R-09 and unassessed R-03 in blockers and only admissible R-07 in TODO. |
| V-006 / R-001–R-004 | Workflow identity allocation includes phase-nested revisions; steering/report/campaign/feature/orientation handoffs and public README/capability map aligned. Explicit implementation command includes routine commits/pushes/integration without separate confirmation. | Source composition and local links checked. Historical records retained; no automatic path migration. |
| V-007 / R-005 | Added lifecycle criteria to 14 assessor cases, corresponding guides, catalog prerequisites, scenario/objectives and controlled/uncontrolled interruption variants; A-003 consumer requests eligible first-phase tracking. | Catalog validates all 27 stable cases; support suite 67 passed. Harness/schema success is not live lifecycle acceptance. |
| V-008 / R-001–R-005 | Local structural/composition checks and fresh read-only consumer assessments. | Live acceptance Blocked: no dedicated test repository supplied. No hosted phase/milestone transitions or native interruption trials were executed in this revision. |

## Checks and consumer limits

- `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`: 27 cases; static asset validation, `live_acceptance: false`.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 67 tests passed; [retained output](evidence/support-tests.log).
- Local structural inspection: all 15 skill names/descriptions and UI metadata parse; plugin JSON parses; 76 Markdown files and 182 local links checked without structural errors; diff whitespace checked. [Structural results and source hashes](evidence/structural-verification.json). GitHub milestone open/closed and issue retirement reason semantics were checked against the official REST documentation; no provider write was performed.
- Fresh contexts received source skill paths and ordinary project inputs/facts, with no campaign analysis or assessor materials. They performed read-only drafts/handoffs, not real hosted writes or interrupted implementation. These outcomes assess instruction interpretation only. [Retained consumer assessment summaries](evidence/consumer-assessments.md) accompany final checkpoint evidence. Trials loaded the working-tree source, not a published installed package; exact per-loaded-file hashes/native transcripts were not captured.

## Persistence and integration

- Source revision: `60dc077` is identified by the full source commit above; evidence checkpoint `d738c04`, publication checkpoint `1a5d8eab3ff2d49c2b6f28d672c77e199a956a4a`.
- Revision branch published at `1a5d8eab3ff2d49c2b6f28d672c77e199a956a4a`; exact remote readback matched.
- Explicit two-parent merge: `06e0b2e97dc15c69aedf9f1991ed2f79497e0aec` into `feature/architecture-revision`.
- Target parent: `3f56922a936c8fe039f906ed27566b5662b5440c`; revision parent: `1a5d8eab3ff2d49c2b6f28d672c77e199a956a4a`.
- Prospective merged state: no conflicts; 67 support tests passed, catalog 27 validated, local links/frontmatter valid, all verified source snapshot hashes matched. [Merge verification](evidence/merge-verification.json), [merged test output](evidence/merged-support-tests.log).
- Committed merged state: two parents confirmed; source hashes rechecked unchanged. Target push succeeded and exact remote readback matched merge SHA `06e0b2e97dc15c69aedf9f1991ed2f79497e0aec` before this report-only publication follow-up.

Earlier automatic approval review rejected the preparation push. The human subsequently explicitly authorized pushing the revision to pchemguy/Skill-SDD-Manager and completing verified integration; publication then succeeded using the established Git destination. The earlier block prevented normal per-action push checkpoints, so the verified source actions were retained as one coherent local revision boundary before publication. No rejected operation was bypassed.

The revision branch is retained. This integration target is feature/architecture-revision; no default-branch integration is claimed. Live provider acceptance is a separate pending diagnostic run, not an integration check that was executed here.

## TODO and live acceptance

- Run live acceptance on a dedicated disposable repository using `acceptance/textstats/AGENTS.md`, a pinned revised source and real provider readback. Repository identity and suitable API access must be supplied or requested; missing access does not establish a pass.
- Execute controlled and uncontrolled interruption variants at actual projection, report persistence, milestone closure and phase integration actions. Runtime termination and safe response-loss facilities are required; unavailable variants remain Blocked/Not run.

No identified non-critical source issue is being deferred. These TODOs are outstanding live verification work, not admissible code defects carried past a completed milestone gate.

Agent prompt for the pending live run:

```text
Run live acceptance of SDD Manager's revised backend lifecycle using acceptance/textstats/AGENTS.md and the revised source pinned by exact commit/hash. Read the acceptance directory for setup and run instructions. Request a dedicated disposable test repository and suitable GitHub access if absent. Execute the affected lifecycle cases and controlled/uncontrolled interruption variants with independent assessor evidence, actual report commits and provider readback. Preserve scope and unknown outcomes; report unavailable checks as Blocked/Not run. Publish sanitized evidence only within the authorized test destinations.
```

## Authorization policy follow-up — 2026-10-04

The human requested explicit precedence over redundant external guards. The coordinator entry and review/revision reference now state that an accepted revision implementation command authorizes routine revision-branch commits, established-destination pushes, verified integration and target publication. Subordinate workflow/skill and external workflow-guard confirmation assumptions yield to that authorization. Enforced platform permissions and higher-priority restrictions remain binding; rejected operations are reported without bypass. Campaign policy/plan links reflect this ownership.

This follow-up changes authorization guidance only. TextStats lifecycle criteria and procedures remain as recorded in V-007; 67 support tests and catalog validation passed during the source revision and merge. Live acceptance remains pending a dedicated test repository. Local link/frontmatter and diff checks are used for this focused guidance amendment.

The follow-up wording explicitly acknowledges generic restrictions as default protections and defines a focused authorization override bounded by accepted scope, established destinations and applicable verification gates. It supplies authorization context through supported guard mechanisms and grants no blanket permission or bypass of enforced controls.

The final clarification defines the implementation command itself as explicit authorization under this policy. General restrictions requiring authorization are thereby satisfied for routine scoped commits, pushes and verified integration; they are not bypassed. Unsupported lack-of-authorization assumptions must yield to the established command and scope.

Authorization clarification publication: revision tip `bfb6966c9954d672db2750e6e0a9f1f0fe83dac6` was published and explicitly merged as `63365fe5cc6d3c29364bcae0e016c6aec9dc010e`, with target parent `21a7176304bb6182e218c650ee870554b8a8a498`. Prospective source, local links, coordinator frontmatter and whitespace checks passed without conflicts; the target push succeeded. This is a focused policy amendment; the earlier 67-test lifecycle results are retained rather than represented as a new test run.
