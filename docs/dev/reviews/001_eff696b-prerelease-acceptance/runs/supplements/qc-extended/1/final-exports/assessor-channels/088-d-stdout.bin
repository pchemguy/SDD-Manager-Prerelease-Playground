# Named-file line-selection specification

## Scope, baseline and authority

This active delta activates [SPEC F-001–F-004](SPEC.md#deferred-range-feature) for named-file delivery. It extends R-007/R-009 CLI invocation with range selection; R-001–R-006 and R-008 remain governing contracts. [PROJECT](PROJECT.md), [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) already define the required pure selection seam, so no design overlay is necessary. Python 3.11+, standard library and unittest remain required.

Preparation baseline is published default `main` at `e7cae5b2216ff7dd311b6f7296d829d1927a6a8a`. Observed JSON implementation is separately published at `e63b8946bbb99347b0f73f070f9c728945ee5925` on paused `phase/2-json-and-stdin`: T-010–T-012 complete, T-013–T-017 pending. This feature does not complete, merge or resume that phase. Package [002_e7cae5b-named-file-ranges](features/002_e7cae5b-named-file-ranges/README.md) owns this delta; main documents remain unchanged.

## F-001 Invocation and validation

Add one optional `--lines START:END` or `--lines=START:END` to exactly one named-file input. Each endpoint contains only ASCII decimal digits and represents a positive, inclusive, one-based endpoint; START <= END. Leading zeros are decimal. Endpoints and digit counts have no arbitrary limit, including interpreter decimal conversion safeguards. Both spelling forms are equivalent.

Reject signs, any whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repetition (including mixed spelling forms). All invalid invocations return 2, useful nonempty stderr, empty stdout and no traceback before input acquisition. Existing missing/extra input, unknown-option and help behavior remains R-007/R-008. `--` ends option parsing; a dash-prefixed file is addressed after it. With no range option, retain whole-input behavior.

Range, JSON and BOM flags compose in either order and may precede or follow INPUT before `--`. This feature leaves literal `-` as a named file until the separately delivered stdin milestone; `./-` remains a named-file path. It adds no stdin acquisition or public API parameter/export.

## F-002 Pipeline and result semantics

Read and strictly decode the complete file before selection. Invalid UTF-8 after END still returns 1 with an identifying diagnostic, empty stdout and no traceback. Existing input/read/decode errors, handle closure and input preservation remain R-006/R-008.

Apply BOM policy exactly once to the complete decoded string before numbering. Use CRLF as one terminator and lone CR/LF as terminators; preserve every selected segment's characters and terminator. A nonempty final unterminated segment is a line; empty input and a trailing terminator create no phantom segment. Other Unicode separators are content. Select START through END inclusively, intersected with available lines; START beyond EOF selects empty content.

Count selected content using R-003/R-004 without normalizing it again. An interior BOM exposed by selection remains ordinary non-whitespace. `--keep-bom` retains every BOM before numbering and selection. Pure selection depends on normalized text and validated endpoints, allowing a future stdin source without source-specific selection rules.

## F-003 Compatibility and delivery exits

For success return 0 and empty stderr. Default stdout is exactly `lines=<N> words=<N>\n`; with `--json`, emit one object plus newline containing only integer `lines` and `words`, equal to text counts. Preserve R-008 failure categories under every flag combination. Public `TextStats`, `count_text` and `count_file` stay immutable/silent/whole-input with unchanged signatures and exports.

Named-file text/JSON range behavior, help and runnable documentation, nonempty unit/integration verification and isolated extracted-source module-entry verification are delivery obligations. Preserve all existing whole-input file/API/CLI behavior and JSON. Stdin delivery, new exports, source streaming, benchmark targets, third-party dependencies and release publication are outside this feature.

## F-004 Objective acceptance

Escapes below denote actual characters. Run every success example in text and JSON, with equal counts, status 0 and empty stderr.

| Complete input | Range / policy | Expected (lines, words) |
| --- | --- | --- |
| `alpha beta\nbeta\nlast two` | 2:3 and 2:99 | (2, 3) |
| `alpha beta\nbeta\nlast two` | 1:1 and 0001:0001 | (1, 2) |
| `alpha beta\nbeta\nlast two` | 4:99 | (0, 0) |
| `a\n\n` | 2:9 | (1, 0) |
| `a\r\nb c\rd\n` | 2:3 | (2, 3) |
| `a\n\ufeff` | 2:2, both BOM policies | (1, 1) |
| Empty | 1:99 | (0, 0) |
| `\ufeff` | 1:1, default / keep | (0, 0) / (1, 1) |
| `\ufeff\ufeff` | 1:1, both policies | (1, 1) |
| `alpha\u2028beta` | 1:1 | (1, 2) |
| `\n` | 1:1 | (1, 0) |

Use valid endpoints with more than 4,300 digits as both END (available subset) and START (empty), as well as many leading zeros that represent small valid endpoints. Never overflow, truncate or impose a cap. Cover every permutation of range/BOM/JSON flags, both range spellings, options before/after INPUT, and dash-prefixed files after `--`.

| Invalid class | Representative values / invocations |
| --- | --- |
| Zero or reversed | `0:1`, `1:0`, `3:2` |
| Signs | `-1:2`, `+1:2`, `1:-2`, `1:+2` |
| Whitespace | ` 1:2`, `1:2 `, `1 :2`, `1:\t2` |
| Non-ASCII digits | `١:٢`, `１:２` |
| Open or extra separators | `:2`, `1:`, `:`, `1:2:3`, `1` |
| Missing | `--lines`, `--lines=`, `--lines --json INPUT` |
| Repeated | two spaced, two equals, or mixed forms, including identical valid values |

Verify each rejection before acquisition using a controlled acquisition seam and a missing named file. Include bad bytes strictly after the selected END to prove full decode; controlled read failures and handle cleanup remain testable at the acquisition seam. Recheck whole-input acceptance from main SPEC, silent unchanged API, file byte preservation, text/JSON equivalence and failure stdout. Distribution checks must run the extracted package's real module entry with isolated imports and cover range successes, invalid ranges, BOM exposure and bad bytes after END. Documentation must describe named-file range delivery accurately and retain deferred stdin status.

## Ownership and readiness

F-001 belongs to C-007 parsing; F-002 uses C-005 acquisition, C-002 once-only normalization, C-003 traversal, C-010 selection and C-004 counting; F-003 uses C-008/C-009 orchestration/rendering with C-006 compatibility. F-004 checks these collaborating boundaries through existing product suites and extraction tools. No material behavioral or design decision remains open. The adjacent [owner QC](FEATURE-SPEC-REVIEW-REPORT.md) reports technical readiness; concrete delegated acceptance is a separate checkpoint before planning. No implementation is authorized here.
