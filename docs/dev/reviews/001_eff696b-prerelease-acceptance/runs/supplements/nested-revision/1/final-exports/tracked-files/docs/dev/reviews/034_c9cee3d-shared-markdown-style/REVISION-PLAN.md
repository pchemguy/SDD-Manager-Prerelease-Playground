# Shared Markdown style revision plan

## Campaign and decisions

- Campaign: `034_c9cee3d`; directory: `034_c9cee3d-shared-markdown-style`.
- Starting baseline: `c9cee3dc61ab3362b30d449d25852e8f35ee70b5`.
- Review checkpoint: `4a8fa3b`; [review report](REVIEW-REPORT.md).
- Working branch: `revision/034_c9cee3d-shared-markdown-style`; integration target: `main`.
- Accepted requirements: R-001 and R-002, directly supplied by the user.
- State: planned; implementation has not started. Version remains `0.15.0`.
- Publication: the review push was rejected by host automatic approval review. Publish and verify the planning checkpoints before dependent source execution. Authentication or an alternate transport does not resolve that denial.

## Shared rule and scope

Add a focused `sdd-conventions/references/markdown-style.md` reference, discoverable through the convention catalogue. Apply it whenever SDD Manager authors, revises or reviews Markdown, including PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, layout, TASKS, focused children, feature counterparts, active campaign/QC/implementation reports, README/guides, AGENTS.md, skill instructions/references, templates and hosted Markdown drafts.

1. Put a blank line after every Markdown heading, regardless of whether the following content is prose, another heading, a list, a table or a fenced block. Cover ATX and Setext headings. Retain the existing blank-line separation before headings where applicable; no leading blank line is required at the beginning of a document/template.
2. Use four spaces per structural indentation level, never tabs. Indent each nested list level four additional spaces relative to its parent, for bulleted, numbered, mixed and task lists. Keep continuation paragraphs and nested blocks attached to their list item with valid Markdown indentation; account for marker width when necessary.
3. Apply these rules to Markdown examples/templates intended to generate documents. Preserve literal source code, data and verbatim material according to their own syntax; do not mechanically alter Python, YAML, shell or other embedded languages. Fenced Markdown templates are Markdown content for style checks, while fences containing executable code are not.

The convention supplies presentation criteria, not new artifact ownership, workflow authorization or acceptance gates. TASKS retains its phase/milestone/task checklist semantics. Closed campaign records remain unchanged and excluded from formatting checks and repair. No historical compatibility work is introduced.

## Ordered revisions

| Action | Findings | Outcome and affected owners | Dependencies | Recheck |
| --- | --- | --- | --- | --- |
| V-001 | R-001, R-002 | Add the focused shared reference and catalogue trigger; give concise heading/list examples and syntax boundaries. | Published planning checkpoint | Both rules and general scope are explicit; examples use blank lines and four-space nesting. |
| V-002 | R-001, R-002 | Connect manager coordination and direct design, specification, planning/layout, tasks, documentation, reporting and verification calls. Reconcile forge Markdown output and affected feature integration/steering/implementation handoffs. Replace redundant generic policy with links where useful, retaining task-specific semantics. | V-001 | Every Markdown author/reviewer route can discover the rule without relying on the manager alone or loading unrelated references. |
| V-003 | R-001, R-002 | Inspect and normalize maintained current plugin Markdown, root documentation and active campaign material, including Markdown templates; add scoped QC checks through existing owners. Preserve rendering, semantics, code/data syntax and closed records. | V-002 | Positive/negative scenarios below; changed links and Markdown structure checked; protected paths unchanged. |
| V-004 | R-001, R-002 | Verify composed guidance and committed-source packaging; complete revision report and current navigation; explicitly merge the complete verified tip, verify and publish the target. | V-003 | Required support suite and package checks pass; version/manifests unchanged; merged tree contains all campaign evidence; remote refs verified. |

## Verification scenarios

| Scenario | Expected result |
| --- | --- |
| SC-001: heading followed by prose, heading, list, table or fence | A blank line separates each heading from subsequent content. |
| SC-002: Setext heading | Blank line follows its underline; parser does not mistake a horizontal rule or code content for a heading. |
| SC-003: top-level and multi-level bullet list | Top-level item remains at its proper container position; each child adds exactly four spaces. |
| SC-004: numbered and mixed nested lists | Same four-space nesting; marker-width and continuation attachment remain valid. |
| SC-005: TASKS and FEATURE-TASKS | Phase/milestone/task remain at zero/four/eight spaces with unchanged IDs, parentage and status. |
| SC-006: list continuation paragraph or fenced block | Continuation/block stays attached to its intended item without becoming an accidental sibling or code block. |
| SC-007: Markdown template inside a fence | Template headings and lists satisfy the shared rules. |
| SC-008: executable code/data fence or verbatim excerpt | Syntax/significant whitespace is preserved; Markdown checks do not reindent its literal contents. |
| SC-009: direct document-owner or reporting call | Shared style is applied without requiring a prior manager invocation. |
| SC-010: closed historical campaign | No content loading for routine style checking, formatting, repair or compatibility report; Git path/object diff proves preservation. |

Use scoped inspection/rendering or syntax-aware checks appropriate to the actual changes; do not claim regex matches prove correct nesting or rendering. Run the repository's required support suite at coherent plugin integration and verify the real package includes the new reference. Passing structural/source checks do not establish live consumer behavior. No new linter dependency is required by this plan.

## Execution, persistence and stopping

The current request covers the review and campaign opening/planning. Stop before source implementation. On a later execution instruction, retain this branch/identity and the user's two rules, publish pending planning checkpoints first, then execute actions in dependency order with their evidence and ordinary checkpoint persistence. Finish the full report before eligible integration so no campaign commit is left outside the merge.

No version bump, release/tag creation, full TextStats acceptance, unrelated style overhaul or historical-record edit is included. Publication remains blocked until the host permits the authorized destination and payload; local review and planning are complete.

## Reopened amendment — list and code-block separation

The user explicitly reopened this campaign on 2026-10-09 after integration/publication at `8b9749c75b56eff028fee1575fdeaf917fe5d7f0`. The original review, accepted rules and execution evidence remain provenance; this amendment is authorized for immediate implementation, verification, report amendment and publication. The established campaign branch is refreshed from that published main baseline. Other closed campaigns remain frozen.

Add two shared presentation rules to the same owner:

- Place a blank line before and after an entire top-level, non-indented list. The list includes its nested items and continuation blocks. Do not require extra blank lines around nested lists or between ordinary list items.
- Place a blank line before and after code blocks, including fenced and indented blocks and blocks nested inside list items. Preserve list attachment and literal code/data indentation. Document boundaries need no artificial leading blank line; a final list or fenced code block still has a trailing blank line.

| Action | Outcome | Verification |
| --- | --- | --- |
| V-005 | Extend the shared convention, its Markdown example, scoped QC guidance and concise entry-point summaries; normalize affected maintained current documents/templates. | SC-011: top-level bullet/numbered list separation; SC-012: compact nested lists remain valid; SC-013: fenced/indented code separation; SC-014: nested code stays attached and code bytes preserved. |
| V-006 | Extend local verification, run required support/package checks, append amendment evidence to this report and update current navigation; explicitly merge and publish the complete tip. | Positive/negative spacing fixtures, current-source checks and package bytes; merged-state suite and clean Git/remote readback. |

Keep version `0.15.0`, artifact ownership, human acceptance boundaries, task identities and literal source semantics unchanged. No new formatter/dependency or live acceptance is required. Stop after verified integration/publication of this amendment.

## Reopened amendment — one space after list markers

The user reopened campaign 034 again on 2026-10-09, from published main `77a82e04842f6f80bf770b359fc85ab40b77a74f`, to require exactly one space after list markers. This continuation retains the campaign identity and authorizes planning, execution, report amendment and verified integration/publication. Other closed campaigns remain frozen.

Use exactly one ordinary ASCII space between a Markdown list marker and its content at every nesting level: `- item`, `* item`, `+ item`, `1. item` and `1) item`. For a task item, the list-marker separator is the space between the bullet and checkbox, as in `- [ ] task`. Do not use multiple spaces or tabs after markers to align text. Four-space indentation before nested markers and valid continuation attachment remain unchanged. Literal code/data, verbatim material, horizontal rules and YAML metadata are not list markers to normalize.

| Action | Outcome | Verification |
| --- | --- | --- |
| V-007 | Add the shared marker-spacing rule, reconcile affected summaries/QC and inspect maintained documents/templates for violations. | SC-015: one-space acceptance and multiple-space/tab rejection across marker types, nesting and task items. SC-016: code/data/horizontal-rule exclusions and Markdown-template inclusion. |
| V-008 | Persist verification and amend the report/navigation; explicitly merge and publish the complete tip. | All local scenarios, mandatory support suite, committed package byte/checksum validation and merged-state verification. |

Version stays `0.15.0`; no new formatter/dependency or live acceptance is included. Stop after verified integration/publication of this amendment.
