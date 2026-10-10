# TextStats project brief

## Purpose and audience

TextStats is a small Python utility for developers and command-line users who need predictable line and word counts for UTF-8 text. It will expose a silent importable API and a module-entry CLI with explicit output and failure contracts. This repository currently contains preparation documents only; functionality has not been implemented.

## Established requirements

The product request establishes Python 3.11+, the standard library and unittest. The public `textstats` module must directly export immutable `TextStats(lines: int, words: int)` with nonnegative values, `count_text(text: str, *, strip_bom: bool = True)` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True)`. The CLI entry is `python -m textstats`.

Line counting recognizes CRLF as one terminator and lone CR or LF as terminators. Each terminator contributes one line; a nonempty final unterminated segment contributes one. Empty input has zero lines, trailing terminators create no phantom line, and other Unicode separators do not terminate lines. Words follow Python `str.split` Unicode whitespace semantics.

By default, remove exactly one leading U+FEFF. Preserve interior BOMs and every BOM when `strip_bom=False` or `--keep-bom` is selected. A retained BOM is ordinary non-whitespace. Files decode as strict UTF-8; API failures retain OSError subclasses or UnicodeDecodeError, produce no partial result, and close owned handles. API calls are silent and inputs remain unchanged.

## Delivery boundaries

| Phase and milestone | Intended useful outcome |
| --- | --- |
| Phase 1, milestone 1.1 | Named-file counting through the public API and `python -m textstats [--keep-bom] INPUT`; exactly one input and `--` for dash-prefixed filenames. Success returns 0 with exactly `lines=<N> words=<N>\n` on stdout and empty stderr; help returns 0. |
| Phase 1, milestone 1.2 | Failure handling, public API/module documentation, runnable README and distribution exits. Input/read/decode failures return 1; missing/extra inputs and unknown options return 2. Failures identify the problem on stderr with empty stdout and no traceback. |
| Phase 2, milestone 2.1 | `--json` emits one object plus newline, with integer `lines` and `words` fields only and identical counts. Text remains the default; JSON key order and spacing are unrestricted. |
| Phase 2, milestone 2.2 | `-` reads stdin bytes to EOF and decodes UTF-8 independently of locale without closing stdin. Empty stdin counts (0, 0); read/decode errors return 1 and identify stdin. Final exits cover documentation, distribution and retained behavior. |

Product tests must be discoverable and nonempty under `tests/unit/` and `tests/integration/`. Workflow fixture checks belong separately under `tests/workflows/`. Distribution verification must invoke the extracted source package's module entry. Exact test commands and package layout will be established during planning, rather than claimed as runnable at this stage.

## Later separately requested range feature

Retain this feature as a future design constraint and separate delivery boundary, outside the initial two-phase executable hierarchy. It will add exactly one `--lines START:END` or `--lines=START:END`, using positive ASCII decimal inclusive one-based endpoints with START <= END and decimal leading zeros. There is no arbitrary endpoint limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated range options with usage status 2 before acquiring input.

Complete input must decode before selection, including bytes after END. Apply BOM policy once before line numbering, preserve selected content and terminators, and select the available subset or zero beyond EOF. Exposing an interior BOM must not strip it. Options compose in either order. Public API signatures and exports stay whole-input. Named-file text/JSON range behavior is this feature's delivery boundary; source-independent compatibility with future stdin is required, while stdin acquisition and delivery remain their own later milestone.

## Acceptance anchors

The eventual specification must retain the full supplied examples and invalid-range matrix. Key anchors are empty input (0, 0), BOM-only default (0, 0), retained BOM (1, 1), two leading BOMs under default policy (1, 1), LF-only (1, 0), `alpha\n\n` (2, 1), and `alpha` followed by U+2028 and `beta` (1, 2). These distinguish terminator counting, Unicode word splitting and exactly-once BOM removal.

For `alpha beta\nbeta\nlast two`, ranges 2:3 and 2:99 yield (2, 3), 1:1 yields (1, 2), and 4:99 yields (0, 0). Blank selected lines and mixed CRLF/CR/LF must retain their counts. No new performance targets, third-party runtime dependencies or extra CLI capabilities are inferred.

## Preparation scope and review

The authorized workflow prepares PROJECT, architecture, decomposition, specification, plan, layout and an executable task hierarchy, pausing for each necessary new document's human review. Stop before production implementation; phase 2 and the later feature are not being implemented by this request.

The supplied product request establishes the requirements; this document organizes them and does not assert acceptance of unseen downstream documents. No consequential product decision is currently unresolved.

The user explicitly delegated intermediate test-artifact assessment and acceptance to the coordinator for this test run. The coordinator accepted PROJECT at commit `b7b017cf7480bded8ad7f7de4a4eed690083b39c`, blob `861ab8534bf96f22c8293922e34dbc292073bc1c`, after substantive comparison and independent durable-state assessment. This is delegated coordinator acceptance of that exact brief, not direct human review or acceptance of later documents. The authorized next stage is architecture.
