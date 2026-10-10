# Phase 2 review — ranges, UTF-8 stdin and final delivery

## Identity, authority and candidate state

Owning final review task: T-017. This is the pre-integration review artifact:
Phase 2 implementation and applicable final exits are verified at published
`phase/2-json-and-stdin` source `b49a26b36d68dc9bab8cf83633f5b7a2aae81eea`.
Concrete delegated acceptance of this report and the
[final implementation report](../../IMPLEMENTATION-REPORT.md), task persistence,
own review-milestone closure and prospective main integration are pending at this
candidate checkpoint. No target merge/publication is inferred.

Current [SPEC](../../../SPEC.md), [PLAN](../../../PLAN.md), canonical
[TASKS](../../../TASKS.md) and adjacent current QC govern. Explicit resume and
published startup acceptance `fb98e7b984134755845fc46390381d9933aa397e` cover the
remaining five owners after accepted amendment
`77e7106e3134cc7053a2b1a045cf1a76cf0361ea` / publication acceptance `963d058`.
The exact milestone 2.2 report candidate was accepted/published at coordinator
`9338f067a575511b6d818a6898a458957f4670a8`, then committed/published as T-016
`b49a26b36d68dc9bab8cf83633f5b7a2aae81eea`.
R-009/JSON delivery is withdrawn; historical identities/reviews remain retained.

Fresh provider GETs established prerequisite native milestones #5 (2.2), #7 (2.4),
#8 (2.5) and #9 (range feature review) closed with zero open issues and matching
original IDs/titles. Milestone #5 closure followed exact published T-016 readback,
issue #17 closed/completed and full all-state associations #14–#17, each closed/
completed with phase label and expected ownership, no extra associations,
pagination or PRs. Native fields were preserved. The accepted existing phase-label
description correction changed only description, with fresh before/after readbacks
and ID/name/color/all other fields preserved. Own final-review milestone #6
remains open until this task's publication and issue #18 closure.

## Delivered phase and retained behavior

Named-file and stdin input support exact text counts and both BOM policies.
The inclusive line-range grammar validates before acquisition, accepts unbounded
positive ASCII decimals and leading zeros, preserves available logical segments
and exposed interior BOMs, and decodes complete bytes even beyond END.
Borrowed stdin reaches EOF with strict locale-independent UTF-8 and stays open;
owned file handles close on all paths. Input/decode failure gives identifying
stderr/status 1 without partial stdout or traceback. Usage failures give status 2
before source access. Empty input and beyond-EOF selection count zero/zero.

The Phase 1 API retains exactly TextStats/count_text/count_file, immutable
nonnegative integer values excluding bool, silent whole-input functions and
keyword-only BOM policy. Module help, option positions and dash-prefixed filenames
remain usable; `-` denotes stdin even after `--`, while `./-` selects a dash file.
Removed JSON options are unknown usage; a literal `--json` filename remains usable
after option termination. No new public range/stream parameter or export exists.

Public README/API instructions and docstrings describe final delivered behavior.
The unchanged eleven-file source allowlist contains package, public docs/notices
and builder/checker; actual extraction invokes the real module with isolated
imports for named-file and byte-fed stdin success/ranges/failures.

## Separate cross-phase implementation code review

This final review freshly inspected the integrated package and tools as a
cross-phase capability, separately from test execution and from the earlier
milestone review. Current relevant tests and public instructions were assessed
against the complete R/F matrix; the T-016-to-current product bytes are unchanged.

| Cross-phase interaction | Assessment |
| --- | --- |
| Phase 1 values/API with later acquisition | Frozen/slotted validated values and whole-input silent signatures remain direct. count_file retains owned binary acquisition and unchanged OSError/decode exceptions; the stdin reader stays internal. |
| Range feature with both sources | The controller performs complete strict acquisition, once-only whole-input BOM normalization, preserved shared selection and normalized counting. No selected-content second normalization exists. Huge endpoints are comparison values, not acquisition/loop limits. |
| Parser/help with failure paths | Exact options and duplicate/ASCII/order checks run before file/stdin access. Unsupported/removed options and invalid range cannot produce partial counts. Expected acquisition failures alone are translated; named identity or stdin/cause/status remain coherent. |
| Source/module/distribution boundary | Minimal module adapter returns controller status. Independent discovery excludes workflow fixtures and rejects zero suites. Allowlisted extraction clears inherited import paths, disables user site, checks imported location and exercises real byte-fed module entry rather than checkout counters. |
| Instructions and scope | Public docs agree with final code, including both source lifetimes and complete decode after END. Historical feature/JSON/amendment reports remain checkpoint records rather than current executable owners; no release, new phase or version is introduced. |

No new bug, critical issue, contract violation or missing required exit evidence
was located. No production repair was required by this final review.
The bounded task-persistence audit inspected T-013–T-016 subjects/diffs/ancestry:
each has one leading owning task ID, exactly its own initial checkbox, current
evidence and complete result, separately published/read back. T-017 receives the
same composition audit at closing and before integration. Protected resources
and historical Phase 1/JSON/range/revision paths have an empty object/path diff
from the accepted resume baseline; closed records were not compatibility-tested
or changed.

## Fresh final verification

Actual repository-root campaign:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B /workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py python -B /workspace/scratch/46b31bb4dff6/037-a013-consumer-docs-retry.py
```

It returned 0 and executed every one of twelve current README/API fences. Actual
product tests/checker commands were run through the external immutable trace
wrapper, preserving their full argv/cwd/separate raw streams/status/inputs/hashes.
The full runner and separate documented discovery each passed 37 unit and
34 integration tests, no skips/warnings; rebuilt isolated distribution passed
478 actual module cases plus exact import and silent API/signature probes.
The explicit eleven archive members exactly matched current source bytes, SHA-256
`4fcf4a60d08f4a8c2a69a0b2d567de70c5a554e2249eb0f101f18c5340b7349c`.
All 2,776 fresh recorded Python children used `-B` and
`PYTHONDONTWRITEBYTECODE=1`; final temporary example inputs are independently
confirmed absent. Original failures/gaps remain external rather than rewritten.

Coverage includes full-input/value/Unicode/terminator/BOM/API/file regression,
borrowed/owned read/decode/lifetime seams, both sources/range spellings/policies,
all acceptance anchors, option order/input positions, huge/leading-zero endpoints,
EOF subsets, bad bytes after END and usage-before-acquisition. Real byte-fed
non-ASCII stdin ran under C and C.UTF-8 with Python UTF-8 mode/coercion disabled.
Archive mutants are rejected for wrong counting, removed-option acceptance,
ignored ranges, second BOM normalization and disabled stdin.

All documented count/status/stream assertions pass. Useful examples produced
stdin counts 3/5, 1/1, 2/3, 1/1 and 0/0; bad complete bytes after END gave clean
status 1. Actual extracted named-file/stdin-range examples produced 3/5 and 2/3.
The unchanged public guide's local links resolve. Current source identities and
report links/headings/whitespace are checked in this task's closing evidence.

## Findings, TODO and limits

[Final implementation report](../../IMPLEMENTATION-REPORT.md#findings-and-todo-aggregation)
deduplicates relevant milestone/phase findings with source/repair references:
M1.2-001, M2.2-001 and M2.2-002 are resolved; EVID-A010-001/002 are resolved
historical evidence/tool interventions. All relevant milestone/phase TODO sections
report no deferred code item. Retired JSON and the closed removal amendment were
read only for this specific TODO/provenance question; JSON was not re-executed.
Prior ambiguous/truncated/failed observations and unknown lost first channels
retain their limitations; successful fresh checks do not reconstruct them.

TODO: None.

Python 3.12.14 and this Unix environment are verified; the full declared Python
3.11+/platform matrix is unverified. Portable controlled seams establish read/
ownership behavior without claiming real permission coverage on every platform.
External notice links, installed packaging and release operations are outside
these exits. Complete in-memory decode is the accepted tradeoff, not a bounded
memory or benchmark claim.

## Exit and publication boundary

Current R-001–R-008/R-010–R-013 and retained F-001–F-004 exits pass.
R-009 remains withdrawn with stable identity and historical evidence.
This final owner supplies the two required substantive reports and all active
task/parent completion status in one accepted closing boundary; retired T-010–
T-012 gain no checkbox or new completion.

Fresh remote main readback is
`fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`. After report acceptance, commit/push/
exactly read back T-017, close issue #18, verify full native milestone #6 association
and close/read back that review milestone. Then refresh the target, audit the
complete prospective difference/persistence, and present the concrete two-parent
integration candidate for delegated acceptance. Verify the prospective merged
state, commit the accepted merge, immediately publish/exactly read back main and
retain the phase branch. Actual final parents/checks/publication belong in the
merge body and externally required final seal, not an invented future SHA here.
Stop after published completed Phase 2; no subsequent task/phase, version or release.
