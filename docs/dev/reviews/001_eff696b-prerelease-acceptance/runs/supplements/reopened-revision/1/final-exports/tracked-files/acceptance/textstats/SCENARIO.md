# TextStats sample scenario

TextStats is a deliberately small **plugin test project**. Named-file counting yields an early useful end-to-end MVP; JSON makes an independent increment; ranges exercise feature preparation, selected incorporation and task transfer; JSON removal exercises subtractive steering and retirement; stdin tests explicit continuation against amended requirements. Failure forks exercise publication, verification and interrupted ownership without damaging the successful product branch.

Consumers receive [the preparation brief](cases/consumer/preparation.md) and their selected request, not this coordinator document or assessor answers. Preparation must express the following chosen requirements in ordinary product artifacts and derive its own task IDs. Do not copy completed historical documents, commits, issue numbers or task IDs into the new run.

## Product environment and organization

Use Python 3.11+ and standard-library `unittest`, with no third-party runtime dependency, network service, database or performance claim. Record the actual interpreter; executing a newer interpreter does not prove 3.11 was tested. Product code is importable as `textstats`; module CLI is `python -m textstats`. Product tests are organized under **`tests/unit/` and `tests/integration/`**, as discoverable packages with nonzero collection. Workflow harness/fixture checks are separate under `tests/workflows/`. Maintain professional module/public API docs, a runnable README and an extracted source-package module-entry check.

## Review and reporting boundaries

The consumer derives its own stable review task IDs under the pinned plugin policy: each delivery milestone ends with a milestone review/testing/report task, and each phase ends with a dedicated one-task phase review milestone. Product milestone numbers below name delivery outcomes; reserve a subsequent phase review milestone without renumbering those outcomes. Main milestone/phase reports share docs/dev/reports/phases/<actual-phase-id>/; steering records use its revisions/<actual-revision-id>/ subtree; feature reports stay under docs/dev/features/<actual-feature-id>/. Check code review, required tests, committed report and hosted closure as separate evidence. Deferred non-critical findings must retain remedy options through phase and final reports.

## Counting and API

Export immutable `TextStats(lines: int, words: int)` with nonnegative values, `count_text(text: str, *, strip_bom: bool = True) -> TextStats`, and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats` directly from `textstats`. API operations count the whole input; range selection adds no public API parameter/export. Calls emit no stdout/stderr. File decoding is strict UTF-8; missing/unreadable input raises an `OSError` subtype and bad bytes raise `UnicodeDecodeError`, with no partial result. Close owned file handles on every outcome.

Remove exactly one leading U+FEFF when `strip_bom=True`; preserve interior BOMs and all BOMs when false. CRLF is one terminator; lone CR/LF also terminate lines. Empty post-BOM input has zero lines. Each terminator contributes a line, and a nonempty final unterminated segment contributes one; no phantom line after a trailing terminator. Other Unicode separators do not terminate lines. Words follow Python `str.split()` Unicode whitespace semantics. Retained BOM is an ordinary non-whitespace character.

Literal contracts below are chosen sample requirements. Assessors use literal expectations independently of production code; consumers receive requirements, not checker implementations.

| Input (escapes represent characters) | lines | words |
| --- | ---: | ---: |
| empty | 0 | 0 |
| `alpha beta` | 1 | 2 |
| `alpha\n` | 1 | 1 |
| `\n` | 1 | 0 |
| `alpha\r\nbeta\rgamma\n` | 3 | 3 |
| `alpha\n\n` | 2 | 1 |
| space then tab | 1 | 0 |
| `alpha` + U+2028 + `beta` | 1 | 2 |

## CLI and increments

Baseline invocation is `python -m textstats [--keep-bom] INPUT`; `--` permits a dash-prefixed filename. Exactly one input is required. Help exits 0. Success exits 0, emits exactly `lines=<N> words=<N>\n` on stdout and no stderr. Missing/unreadable file or invalid UTF-8 exits 1, with useful nonempty identifying stderr, no success stdout and no traceback. Usage failures (missing/extra input, unknown option) exit 2 with useful stderr, no success stdout/traceback. Files remain unchanged.

Deliver Phase 1 milestone 1.1 as useful named-file API/CLI counting. Milestone 1.2 establishes failure handling, API/module docs, README and distribution exits. Integrate Phase 1 only when all exits pass.

Phase 2 milestone 2.1 adds `--json` while preserving default text output. JSON stdout is a single JSON object followed by newline with integer `lines` and `words`, no additional semantic fields, matching literal counts; formatting/key order is not constrained. Pause before stdin work.

Prepare the range feature at that paused Phase 2 checkpoint. Named-file text/JSON range delivery is its exit; source-independent selection compatibility with **future stdin** is a design constraint. Actual stdin acquisition/tests/integration belong to the later stdin milestone and must not inflate feature prerequisites.

Steering assesses, then on a separate explicit command removes JSON. Amend existing docs/code/tests and retired task ownership directly, preserving text/counting/ranges; use no feature overlay. After removal `--json` is a usage error (2), before input acquisition; a literal filename `--json` still works after `--`. Stop after amendment integration. Only a subsequent explicit case request resumes stdin work.

Phase 2 milestone 2.2 adds stdin through `-`, retaining named files and all retained range/BOM behavior. Read bytes until EOF and decode UTF-8 independent of locale; do not close stdin. Empty stdin is (0,0); read/decode errors use status 1 and identify stdin. Complete final phase exits and explicitly integrate; no third phase is implied.

## Range contract

Invocation adds one `--lines START:END` or `--lines=START:END`. Endpoints are positive ASCII decimal integers, inclusive and one-based, START <= END; leading zeros are decimal. Reject signs, whitespace, Unicode digits, open endpoints, zero, reversal, extra colons, missing/repeated range options with usage status 2. Validate usage before acquiring input, even if the source is missing. No arbitrary endpoint limit, multi-range/from-end behavior or streaming guarantee is provided.

Decode the **complete** input before selecting lines: malformed bytes after END still fail. Apply BOM policy once before numbering. Retain selected lines' original contents/terminators and count only existing selected lines/words. Requests beyond EOF use the available subset, including zero; no final phantom line. Interior BOM does not become removable because selection exposes it. Options compose in either order.

| Complete input | Range | lines | words |
| --- | --- | ---: | ---: |
| `alpha beta\nbeta\nlast two` | `2:3` | 2 | 3 |
| same | `1:1` | 1 | 2 |
| same | `2:99` | 2 | 3 |
| same | `4:99` | 0 | 0 |
| empty | `1:3` | 0 | 0 |
| `a\n\n` | `2:9` | 1 | 0 |
| `a\r\nb c\rd\n` | `2:3` | 2 | 3 |
| `a` + U+2028 + `b\nc` | `1:1` | 1 | 2 |
| U+FEFF only, default | `1:1` | 0 | 0 |
| U+FEFF only, keep BOM | `1:1` | 1 | 1 |
| U+FEFF + ` a\nb`, either mode | `2:2` | 1 | 1 |
| `a\n` + U+FEFF + ` b` | `2:2` | 1 | 2 |
| two leading BOMs, default | `1:1` | 1 | 1 |

Exercise singleton unterminated final lines, `01:02`, all-lines equivalence, LF/CR/CRLF blank boundaries, malformed range precedence and decode errors beyond END. Named-file range exits include extracted-source invocations and examples. Actual stdin whole-input/range empty/BOM/mixed-newline, locale independence and stream lifetime/read/decode cases are later stdin exits.

The original [campaign plan](../../docs/dev/reviews/008_98a5562/REVISION-PLAN.md) is provenance only. Its fixed destination and completed identities are not inputs to this project.
