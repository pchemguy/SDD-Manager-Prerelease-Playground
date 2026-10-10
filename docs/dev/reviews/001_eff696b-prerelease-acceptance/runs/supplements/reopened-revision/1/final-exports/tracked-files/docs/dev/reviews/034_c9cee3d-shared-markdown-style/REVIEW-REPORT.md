# Shared Markdown style review

## Campaign and assessment

- Campaign: `034_c9cee3d`; directory: `034_c9cee3d-shared-markdown-style`.
- Starting and reviewed baseline: `c9cee3dc61ab3362b30d449d25852e8f35ee70b5`.
- Working branch: `revision/034_c9cee3d-shared-markdown-style`; target: `main`.
- Reviewer/date: coordinating agent, 2026-10-09.
- Scope: current shared conventions and Markdown authoring/review handoffs. User criteria: a blank line after every Markdown heading and four-space indentation, including nested lists, applicable to all documents.
- Evidence: current-source inspection and targeted text search; no external research or live consumer execution.
- State: focused review complete; shared policy additions are authorized for planning, not implemented.

## Coverage and findings

| Criterion | Current evidence | Outcome |
| --- | --- | --- |
| Blank line after every heading across all document workflows | `sdd-docs/SKILL.md`, `sdd-docs/references/standalone-documentation.md`, `sdd-report/SKILL.md`, and `sdd-forge/references/github-projection.md` require blank lines around headings. | Local coverage exists; universal shared ownership/entry is absent (R-001). |
| Four-space indentation, including all nested lists | `sdd-tasks/SKILL.md` and `sdd-tasks/references/task-derivation.md` specify four spaces per checklist level; `conformance-review.md` checks that hierarchy. | Explicit coverage is limited to task checklists (R-002). |
| Shared discoverability | `sdd-conventions/SKILL.md` lists focused reusable conventions but no Markdown style convention. | Both rules need one discoverable owner with author/reviewer handoffs (R-001, R-002). |

### R-001 — Heading spacing is expressed as local workflow guidance

- Type/priority/confidence: policy coverage gap; medium; high from inspected source.
- Evidence: the four local instructions above already separate headings from adjacent content with blank lines. The shared convention catalogue has no Markdown-wide entry, and design/specification/planning owners do not route this rule through a shared style reference.
- Consequence: direct authoring of other documents has no explicit common style obligation.
- Accepted correction: elevate the existing rule into shared Markdown guidance for every authored or maintained document, including examples/templates, main and feature documents, active reports, skills/references, README/guides and Markdown hosted drafts. Retain the existing before-heading rule; explicitly require a blank line after each heading.
- Recheck: shared rule is reachable from document owners and direct calls; examples with prose, a list, another heading or a fence immediately following a heading are identified and corrected within authorized current scope.
- Disposition: accepted in planning; verified by V-001 through V-004 at the source/local fixture level. See [revision evidence](REVISION-REPORT.md). Baseline observations above remain unchanged.

### R-002 — Four-space indentation is confined to task checklists

- Type/priority/confidence: policy coverage gap; medium; high from inspected source.
- Evidence: the task owner specifies phase at column zero, milestone at four spaces, task at eight, and exactly four spaces per child level. Targeted searches find no equivalent general-document requirement.
- Consequence: other nested bullet, numbered and mixed lists can use inconsistent indentation despite the requested global style.
- Accepted correction: define four spaces per structural indentation level, spaces rather than tabs, and four additional spaces for each nested list level, with valid continuation/block attachment. Keep TASKS hierarchy semantics with its owner and connect it to the shared style rule.
- Recheck: ordinary, ordered, mixed and task lists follow the same nesting rule; continuation paragraphs and nested blocks remain attached to their item. Preserve literal code/data indentation inside code examples according to their language instead of reformatting executable syntax as Markdown.
- Disposition: accepted in planning; verified by V-001 through V-004 at the source/local fixture level. See [revision evidence](REVISION-REPORT.md). Baseline observations above remain unchanged.

## Limits and revision handoff

Review assessed articulation and ownership of the two requested rules, not an exhaustive formatting audit of every file. No rendering or live agent behavior was tested. No code, manifests, version, tests or closed campaign records were changed. Prior campaign contents were not loaded for this review.

Prepare one shared convention, wire authoring and verification entry points, reconcile local repetitions and inspect current examples. Normalize maintained current documents within the accepted execution scope; closed campaign records remain excluded. No new formatter, dependency or unrelated style policy is required.
