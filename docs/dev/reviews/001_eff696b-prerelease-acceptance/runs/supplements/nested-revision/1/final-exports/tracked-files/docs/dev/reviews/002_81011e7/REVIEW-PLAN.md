# Systematic plugin review plan

**Campaign:** `002_81011e7`. Current record: `docs/dev/reviews/002_81011e7/REVIEW-PLAN.md`. Established finding IDs and baseline evidence are retained.

## Baseline, purpose, and deliverables

- **Reviewed baseline:** `81011e7db200f0eef89a52d35896bbf97575b6c1` (`81011e7`), plugin version `0.14.1`.
- **Purpose:** Evaluate all packaged capabilities and their composition; produce located, evidence-backed findings a subsequent agent can revise and verify.
- **Plan:** `docs/dev/reviews/002_81011e7/REVIEW-PLAN.md`.
- **Report:** `docs/dev/reviews/002_81011e7/REVIEW-REPORT.md`.
- **Historical input:** [prior review](../001_49143fa/REVIEW-REPORT.md). Recheck its relevant scenarios; do not treat its results as fresh evidence or automatically reopen corrected findings.
- **Review status:** S01–S15 and P01–P03 are complete; results and pushed checkpoints are recorded in the [review report](REVIEW-REPORT.md).
- **Current scope:** Completed source revisions for SDD-R-001 and SDD-R-002, final package validation, and archive. See the report for actual checks, revision commits, and remaining validation limits.

The filename suffix identifies the source revision being reviewed, not the commit containing the plan or later report updates. Keep the suffix fixed throughout this campaign. Review baseline files through `git show 81011e7:<path>` or a detached disposable worktree; commit report updates on the working branch. Record any working-branch differences that affect evidence. A later source revision requires an explicit revised scope or a new baseline-specific campaign; do not silently mix revisions.

## Review boundary

Review all 15 `skills/*/SKILL.md` entries, their references, presentation metadata and assets, applicable license/provenance, root manifest, README, capability map, and their relationships. Include any additional discovered package-owned files in the inventory and explain their role or exclusion.

- **Findings only:** Do not revise skills, runtime behavior, manifest, or README during review. Report changes belong to the reviewer; source corrections belong to the subsequent revision agent.
- **Evidence:** Read the complete skill and its resources. A filename, declared capability, or text-presence assertion does not establish working behavior.
- **Experiments:** Use disposable fixtures and local bare remotes for file/Git scenarios. Preserve the source worktree and unrelated staged, unstaged, and untracked content.
- **External effects:** Live provider writes, credential replacement, dependency installation, and client installation are outside the default review scope. Report untested provider/client behavior. Perform them only when separately authorized in an appropriate test environment.
- **Sources:** Review the baseline's instructions and established user constraints. Identify external-standard or provider claims needing verification; distinguish inspected local provenance from independently verified remote content.
- **No inferred approval:** Prior review conclusions and passing structural checks do not approve design changes or establish end-to-end completion.

## Order and dependency treatment

This is a bottom-up review order by responsibility and complexity, not a claim that the skills form an acyclic invocation graph. Shared orientation, reporting, and manager coordination appear throughout the plugin. Review their interface requirements when encountered; resolve reciprocal coordination edges in the final composition passes. Do not postpone a located finding simply because its other owner is reviewed later.

| Unit | Skill | Focus and prerequisite context | Required scenario focus |
| --- | --- | --- | --- |
| S01 | sdd-conventions | Shared criteria and hierarchy invariants; no artifact or execution ownership. | Apply a convention proportionately; detect duplicate IDs and ambiguous parentage. |
| S02 | sdd-orient | Read-only discovery, instructions, Git eligibility, and factual handoff. | Non-Git, monorepo/scoped instructions, clean/dirty, unborn/detached/conflicted state, and interrupted evidence. |
| S03 | sdd-report | Formats and evidence distinctions; consume task/issue facts without mutation. | Planned issue versus completed result; partial versus closing references; taskless maintenance; absent verification. |
| S04 | sdd-design | Exploration, brief, architecture, decomposition, and review boundaries. | Discussion without file creation; accepted versus assumed decisions; direct entry into an established stage. |
| S05 | sdd-specify | Observable contracts, acceptance, focused children, and feature deltas. | Requirements versus observed code; conflicting sources; active feature delta and end-state prose. |
| S06 | sdd-plan | Delivery strategy, milestones, exits, and physical ownership. | PLAN/layout separation; unresolved inputs; feature-plan optionality; coherent stopping boundaries. |
| S07 | sdd-tasks | Derivation and read-only progress review, stable identities, hierarchy form. | Main/feature ID uniqueness; four-space nesting; unchecked derivation; selection/completion/reconciliation routed to their owners. |
| S08 | sdd-tdd | Test strategy, independent expectations, meaningful RED, and test ownership. | Intended failure versus setup error; code predating tests; behavior-preserving refactor; misleading mocks or copied expectations. |
| S09 | sdd-docs | Module/API coverage, project style, guides, and governing findings. | Style fallback; README example checks; generated/external exclusions; governing amendment deferred to the human. |
| S10 | sdd-verify | Check selection, condition coverage, state-bound evidence, and failure classification. | Zero tests, skips, warnings, interruption, stale evidence, unrelated failure claims, and no automatic repairs. |
| S11 | sdd-integrate-feature | Accepted delta incorporation, source cleanup, and selected task reconciliation. | SPEC-only scope; source still referenced; TASKS-only versus joint ownership transfer; preserved evidence and parent claims. |
| S12 | sdd-forge | Optional report dependency, GitHub projection, identity, auth, and lifecycle. | Unique matching; renamed parents; partial/interrupted writes; duplicate issue/PR exclusion; 403; backlog and idempotent closure. |
| S13 | sdd-implement | Range selection, continuation, TDD/docs/verification composition, persistence, and checkpoints. | Selection-only; push-first; checked-uncommitted; dependency blockers; staged/hunk isolation; per-task and parent completion; older pending closures. |
| S14 | sdd-steer | Human-commanded amendment, direct document edits, retained contracts, persistence, and stop. | Assessment-only; removal with retained behavior; no feature overlay/integration; no automatic main-workflow resume. |
| S15 | sdd-manage | All workflow routes, shared prerequisites, credentials, transitions, and persistence ownership. | Preparation-only and combined requests; established authorization; missing skills/tools; credential/store blockers; scope conflicts; exact stopping points. |

After S15, complete P01 (package-wide validation), P02 (cross-skill/workflow synthesis), and P03 (report consolidation and revision handoff). These passes complement the individual reviews; they cannot substitute for reading any skill.

## Criteria applied to each skill

Record each criterion as **Satisfied**, **Finding**, **Blocked**, or **Not applicable**, with evidence or a reason. Use Blocked when evidence is unavailable; do not use Not applicable to conceal an unperformed check. Satisfied is bounded to the examined behavior and evidence level.

| Criterion | Assess |
| --- | --- |
| C01 — Packaging and discovery | Name/frontmatter, description triggers, contained resource paths, metadata, icons, and optional components. |
| C02 — Purpose and boundaries | Cohesive responsibility, usable entry conditions, inputs/outputs, explicit effects and stopping rules. |
| C03 — Authority and scope | User authorization, instruction discovery, accepted decisions, dirty ownership, and no silent scope expansion. |
| C04 — Dependencies and handoffs | Required versus optional skills/tools, owner routing, missing dependency behavior, reciprocal interface consistency. |
| C05 — Document and task contracts | Canonical ownership, main/feature semantics, stable IDs, parentage, reconciliation, source retention, and completion claims. |
| C06 — Execution and continuity | Eligible Git baseline, task selection, interruption, verified pending work, failure handling, and checkpoints. |
| C07 — Persistence and external effects | Scoped commits, index/worktree preservation, pushes, hosted authorization, idempotency, and partial outcomes. |
| C08 — Credentials and access | Approved external store, protected transfer, provider checks, sanitized failures, cause-sensitive escalation, and bounded retries. |
| C09 — Testing and verification | Meaningful scenarios, independent expectations, acceptance coverage, actual collection/outcomes, state/environment fidelity, and valid reuse. |
| C10 — Reporting and evidence | Planned/implemented/verified/committed/pushed/hosted distinctions, supported certainty, limitations, and source attribution. |
| C11 — Composition and editorial quality | Progressive disclosure, clear sequence, concise lists/tables, consistent terms, blank heading spacing, useful examples at the end. |
| C12 — Context fidelity | No unexplained references to supplied material or conversation history; no editing-history language in finalized instructions; no copied example facts presented as requirements or current evidence. |

For C11–C12, preserve legitimate examples, provenance, and actual compatibility obligations. A specific word or long paragraph is not automatically a defect: identify the consequence and governing criterion. Review compositional overload, fragmentation, weak transitions, repetition, and contradictions as meaning-level findings rather than imposing word-count quotas.

## Per-skill procedure and persistence gate

1. **Establish the unit:** Inspect its baseline entry point, every reference/asset/metadata file, applicable provenance, and relevant inbound/outbound contracts. List inspected and excluded files in its report section.
2. **Assess the criteria:** Record C01–C12 outcomes and supporting locations. Cite baseline path and line/section, with short exact excerpts when necessary. Distinguish confirmed contradictions, evidence gaps, and optional recommendations.
3. **Exercise scenarios:** Use representative success, branch, failure, and boundary cases. For agent instructions, observe a consuming agent's actions or concrete disposition. For scripts/Git, execute controlled fixtures when needed. Record setup, inputs, expected behavior, observed output/effects, command exit status, and limitations. Static inspection alone is not runtime validation.
4. **Record findings:** Allocate stable IDs, add or update the global index and full finding records, link cross-skill effects, and update the unit's criterion coverage, evidence, unresolved questions, and status. A unit with no findings still requires a documented outcome.
5. **Validate the report update:** Check heading spacing, links, finding references, coverage, and consistency between summary and detail. Ensure no secrets or unsupported completion claims are included.
6. **Commit and push before the next skill:** Commit the report and only authorized review artifacts. Use a subject such as `Review sdd-design against 81011e7 (S04)`. Push to the established branch and verify remote containment. If pushing fails, preserve the commit, mark the campaign blocked in the next available report update, and do not advance to another skill until resolved. Do not force-push or overwrite concurrent work.
7. **Resume from evidence:** Read the last pushed report state and Git history. An interrupted unit remains In progress; an already assessed but uncommitted report is validated and persisted before advancing. Do not repeat finished units without a changed scope or uncovered gap.

The reviewing source snapshot remains fixed while report commits advance. The report's unit status describes coverage, not source correctness: **Reviewed** can coexist with open findings. Push verification belongs in the subsequent checkpoint row or Git history; do not embed a report commit's own SHA inside itself. Cite its report unit ID in the commit for lookup.

## Finding identity and revision contract

Assign global IDs `SDD-R-001`, `SDD-R-002`, and so on in discovery order across this campaign. Never renumber or reuse an ID; changing skill order, priority, or conclusion does not change identity. Use these IDs in summaries, criterion results, dependencies, revision commits, and validation records.

- **One root cause, one record:** Cross-skill instances belong to one finding with all affected paths. Link distinct dependent findings rather than duplicating them.
- **Traceability:** Each finding identifies its unit(s), criterion(s), category, priority, confidence, exact evidence, consequence, recommended correction, and objective recheck.
- **Evidence gaps:** Record unavailable checks in coverage even when no defect is established. Create an evidence-gap finding when missing evidence blocks a defined requirement or completion claim; do not turn every untested environment into a bug.
- **Meaning-changing proposals:** Identify changes to responsibility, workflow, authority, scope, or guarantees explicitly; return undecided design choices to the human instead of prescribing an unsupported requirement.
- **Lifecycle:** Start at Open. Subsequent revision can mark In progress, Addressed, Verified, Deferred, Rejected, or Duplicate. Preserve the original evidence and add the disposition rationale. Addressed means a correction exists; Verified requires the objective recheck and applicable regression evidence. Rejected requires evidence/reason; Duplicate links to the retained ID.

| Priority | Meaning |
| --- | --- |
| P0 | Observed immediate critical exposure or destructive behavior requiring suspension of the affected operation. |
| P1 | Major authority, data/state integrity, or core-workflow defect. |
| P2 | Material inconsistency, omission, or failure of a practical supported workflow. |
| P3 | Local clarity, composition, or maintainability issue with a concrete consequence. |

Record **Defect**, **Evidence gap**, or **Recommendation** separately from priority. Recommendations are not mandatory revisions unless accepted. Confidence is High, Medium, or Low with a reason; plausible unexercised behavior must not be presented as observed failure.

## Package and composition passes

### P01 — Package validation

- Inventory all packaged files; verify all 15 skills appear once and all loaded resources resolve within the intended package.
- Run the available Agent Skills/Agent Plugins validator and inspector, recording tool identity/version or source path, exact commands, baseline location, exit status, output, and limitations. Do not assume the previous review's tooling is present; report unavailable tools without silently installing them.
- Check heading spacing in instructions and Markdown templates, frontmatter, skill-name references, presentation prompt/name/icon consistency, SVG containment, retained licenses, and links.
- Assess discovery/portability claims without inferring client installation or display support from successful structural checks.
- Update, commit, and push the report before P02.

### P02 — Cross-skill and workflow synthesis

Build a compact producer/consumer matrix for authority, inputs, outputs, mutation ownership, task status, persistence, credentials, and stopping rules. Check both directions of each consequential handoff and resolve earlier deferred coordination questions.

Exercise initial preparation, feature preparation, bounded implementation, interrupted continuation, checkpoint steering, selected integration, focused review/maintenance, and hosted synchronization. Include combined requests and boundary-changing user instructions. Revisit the historical review's staged isolation, task transfer, older issue backlog, interruption routing, and taskless commit cases against this baseline.

For each workflow, distinguish static review, read-only agent assessment, executable local fixture, and authorized live execution. Record exclusions and provider/client dependencies. Deduplicate findings and link the affected skill units. Update, commit, and push before P03.

### P03 — Consolidation and revision handoff

- Confirm every skill/resource and C01–C12 criterion is accounted for; every skipped scenario has a reason and consequence.
- Reconcile the global findings index, detailed records, cross-skill matrix, scenario outcomes, unit coverage, and executive summary.
- Order the revision queue by risk and dependency, retaining stable finding IDs. Identify independent fixes, coupled changes, human decisions, and verification prerequisites.
- Separate source defects, recommendations, evidence gaps, external blockers, and completed checks. State the actual readiness conclusion and validation limits.
- Do not claim zero issues or approve the plugin solely because all review units are marked Reviewed.
- Validate, commit, and push the consolidated report. Return the report path, baseline, open findings by priority, blocked checks, and the revision queue to the subsequent agent.

## Revision follow-up

The accepted follow-up is retained in [REVISION-PLAN.md](REVISION-PLAN.md), with observed results in [REVISION-REPORT.md](REVISION-REPORT.md).

## Report structure and templates

Use the companion report's existing sections: campaign metadata, executive summary, unit progress, coverage/evidence by skill, package/composition results, global finding index, full finding records, scenarios, revision queue, and validation limits. Keep findings in one canonical record and link them from other views.

### Finding record template

```markdown
### SDD-R-001 — Short actionable title

| Field | Value |
| --- | --- |
| Type / priority / status | Defect / P2 / Open |
| Units / criteria / category | Sxx / Cxx / contract, workflow, Git, hosting, evidence, or editorial concern |
| Affected baseline locations | Paths and line ranges or section anchors at 81011e7 |
| Confidence | Level and basis |
| Evidence | Exact conflicting instructions or observed scenario/command results |
| Consequence | Supported effect on an actual workflow or reader |
| Recommended correction | Bounded change; identify any human decision needed |
| Recheck | Observable acceptance for the correction and relevant regression cases |
| Related IDs | Dependencies or duplicates; none when absent |
| Revision disposition | Initially not revised; later commits, tests, and rationale |
```

### Per-skill record template

```markdown
### Sxx — sdd-name

**Status:** In progress / Reviewed / Blocked.
**Inspected baseline files:** Entry, references, metadata, assets, and provenance.
**Relevant contracts:** Producers, consumers, authority, and handoff assumptions.

| Criterion | Outcome | Evidence / finding IDs / reason |
| --- | --- | --- |
| C01–C12, one row per criterion | Satisfied / Finding / Blocked / Not applicable | Located evidence or explicit exclusion |

**Scenarios:** IDs, evidence level, observed outcomes, and gaps.
**Findings:** Stable IDs or an evidence-bounded no-findings statement.
**Checkpoint:** Report unit/commit lookup, last known push verification, or blocker.
```
