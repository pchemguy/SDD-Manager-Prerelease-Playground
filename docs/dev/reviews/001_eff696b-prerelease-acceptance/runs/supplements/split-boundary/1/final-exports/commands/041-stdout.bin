# Agent orientation

SDD Manager is an Agent Plugin for specification-driven development in Git repositories. This file is the entry point for agents working on this repository and for agents reading an installed SDD Manager package. Read [README.md](README.md) for capabilities, package contents and evidence limits.

## Source and instructions

- Workflow source: `skills/<skill>/SKILL.md` and its conditionally loaded references. Start coordinated work at [sdd-manage](skills/sdd-manage/SKILL.md); inspect the selected owner before edits.
- Metadata: root `plugin.json` is the canonical package manifest; keep `.codex-plugin/plugin.json` byte-identical for temporary legacy client compatibility. Artwork/templates live in `assets/`; package notices are `SDD-MANAGER.md` and `AI_DISCLOSURE.md`.
- Test tooling and fixtures: `acceptance/textstats/`. Read its [AGENTS.md](https://github.com/pchemguy/SDD-Manager/blob/main/acceptance/textstats/AGENTS.md) before touching or executing that scope. A support-suite run is distinct from a live acceptance campaign.
- Retained development evidence: [review/revision index](https://github.com/pchemguy/SDD-Manager/blob/main/docs/dev/reviews/README.md). This repository has campaign plans/reports rather than a root project TASKS owner; do not invent executable task IDs from findings. Current work/branch state is discoverable through Git and the selected campaign record.

When installed as a package, use this file for package-level orientation and then load the selected skill's `SKILL.md` plus only the references it requires. When working on the SDD Manager source repository, also read applicable nested AGENTS.md before work on its paths. If your host does not discover this entry point, load it explicitly. Keep maintained navigation accurate without overwriting controlling human instructions.

Use current source and the active campaign for routine work. Prior closed review/feature/steering records are frozen history, except the selected eligible revision campaign explicitly reopened under [revision modes](skills/sdd-manage/references/revision-modes.md): do not load their contents without a specific current need, edit them, or check/report their compatibility with subsequent changes. Discover identities/paths without reading contents and verify preservation from Git path/object diffs. See [closed campaign records](skills/sdd-conventions/references/review-campaigns.md#closed-campaign-records).

## Verification and persistence

Apply the shared [Markdown style](skills/sdd-conventions/references/markdown-style.md) to authored or maintained documents: blank lines after every heading and around top-level lists and code blocks, plus four spaces per structural indentation level, including nested lists, and exactly one space after each list marker. Preserve literal code/data syntax and closed records.

From repository root, run the support suite for changes affecting acceptance tooling and for coherent plugin boundary integration:

```text
python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v
```

Use Python 3.11 or the established supported runtime; release CI uses 3.11. Check changed Markdown links, manifest synchronization, presentation asset paths and actual package contents as applicable. State the tested source and evidence limits; passing support tests do not establish live agent/client acceptance.

For task-list execution, follow the [task commit contract](skills/sdd-implement/references/completion-and-checkpoints.md#task-commit-contract): one executable task's closing result/evidence and initial checklist completion in the same commit, with a leading single owning task ID. Non-task campaign actions and merge commits do not invent task IDs. Use the linked audit/recovery rules for continuation and integration.

Push every workflow-owned commit and verify remote containment before further project work or another commit; do not accumulate commits in the sandbox. Pause on an unresolved push. Honor explicit user-directed local-only/deferred publication within its stated scope. See [per-commit publication](skills/sdd-manage/references/git-workflows.md#publish-each-commit).

Follow [Git integration and recovery](skills/sdd-manage/references/git-workflows.md) and the user's scope/stopping boundaries. Preserve unrelated changes; stage owned paths only. Completed authorized workflows include normal checkpoint pushes and eligible verified integration. Never force-push or reset unrelated work. Keep credentials out of source, reports and handoffs; use existing protected authentication.
