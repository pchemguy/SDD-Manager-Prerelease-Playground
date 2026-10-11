# Core development workflows revision report

## Campaign and state

- **Campaign:** `006_0393fee`; date 2026-10-02.
- **Starting baseline:** `0393fee5382be42465c7089924f315f0f6f44f7e`.
- **Execution checkpoint:** `124b5e29543e740817699851de82ab6ac35db30d`.
- **Plan:** [REVISION-PLAN.md](REVISION-PLAN.md).
- **Working branch:** `revision/core-workflows-006`; target: `feature/architecture-revision`.
- **State:** Completed; V-001–V-003 verified within recorded limits, explicitly merged, and target publication verified.

## Revision evidence

| Action | Actual changes and observed checks | State / limits |
| --- | --- | --- |
| V-001 | Added canonical three-workflow model before an explicitly named operation catalog; linked formal revision and lightweight steering without duplicating procedures. Inspected entry, document optionality, authorization, branch meaning, and steering stop boundaries. Changed Markdown and affected package checks passed. | Source revised; composed consumer assessment pending. |

| V-002 | Aligned README overview and capability map with the canonical model and lightweight revision distinction. Inspected short/full overview consistency; package, heading/link, and diff checks passed. Corrected broad untested-hosting status to distinguish prior isolated issue test from untested complete hosted tracking. | Source aligned; final consumer assessment pending. |

| V-003 | Fresh consumer routed all six scenarios with correct preparation, ownership, branch identity, and stop boundaries. All 15 skill/plugin validators, inventory, metadata/icon, changed heading/link/anchor, diff and tracked credential checks passed. | Verified as source composition and consumer interpretation; no consumer runtime execution claimed. |

## Checkpoints

- V-001: `c073a3932dc40771b3109c4bd373ca4333f1367f`; push and remote HEAD equality verified.

- V-002: `6f3cd7260f8ceacc12fef98fe954654c9880b227`; push and remote HEAD equality verified.

Action reports are committed/pushed with their source; remote containment is verified before dependent actions. Subsequent evidence records preceding exact SHAs.

## Limits

Documentation/source interpretation checks do not establish consumer runtime execution. No consumer production code, live hosted object, credential policy, task ownership, or transaction workflow is changed. Working-branch and prospective merged-state checks passed; target publication verified.

## Structural verification

- `python /tmp/sdd006-check.py`: changed Markdown headings, relative links, credential patterns, and `git diff --check` passed. File/template starts need no leading blank.
- `python <agent-package-author>/scripts/validate_skill.py skills/<name>`: all 15 bundled skills passed.
- `python <agent-package-author>/scripts/validate_plugin.py .`: passed; package inventory reported 15 skills, zero errors and zero warnings, runtime unverified.
- Inline Python: presentation YAML prompt/skill names and icon paths, all SVG parsing, changed local heading anchors, and tracked-text credential-pattern scan passed. Existing affected presentation descriptions still match responsibilities.
- Source composition: reviewed the full boundary diff against `124b5e2`; ownership, MVP-first strategy, task/feature identity, push-first execution, token convention, explicit integration, and human-controlled steering remain intact. Added explicit instructions to omit nonexistent review stages/finding IDs for a directly accepted prompt-defined revision.

## Integration

Fetched target before integration; it was up to date. `git merge --no-ff --no-commit revision/core-workflows-006` created the prospective merge. Changed Markdown/link/credential checks, plugin validation and staged-diff whitespace passed before the explicit commit.

- **V-003 tip:** `0b127d73b966e76714a5dd5363db51b789839b4a`; working-branch remote equality verified.
- **Merge:** `2188b8ffc2418bd25ae58087abffd8b734ad5961`.
- **Target parent:** `124b5e29543e740817699851de82ab6ac35db30d`.
- **Revision parent:** `0b127d73b966e76714a5dd5363db51b789839b4a`.
- **Publication:** Target push succeeded; remote HEAD equaled the merge SHA. Two-parent integration and source-boundary containment verified.

This final retained evidence/navigation checkpoint changes no skill sources.

## Consumer scenario evidence

A fresh consumer read only the relevant skill entries/references, without campaign artifacts or intended answers. It received the six project requests below and returned routing decisions; it made no file changes and used no credentials/network. The source clarification for direct prompt revisions was additionally inspected after the consumer began.

| Scenario | Observed interpretation | Evidence limit |
| --- | --- | --- |
| SC-001 | Routed new-project preparation to main/greenfield, design/spec/plan/tasks, and stopped before implementation. | Routing response, not generated consumer project. |
| SC-002 | Entered accepted existing TASKS directly, selected two eligible tasks, preserved push-first and established target independently of the named working branch. | No task execution or Git fixture run. |
| SC-003 | Entered accepted correction directly through revision planning, without fabricated review/report; amended governing inputs through owners and retained bounded verification/integration. | Interpretation and source check; desired contract treated as explicit human input. |
| SC-004 | Routed ZIP addition to feature, reused sufficient design, prepared only needed deltas and active tasks, and stopped at the first two tasks without unrelated full-feature incorporation. | No actual feature package/implementation generated. |
| SC-005 | Routed removal at paused checkpoint to lightweight revision/steering; amended existing documents, created no feature overlay, targeted paused branch, and returned control without resume. | No production amendment executed. |
| SC-006 | Routed specification review to read-only behavioral assessment with no repairs, completion updates, or integration. | No full project review performed. |

The consumer distinguished core purposes from operations and branch names. Default scoped explicit integration, optional stage entry, preserved task ownership, and steering's human-controlled stop remain intact. This establishes instruction interpretation for the scenarios, not installed-client enforcement.
