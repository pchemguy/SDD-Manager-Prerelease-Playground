# Review plan

## Campaign and candidate

- Campaign: `037_a6c42dd`; full starting and reviewed source: `a6c42dd754843abf9bafca7dee2aee9e733b046a`.
- Working branch: `revision/037_a6c42dd-prerelease-review`; eventual revision integration target: `main`, `pchemguy/SDD-Manager`.
- Candidate package: `sdd-manager.zip`, source version `0.15.0`, 132 regular files, 298720 bytes; SHA-256 `52a828f85e7ff619a0ebe028b446650ba999d89b2445efe573714ba96a012b2d`.
- Package built locally from the exact source using the unchanged release workflow's `git archive` member selection; this is not a hosted asset or installed-client result.
- Objective: apply the [comprehensive prerelease profile](../../../../skills/sdd-manage/references/prerelease-review.md) to the entire CURRENT supported SDD Manager product and report defects, evidence gaps and bounded improvement opportunities.
- Scope authority: create/publish this campaign's review plan, inventory and report; run scoped local checks. No repairs, revision execution, product release/tag, publishing dispatch, hosted settings/tracking writes or main merge are authorized by this review request.
- State: Resumed by the human on 2026-10-10 for supplemental comprehensive assessment of integrated campaigns 038–041. The original candidate, completed assessment and five Open findings remain retained. Supplemental U-008 assessment is complete; this continuation updates review evidence only; repair planning/execution and main integration remain outside scope.
- Inventory: [SOURCE-INVENTORY.md](SOURCE-INVENTORY.md) accounts for every current nonhistorical tracked path; packaged files and source-only support tooling have distinct evidence boundaries.

## Review order, criteria and scenarios

| Unit | Scope / focused owners | Dependencies | Criteria | Representative scenarios / checks |
| --- | --- | --- | --- | --- |
| U-001 | Root scope/claims/instructions, prompt/notices/license/metadata and all sdd-conventions resources. | Pinned source/inventory. | C-001: one discoverable current authority, accurate supported/deferred claims, coherent naming/hierarchy/modularity/style and appropriate notices. | S-001: installed package versus source checkout; S-002: direct call versus coordination; S-003: controlling instruction conflict and closed history exclusion. |
| U-002 | All sdd-design, sdd-specify, sdd-plan, sdd-tasks and sdd-integrate-feature source. | U-001. | C-002: complete intended contracts, owner boundaries, necessary feature deltas, prerequisite/QC/human gates, single task ownership and incorporation/archive eligibility. | S-004: greenfield chain; S-005: interrupted existing documents; S-006: small/large feature preparation; S-007: selected versus full feature incorporation. |
| U-003 | All sdd-manage, sdd-orient, sdd-implement and sdd-steer source. | U-001/U-002. | C-003: correct handoffs/authorization, branch/commit publication barriers, range selection, human checkpoints, recovery and stopping boundaries. | S-008: partial milestone/full phase; S-009: clean tree with unpublished commits; S-010: push/merge failure; S-011: steering stops before task resumption; S-012: prerelease reminder versus selected review. |
| U-004 | All sdd-docs/sdd-report source plus root README/AGENTS/current navigation and every current diagram/template. | U-001–U-003. | C-004: audience and composition, true examples/claims/links, concise orientation, diagram semantic gates/failures/stop points and evidence presentation. | S-013: diagrams compared with owner workflows; S-014: Markdown template/list/fence rendering/spacing; S-015: reported completion versus actual evidence. |
| U-005 | All sdd-forge source and actual release CI. | U-001–U-004. | C-005: credentials/permission separation, tracking projection/lifecycle, highlights/notes transfer, one publisher, exact candidate, complete assets, safe retry and readback. | S-016: incremental highlights/cuts/retry; S-017: uncertain hosted write; S-018: tag-triggered actual workflow; S-019: draft/partial assets/latest selection and optional review. |
| U-006 | All sdd-tdd/sdd-verify source and acceptance/textstats docs, catalogs, helpers, schemas, fixtures and tests. | U-001–U-005. | C-006: meaningful checks/independent expectations, unsupported-platform/fresh-consumer limits, sensitive-data handling and actual test coverage. | S-020: run 113-test support suite; S-021: success/failure/boundary/recovery contracts and harness inspection; S-022: distinguish local support from live consumer acceptance. |
| U-007 | Every built member, manifests, root/skill artwork and presentation metadata; final cross-unit consolidation. | U-001–U-006. | C-007: exact source/package bytes, required/excluded members, safe paths, checksum, resolvable resources and honest compatibility/readiness. | S-023: ZIP/source/hash/member inspection and extracted resource resolution; S-024: skill/plugin validators; S-025: readiness blockers versus unaccepted deferral proposals, candidate change requires affected recheck. |

The release diff may prioritize scrutiny but never restrict this inventory. Assess relevant success, negative and recovery branches on both sides of consequential handoffs. Source inspection does not establish agent runtime behavior. Read all selected current skill entries/references and inspect source-only support components within their roles; do not supply assessor material to a claimed fresh consumer.

## Evidence, exclusions and priorities

Use source inspection, documented scenario assessment, actual local execution and focused authoritative external verification where needed. Read-only online verification may check referenced provider APIs/actions; no authenticated external mutation is implied. Run the declared support suite, package/member/reference checks and suitable Markdown/presentation validators. Attempt diagram rendering with available local tools; record unavailable facilities rather than claim rendered readability. No new product tests or source fixes are introduced during review.

Closed review/revision/feature/steering records are frozen and excluded from routine loading, link/style checks and compatibility assessment. The current campaign index is navigation, not a substitute for historical evidence. Unlinked EXPLORE_DRIVE drafts are nonauthoritative exploration and excluded. Generated/vendor files are accounted for separately. No live acceptance destination is selected; fresh-consumer execution, installed-client discovery, live CI, hosted release/download integrity and unrepresented platforms remain unverified unless concretely exercised within authorized scope.

Allocate stable R-001 onward once. Each finding records exact baseline locations/evidence, type (defect/evidence gap/improvement), consequence, priority/confidence, bounded correction, dependencies, needed human decision and objective recheck. Use P1 for a demonstrated failure of a claimed required release/workflow path, P2 for material bounded defects or coverage gaps, and P3 for maintainability/usability improvements; justify classification without treating every unknown as a blocker.

Keep findings Open until the human actually accepts, rejects or defers them. Readiness separates required-check blockers, optional improvements and unavailable evidence. Do not invent accepted deferrals or risk acceptance. Every conclusion applies only to the pinned candidate; fixes/new candidates require affected unit/handoff/regression rechecks.

## Persistence and stopping

Commit/push/read back the plan and inventory before assessment. After each unit, maintain the canonical review report (including no-finding coverage and actual checks), commit it and verify remote containment before any next unit or additional project work. Report checkpoints remain on this campaign branch. Do not merge review-only planning/report changes into main as an implementation prerequisite.

Consolidate coverage, canonical findings/counts, readiness, proposed revision queue and evidence limits; publish the final report and return it. Stop before repairs, revision execution or product release publication. This campaign remains available for a separately accepted revision plan and authorized execution.

## Resumed assessment: campaigns 038–041

Human request: resume 037 and update its comprehensive report with findings/assessments related to the four integrated campaigns. Original candidate and U-001–U-007 evidence remain historical; they do not certify the changed candidate.

- Supplemental exact source: `b246f8f92f35a8d2077bce467102f63270d64f2b`, version `0.15.0`; branch `revision/037_a6c42dd-prerelease-review`.
- Integration provenance: 038 at `8bb3b3d`; 039 and its amendments at `7f06904`, `f64e7eb`, `a0685b5`; 040 and its amendment at `e24f30c`, `ca99ca1`; 041 at `b246f8f`. Full identities and parent/source containment are available in Git.
- Selected historical consultation: only these four child campaigns' reports and merge evidence, to establish delivered scope and evidence limits. Other closed records remain excluded and unchanged.
- Supplement existing inventory with exact changed path/blob identities. Build the workflow-shaped package from the new pin and record hash/member checks; no hosted asset or installed-client result is implied.

| Unit / criteria | Affected coverage | Assessment and rechecks |
| --- | --- | --- |
| U-008 / C-001–C-007 | Campaigns 038–041 and their cross-unit effects on U-001–U-007. | Read all changed current product/support guidance and relevant unchanged authorities; compare tracking/activation/outage handoffs, prompt authorization/checkpoints, nested/reopened identity/return, cumulative summaries/highlights, atomic task closure/audit/recovery. Reassess README/AGENTS/diagrams and original R-001–R-005 where affected. Run support/catalog checks and the shipped highlights recipe fixtures; inspect exact package and changed-resource links. Distinguish source scenarios, local execution and child historical evidence from live fidelity. |

U-008 is one bounded supplemental unit with four campaign subassessments and final cross-unit consolidation; its completion checkpoint publishes the report before further project work. Unchanged baseline coverage may be reused only with byte-identity and relevant handoff applicability established. Record unavailable or incomplete rechecks rather than infer full candidate readiness. Allocate R-006 onward only for demonstrated new findings; consolidate overlapping runtime gaps under R-005. No full TextStats/live consumer campaign, hosted tracking/release mutation, product source repair, child-record amendment, revision execution, main merge or release is selected.
