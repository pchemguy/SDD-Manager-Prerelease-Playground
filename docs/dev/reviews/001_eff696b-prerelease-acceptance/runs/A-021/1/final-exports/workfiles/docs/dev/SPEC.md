# TextStats system specification

## Scope and authority

TextStats provides predictable line and word counts through a silent Python API and module-entry CLI. The accepted [PROJECT](PROJECT.md), [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) govern product purpose and structural boundaries. Python 3.11+, standard-library runtime and unittest are required. Phase 1 is delivered; ranges and stdin delivery remain incomplete.

R-001 through R-013 specify the intended initial two-phase system; milestone labels identify delivery obligations without authorizing implementation. F-001 through F-004 govern accepted named-file ranges in Phase 2 milestones 2.4–2.6. Incorporation specifies intended behavior without asserting delivery. No focused specification children are needed.

## Public API and values

### R-001 Direct exports and statistics

Importable `textstats` directly exports `TextStats`, `count_text` and `count_file`. `TextStats(lines: int, words: int)` is immutable, with integer, nonnegative fields and value equality. Construction with a negative count raises ValueError; a non-integer count raises TypeError. Boolean values are excluded from the count domain despite Python's bool/int subtype relationship. Invalid construction cannot create a value with an invalid field. Exception wording is not prescribed. These construction details settle the design's previously delegated integer-domain boundary.

### R-002 Whole-input counting API

The signatures are `count_text(text: str, *, strip_bom: bool = True) -> TextStats` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats`. The keyword-only policy has the same meaning for both. Both return whole-input counts, are silent on stdout/stderr, and expose no range parameter. Valid text/file calls with identical decoded contents and policy return equal values. Behavior for arguments outside the annotated input domains is not otherwise prescribed.

### R-003 Line semantics

CRLF is one terminator; lone CR and lone LF are terminators. Each terminator contributes one line. A nonempty final unterminated segment contributes one line. Empty text contributes zero lines, and a trailing terminator creates no additional phantom line. Other Unicode separators, including U+0085, U+2028 and U+2029, do not terminate lines. Apply R-005 before deciding whether a final segment is nonempty.

### R-004 Word semantics

The word count equals the number of elements produced by Python `str.split()` with no separator argument on the counted text. Unicode whitespace separates words and runs of whitespace add no empty words. Word semantics do not broaden line-terminator semantics.

### R-005 BOM policy

With `strip_bom=True`, remove exactly one leading U+FEFF from the complete text. Preserve a second leading BOM and every interior BOM. With `strip_bom=False`, preserve all BOMs. Retained BOM is ordinary non-whitespace, including in otherwise empty content. CLI `--keep-bom` selects the retaining policy. No other text normalization or rewriting is permitted.

### R-006 Named-file decode, failure and ownership

Read complete input as bytes and decode strict UTF-8, retaining newline characters exactly. A named-file API call raises the applicable OSError subclass for missing/unreadable files or read failures and UnicodeDecodeError for invalid UTF-8. Do not return a partial result. Close every handle opened by the utility on success and failure. Inputs remain byte-for-byte unchanged. No fallback encoding, replacement character or locale-dependent decode is permitted.

## CLI contracts

### R-007 Baseline named-file invocation

Phase 1 milestone 1.1 supplies `python -m textstats [--keep-bom] INPUT` with exactly one named-file input. Support `--` to terminate option processing so dash-prefixed filenames are usable. A literal filename `-` is a named-file input before milestone 2.2; after stdin delivery it denotes stdin, and an actual file with that name can be addressed as `./-`. Recognized options can precede or follow the input, subject to `--` termination. Do not interpret options appearing after `--` as options.

Success returns status 0, stdout exactly `lines=<N> words=<N>\n` using nonnegative decimal integers, and empty stderr. This remains the default format in phase 2. Help through `-h` or `--help` returns 0 with useful usage/options on stdout and empty stderr; it requires no input acquisition. Help output's exact prose is unrestricted.

### R-008 CLI failures and usage

Phase 1 milestone 1.2 supplies complete failure handling. Missing/unreadable named files, input read failures and decode failures return status 1 with nonempty stderr identifying the input and cause, empty stdout and no traceback. Missing input, extra inputs and unknown options return status 2 with useful usage/error stderr, empty stdout and no traceback. Parse and validate invocation before acquiring input. Status categories are stable across the phase 2 options. No input is changed and no partial result appears on stdout.

### R-009 JSON output

Phase 2 milestone 2.1 supplies `--json`, composing with `--keep-bom` and named-file input. Success returns 0 with one JSON object and a final newline, empty stderr, and exactly the keys `lines` and `words`, each containing an integer equal to the text-format count. No extra fields or JSON booleans are permitted. Key order and spacing are unrestricted. Without `--json`, preserve R-007 text output. Failures retain R-008, regardless of output selection.

### R-010 Stdin input

Phase 2 milestone 2.2 supplies input token `-` as stdin. Read bytes until EOF and decode complete content as strict UTF-8 independently of locale, without closing stdin. Apply the same counting/BOM/output policies as named files. Empty stdin returns (0, 0). Read or decode failure returns 1, identifies stdin and the cause on stderr, and produces empty stdout with no traceback. Stdin acquisition does not alter `count_file` semantics or add an API export. Output succeeds only after complete input acquisition and decoding.

## Documentation, testing and distribution

### R-011 Public documentation and runnable README

Phase 1 milestone 1.2 supplies public API/module documentation describing exports/signatures, counts, BOM policy, silent APIs, strict decoding, exceptions and handle ownership. The README supplies runnable named-file/module-entry examples, setup and test instructions, output/status/help behavior and distribution usage. Phase 2 final exits update documentation for JSON/stdin and retained behavior. Documentation must describe delivered capabilities accurately; the preparation README's present lack of runnable code is explicit until delivery.

### R-012 Product verification organization

Use unittest with discoverable, nonempty product suites under `tests/unit/` and `tests/integration/`. Discovery must collect actual product tests rather than succeed with zero tests. Keep workflow fixture checks separately under `tests/workflows/`; they do not count as product verification. Verify API semantics and silence, immutability, acquisition/decode exceptions and resource lifetime, CLI process outputs/statuses, input preservation and retained behavior at the relevant delivery exits.

### R-013 Extracted-source distribution

Provide a source distribution containing the importable package, module entry and required user/API documentation. Verify its extracted contents by invoking `python -m textstats` in the extracted source context, without relying on imports from the original checkout or an unrelated installed package. Named-file success and failure and the delivered phase's JSON/stdin behavior must retain their specified contracts in that context. Packaging uses the standard library; no extra runtime dependency is required. Physical archive layout and check commands belong in planning/layout.

<a id="deferred-range-feature"></a>

## Named-file range contracts

### F-001 Invocation and validation

Add one optional `--lines START:END` or `--lines=START:END` to exactly one named-file input. Each endpoint contains only ASCII decimal digits and represents a positive, inclusive, one-based endpoint; START <= END. Leading zeros are decimal. Endpoints and digit counts have no arbitrary limit, including interpreter decimal conversion safeguards. Both spelling forms are equivalent.

Reject signs, any whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repetition (including mixed spelling forms). All invalid invocations return 2, useful nonempty stderr, empty stdout and no traceback before input acquisition. Existing missing/extra input, unknown-option and help behavior remains R-007/R-008. `--` ends option parsing; a dash-prefixed file is addressed after it. With no range option, retain whole-input behavior.

Range, JSON and BOM flags compose in either order and may precede or follow INPUT before `--`. This feature leaves literal `-` as a named file until the separately delivered stdin milestone; `./-` remains a named-file path. It adds no stdin acquisition or public API parameter/export.

### F-002 Pipeline and result semantics

Read and strictly decode the complete file before selection. Invalid UTF-8 after END still returns 1 with an identifying diagnostic, empty stdout and no traceback. Existing input/read/decode errors, handle closure and input preservation remain R-006/R-008.

Apply BOM policy exactly once to the complete decoded string before numbering. Use CRLF as one terminator and lone CR/LF as terminators; preserve every selected segment's characters and terminator. A nonempty final unterminated segment is a line; empty input and a trailing terminator create no phantom segment. Other Unicode separators are content. Select START through END inclusively, intersected with available lines; START beyond EOF selects empty content.

Count selected content using R-003/R-004 without normalizing it again. An interior BOM exposed by selection remains ordinary non-whitespace. `--keep-bom` retains every BOM before numbering and selection. Pure selection depends on normalized text and validated endpoints, allowing a future stdin source without source-specific selection rules.

### F-003 Compatibility and delivery exits

For success return 0 and empty stderr. Default stdout is exactly `lines=<N> words=<N>\n`; with `--json`, emit one object plus newline containing only integer `lines` and `words`, equal to text counts. Preserve R-008 failure categories under every flag combination. Public `TextStats`, `count_text` and `count_file` stay immutable/silent/whole-input with unchanged signatures and exports.

Named-file text/JSON range behavior, help and runnable documentation, nonempty unit/integration verification and isolated extracted-source module-entry verification are delivery obligations. Preserve all existing whole-input file/API/CLI behavior and JSON. Stdin delivery, new exports, source streaming, benchmark targets, third-party dependencies and release publication are outside this feature.

### F-004 Objective acceptance

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


## Whole-input acceptance matrix

Escaped sequences in this table denote actual input characters; U+2028 is a Unicode line separator.

| Input | Default (lines, words) | Retaining BOM (lines, words) where relevant |
| --- | --- | --- |
| Empty string | (0, 0) | (0, 0) |
| `alpha beta` | (1, 2) | Same |
| `alpha\n` | (1, 1) | Same |
| `\n` | (1, 0) | Same |
| `alpha\r\nbeta\rgamma\n` | (3, 3) | Same |
| `alpha\n\n` | (2, 1) | Same |
| Space followed by tab | (1, 0) | Same |
| `alpha\u2028beta` | (1, 2) | Same |
| `\ufeff` | (0, 0) | (1, 1) |
| `\ufeff\ufeff` | (1, 1) | (1, 1) |
| `\ufeffalpha beta` | (1, 2) | (1, 2) |
| `a\ufeffb` | (1, 1) | (1, 1) |
| `\r\n` | (1, 0) | Same |
| `\r` | (1, 0) | Same |

Named-file and text API results agree for these inputs. CLI text and JSON agree where delivered. Verify non-ASCII UTF-8, CRLF boundaries, owned-handle closure after decode/read failures, immutable results and unchanged input bytes. CLI integration covers named-file paths (including dash-prefixed), help, missing/extra inputs, unknown options, missing/unreadable/read-failing files, bad bytes, empty stdout on failures and useful diagnostics. Phase 2 adds text/JSON stdin, empty stdin, invalid bytes/read errors, locale independence and retained stream ownership. Distribution acceptance repeats the appropriate delivered module-entry behaviors after extraction.

## Behavioral ownership and review boundary

| Contract group | Responsible design components |
| --- | --- |
| R-001/R-002 | C-001 statistics and C-006 API adapters |
| R-003/R-004/R-005 | C-002 normalization, C-003 logical lines and C-004 counting |
| R-006/R-010 | C-005 acquisition, C-006 API and C-008 CLI |
| R-007/R-008/R-009 | C-007 parser, C-008 controller and C-009 rendering |
| R-011/R-012/R-013 | Public boundaries C-001 through C-009, supported by documentation and product/distribution verification |
| F-001 through F-004 | C-007/C-008 and C-010 over C-002/C-003/C-004; no additional API export |

The adjacent [SPEC review report](SPEC-REVIEW-REPORT.md) owns the technical conformance assessment. The coordinator accepted SPEC and SPEC-REVIEW-REPORT at commit `bf3eb5e9a8d30a9e8a457f7708afa3b400100417`, SPEC blob `86cfd0c0cc6241bad1329a4873dbbc7517cc1160` and report blob `6b7b1637fc0095387b2c32846725f64c4cc2e715`, under delegated test-artifact review authority; published decision evidence is `37115e0`. Full-content assessment found no material issue and accepted the explicit constructor domain and staged dash-input settlements. This scope authorizes PLAN strategy, without accepting unseen layout/TASKS or implementation.
