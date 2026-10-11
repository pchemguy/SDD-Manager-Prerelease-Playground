# Pre-release review plan

Campaign: **024_ed2d571**. Starting and reviewed source: **ed2d571d20aa8ad6ee77f25ad89602e82e6a653b**, version **0.14.6**. Date: 2026-10-06.

Working branch: `revision/024_ed2d571-pre-release-review`; source target: `feature/architecture-revision` (remote main currently also names the baseline). This review publishes report artifacts only. Source repairs, installation, a new live acceptance campaign and source integration are outside this request. Preserve unrelated untracked work. Reuse existing checkout; no clones and no /pyenv access.

## Ordered coverage

| Unit | Scope and criteria | Scenarios and evidence | Dependencies |
| --- | --- | --- | --- |
| U-001 | Package discovery, synchronized metadata, assets, licensing, declared format and skill structure | Inspect both manifests; validate all 15 skill entries and local paths; distinguish Codex metadata from portable Agent Plugins conformance | Baseline orientation |
| U-002 | Skill ownership, progressive disclosure and cross-skill workflows | Inspect every entry/reference; trace preparation gates, bounded execution/resume, feature ownership transfer, steering stop, verification, hosted lifecycle and authorization; positive and refusal scenarios | U-001 |
| U-003 | Harness correctness, safety and coverage | Run full support suite; inspect catalog/schema/variant grade and prerequisite logic, controlled recovery, package pinning, final evidence integration; reproduce credible findings without modifying source | U-002 |
| U-004 | Documentation, release evidence and independent consolidation | Check current links, prompts, diagrams and claims; reconcile independent source review; distinguish historical source, current support evidence, live-agent and installed-client evidence | U-001–U-003 |

## Evidence and checkpoints

Use source inspection, actual local support execution and a fresh independent reviewer under the requesting-code-review skill. A support check does not certify agent behavior. No live GitHub object mutation or installed-client activation is selected. Consult primary standards documentation only for actual compatibility claims. Record exact commands, output, tested state, findings with stable R-IDs, no-finding coverage and unavailable facilities.

After each unit update REVIEW-REPORT.md, commit the scoped evidence and normally push the checkpoint, verifying the exact remote ref before dependent work. Source remains pinned even as report commits advance. Keep independent findings separately attributed and reconcile against reproductions. Report proposed fixes; do not implement them during review.

## Completion

Consolidate severity, confidence and disposition, release readiness by declared target, proposed revision order and objective rechecks. Missing complex optional live/native facilities are non-blocking omissions, not manufactured source failures. Required consumer coverage and installed-client claims remain distinct evidence limits. Stop after publishing the final review report.

Execution status: all four planned units assessed on the pinned baseline. Findings, actual checks, independent attribution, limits and proposed next actions are retained in [REVIEW-REPORT.md](REVIEW-REPORT.md). No source revision executed.
