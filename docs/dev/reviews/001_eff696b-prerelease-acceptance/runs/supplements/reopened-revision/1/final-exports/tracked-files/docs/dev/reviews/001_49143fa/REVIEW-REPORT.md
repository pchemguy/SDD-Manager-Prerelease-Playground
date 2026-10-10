# Plugin review

**Campaign:** `001_49143fa`. Current record: `docs/dev/reviews/001_49143fa/REVIEW-REPORT.md`. Established finding IDs and baseline evidence are retained.

Full reviewed baseline: `49143fa039c65e1d9c9e44d40eff470d729e2c8c`. This historical report also contains its corrections and verification; missing separate stage artifacts are not reconstructed.

Review date: 2026-09-30. Reviewed baseline: `49143fa`, plugin version `0.14.0`. Corrections in this review produce version `0.14.1`.

## Scope and method

- Read all 15 packaged skill entry points and their references, README, capability ownership map, manifest, presentation metadata, and retained TDD license/provenance.
- Review authoring, integration, execution, interruption, steering, verification, reporting, hosted projection, credentials, and cross-skill boundaries.
- Use independent read-only agent reviews for execution/hosting and document/testing contracts, followed by consuming-agent assessments of corrected scenarios.
- Run the agent-package-author plugin validator and package inspector, plus local heading, relative-link, skill-reference, metadata, SVG containment, and credential-material checks.
- Execute disposable Git fixtures for staged-file isolation, mixed-ownership hunk isolation, index/worktree preservation, and push containment against a local bare remote.

## Findings and corrections

| Priority | Finding | Correction |
| --- | --- | --- |
| P2 | Adding only owned paths before a normal commit still includes unrelated content already staged. Implementation and steering did not explicitly isolate that content. | Require staged-diff inspection and exclusion from the commit while preserving the unrelated index state. Document path-scoped commits for wholly owned file contents and temporary indexes for selected changes. Align the coordinator's persistence rule and inspect post-commit cached/worktree diffs to detect stale owned index entries after temporary-index commits. |
| P2 | Transferring feature entries with only TASKS selected can leave duplicate executable IDs in the unselected active FEATURE-TASKS. | Require both lists in scope for ownership transfer; retire each source checkbox in the same change. Permit TASKS-only reconciliation of existing main entries and defer transfers outside scope. Retained source navigation cannot be a duplicate executable checklist. |
| P2 | Inspecting only the resumed or latest task can miss older pending hosted closures after an outage. | Reconcile verified completed tasks within the established maintained tracking scope, including older pending references and closures. Use existing checklist, Git, and hosted evidence without adding a journal or blocking local work solely for a hosting outage. |
| P3 | Completion reporting assigned interruption decisions to an undefined recovery workflow. | Name orientation, manager coordination, and implementation continuation as the current owners. |
| P3 | The unconditional commit task-ID instruction conflicted with coordinator persistence of preparation or maintenance having no assigned task. | Always include the owning ID for task-associated commits; never fabricate an ID for unassigned preparation or maintenance. Name the coordinator as persistence owner outside active implementation. |

Clarify that the shared 403 escalation includes provider-indicated non-credential causes: the manager assesses credential suitability and other remedies without treating escalation as mandatory token substitution.

Normalize incidental sentence capitalization in the affected documentation, testing, and verification entry points. No additional skill, transaction artifact, issue map, PR operation, or hosting dependency is introduced.

## Verification results

| Check | Observed result |
| --- | --- |
| Plugin structural validator and full package inventory | All 15 skills valid; zero errors and warnings. |
| Local content and presentation checks | Heading spacing, relative resource links, referenced skill names, prompt invocation, short-description bounds, icon paths, and self-contained SVG XML passed. No credential-like material found in reviewed Markdown. |
| Path-scoped Git commit fixture | Commit included only the owned file; unrelated staged blob and unstaged file remained intact. |
| Temporary-index Git commit fixture | Commit included only the selected owned hunk; the original index remained byte-identical because the selected owned hunk was already staged there. Post-commit cached diff contained only the unrelated staged file; the worktree diff contained only the unrelated unstaged hunk, with no staged reversal of the committed owned change. |
| Local bare-remote push fixture | Remote branch SHA matched the resulting committed state. |
| Corrected coordination scenarios | Seven read-only consuming-agent assessments covered scoped/joint task transfer, older hosted backlog, staged ownership, taskless commit drafts, selection-only requests, and a policy-related 403. Expected boundaries were observed; the 403 result prompted the shared-protocol clarification above. |
| Independent contract review | Identified the staged-commit, task-transfer, older-closure, and stale-recovery issues above; no additional blocking conflict in the reviewed design, specification, planning, documentation, testing, or verification contracts. |

## Practical boundaries checked

- Clean worktrees with outstanding commits enter push-first implementation; selection-only requests stay read-only.
- Checked but uncommitted tasks retain implementation and require actual completion evidence before persistence.
- Main and feature task identities remain project-wide unique; ambiguous active scopes require resolution.
- Document-only integration leaves task lists outside scope unchanged and retains sources still needed by active work.
- Task transfer requires one executable owner and preserved status, dependencies, and evidence.
- Steering changes existing owners, creates no feature overlay, and returns control without resuming implementation.
- Verification reports gaps and failures without repairs or completion mutations; documentation defers governing amendments to the human.
- Hosted failures preserve local results; older pending closures are reconciled within maintained scope without duplicate writes.
- Tokens remain outside project artifacts and ordinary handoffs; backend access checks distinguish policy restrictions from replaceable credentials.

## Remaining validation limits

The behavioral Git fixtures exercised real local commands. Agent assessments exercised instruction selection and coordination in read-only scenarios; they did not execute a full project implementation or a live GitHub mutation. Structural checks do not establish installation or display behavior in any particular client. Live end-to-end workflow and provider integration validation remains separate work. External specification and provenance links were retained; this review did not revalidate their current remote contents or provider permission requirements.
