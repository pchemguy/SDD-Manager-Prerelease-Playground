# TextStats system specification

## Scope and authority

TextStats provides predictable line and word counts through a silent Python API and module-entry CLI. The accepted [PROJECT](PROJECT.md), [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) govern product purpose and structural boundaries. Python 3.11+, standard-library runtime and unittest are required. No implementation exists.

R-001 through R-013 specify the intended initial two-phase system; milestone labels identify delivery obligations without authorizing implementation. F-001 through F-004 retain the later separately requested range feature's contract as a deferred compatibility constraint. That feature is outside the initial executable hierarchy. No focused specification children are needed.

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

## Deferred range feature

### F-001 Range grammar and validation

A separately requested feature adds exactly one `--lines START:END` or `--lines=START:END`. START and END consist solely of ASCII decimal digits and represent positive inclusive one-based endpoints with START <= END. Leading zeros are decimal. No arbitrary endpoint or digit-count limit is permitted. Reject signs, surrounding or interior whitespace, Unicode digits, zero, reversal, open endpoints, extra colons, missing values and repeated range options. Repetition across the two spelling forms is also invalid. Reject with usage status 2, useful stderr, empty stdout and no traceback before acquiring input. Valid very large decimal endpoints must remain valid despite any interpreter conversion safeguard.

### F-002 Selection semantics and decode ordering

Decode the complete input before selecting lines; invalid bytes after END still fail under R-008. Apply R-005 exactly once to complete decoded input before numbering. Select inclusive one-based logical lines under R-003, preserving each selected segment's contents and terminators. If END exceeds EOF, select the available subset; if START exceeds EOF, select empty content. Count the selected content under R-003/R-004 without further BOM stripping. An interior BOM exposed at the beginning of selected text must remain ordinary non-whitespace.

### F-003 Composition and delivery boundary

Range selection composes with `--keep-bom` and `--json` in either option order, using either accepted range spelling. Preserve default text output and R-008 error categories. Named-file text/JSON range behavior is the feature's delivery boundary. The public API remains whole-input with no range parameter or new export. Source-independent selection must be compatible with future stdin, but this feature does not implement or pull forward stdin acquisition/delivery.

### F-004 Objective range acceptance

| Complete input (escaped) | Range | Expected (lines, words) |
| --- | --- | --- |
| `alpha beta\nbeta\nlast two` | 2:3 | (2, 3) |
| `alpha beta\nbeta\nlast two` | 2:99 | (2, 3) |
| `alpha beta\nbeta\nlast two` | 1:1 | (1, 2) |
| `alpha beta\nbeta\nlast two` | 4:99 | (0, 0) |
| `a\n\n` | 2:9 | (1, 0) |
| `a\r\nb c\rd\n` | 2:3 | (2, 3) |
| `a\n\ufeff` | 2:2, default BOM policy | (1, 1) |
| Empty input | 1:99 | (0, 0) |

Acceptance also covers zero/reversed/negative/signed/Unicode-digit/whitespace/open/extra-colon/missing/repeated ranges, invalid UTF-8 after END, decimal leading zeros, endpoints far beyond EOF and all option-order combinations. Validate rejection before named-file access, including when the selected filename is missing. Very large endpoints select the available subset or empty content without overflow, truncation or an arbitrary cap.

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
| F-001 through F-004 | C-007/C-008 and deferred C-010 over C-002/C-003/C-004; no additional API export |

The adjacent [SPEC review report](SPEC-REVIEW-REPORT.md) owns the technical conformance assessment. SPEC is pending delegated coordinator assessment of its exact published state. Technical Ready does not accept unseen PLAN/layout/TASKS or authorize implementation.
