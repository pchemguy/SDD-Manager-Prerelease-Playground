# TextStats component decomposition

## Governing design and scope

This component model refines the accepted [architecture](ARCHITECTURE.md) and [project brief](PROJECT.md). Components are logical units with stable design identities; internal function names below express interface shape and may be finalized during implementation without changing their obligations. They prescribe no physical file inventory or implementation order. No production code exists.

## Components and boundaries

| ID / component | Provided boundary and owner responsibility | Required collaborators and exclusions |
| --- | --- | --- |
| C-001 Statistics value | Public immutable `TextStats(lines: int, words: int)` with nonnegative counts. Own construction invariants and value representation. | No acquisition, output or normalization. SPEC will settle invalid-construction exceptions and integer-domain details. |
| C-002 BOM normalization | Internal `normalize_text(text, strip_bom) -> str`; remove exactly one leading BOM when selected and retain all other characters. Own this policy once per pipeline invocation. | Strings only; no decode, line selection or counting. |
| C-003 Logical-line traversal | Internal `logical_lines(normalized_text)` yields nonempty logical segments with their original content and CRLF/CR/LF terminators; blank terminated lines remain segments. A final nonempty unterminated segment is yielded; empty text yields none. | No BOM handling or Unicode-whitespace splitting. This is the shared line boundary for counting and future selection. |
| C-004 Normalized counting | Internal `count_normalized(normalized_text) -> TextStats`; derive line count from C-003 and word count from `str.split` on the same text. | C-001 and C-003; never normalize again, acquire input or emit output. |
| C-005 Byte acquisition and decode | Acquire complete bytes from a named file and decode strict UTF-8 without text newline translation. Own opening and closing named-file handles on every path. Future borrowed-stdin acquisition reads its binary stream to EOF and never closes it. | Python filesystem/binary stream operations; no BOM removal, range selection, counting or output. Preserve acquisition and decode exceptions for callers. |
| C-006 Public API adapters | Directly expose C-001 plus `count_text(text: str, *, strip_bom: bool = True)` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True)`. Adapt whole-input requests to C-002/C-004; file calls use C-005 first. | No CLI invocation or range argument; no extra public export, stream output or exception-to-status translation. |
| C-007 CLI invocation parser | Validate option syntax and exactly one input; provide input identity and BOM policy. Future range validation supplies numeric endpoints before input acquisition. | No C-005 access during parsing. Help and usage termination belong to CLI control, not API behavior. |
| C-008 CLI controller | Coordinate parsed invocation, acquisition, text pipeline and result rendering; map expected usage/acquisition/decode failures to identifying diagnostics/status. Own process-stream writes. | C-007, C-005, C-002, C-004 and C-009; no separate counting algorithm. Future C-010 sits between normalization and counting. |
| C-009 Result rendering | Internal renderer transforms completed C-001 into the specified text string plus newline. | No stream write, acquisition, normalization or counting. Controller emits the result. |
| C-010 Future range selection | Future internal `select_lines(normalized_text, start, end) -> str`, with inclusive one-based endpoints, preserving available selected segments and their terminators. | C-003 and validated CLI endpoints; no input-source dependency or BOM normalization. This future feature is outside the initial two-phase executable hierarchy. |

The identities group coherent verification obligations and provide downstream specification/planning traceability; they do not require one module or task per row. No focused children are necessary for this compact component set.

## Collaboration and data lifetime

`count_text` receives the complete string, normalizes through C-002 and counts through C-004. `count_file` uses C-005 to acquire/decode complete input, then follows the equivalent public whole-input pipeline. The API adapters return C-001 without writing stdout/stderr. Strict byte decoding preserves CRLF, lone CR and LF exactly rather than relying on universal-newline text mode.

The CLI parses and validates before C-005 acquires input. C-008 then normalizes exactly once and passes normalized text to C-004. Only a completed value reaches C-009 and only the controller writes its output. If the future range feature is separately requested, C-008 passes normalized text through C-010 first and sends its result directly to C-004, bypassing C-002 a second time. Consequently, a BOM exposed inside selected content remains ordinary non-whitespace.

C-003 yields segments such as `a\r\n`, `b c\r` and `d\n` without changing characters. Selecting whole segments and concatenating them preserves line boundaries for C-004 and preserves Unicode whitespace for word counting. Segment enumeration can be lazy over the already decoded string; it does not imply streaming decode or partial input acceptance. Counting and range selection share the same terminator semantics.

For future stdin, C-005 obtains bytes from the externally owned binary input stream and returns decoded text after EOF; the remainder of the pipeline is identical. The parser/controller activate that acquisition choice only at its delivery milestone. Decoded strings, segments and results are local to an invocation; there is no shared mutable counting state or input mutation.

## Failure and verification seams

C-001 can be checked through construction, immutability and value assertions. C-002 can be checked with empty, BOM-only, repeated-leading and interior-BOM strings under both policies. C-003/C-004 can be checked with mixed terminators, consecutive blank lines, final segments and Unicode whitespace/separators. These seams need no filesystem or subprocess.

C-005 can be checked with temporary valid/invalid UTF-8 files, missing/unreadable paths and controlled read failures, including handle cleanup. Borrowed-stream checks later verify byte decoding, locale independence, EOF and retained ownership. C-006 checks establish direct imports, whole-input equivalence, silence and exception propagation. No partial decoded/count result is returned on input failure.

C-007 checks establish help/usage behavior and, later, range validation before acquisition, including repeated options and unbounded decimal endpoints. C-008/C-009 checks establish exact text output, removed-option rejection, empty failure stdout and identifying stderr/status. Subprocess integration validates the real module entry and extracted-source distribution; component-level seams support controlled acquisition failures that can be difficult to reproduce reliably through platform permissions.

C-010's future checks cover available subsets, beyond-EOF emptiness, blank selected lines, mixed terminators, bad bytes after END and interior BOM exposure. These are deferred feature obligations, not tests or delivery included in this preparation request.

## Contract handoff and review

The product request already fixes line/word/BOM semantics, API signatures, output and exit categories. SPEC will provide the full objective acceptance matrix, exact staged CLI grammar, invalid constructor/input-type contracts where required, useful diagnostic expectations and the public documentation/distribution obligations. Internal naming is provisional; public exports are fixed. There is no unresolved component decision that requires upstream architecture revision.

Owner review checked one owner per responsibility, acyclic collaboration, preservation of binary-decoded newlines, once-only normalization, source independence, lifetime/error seams, component cohesion and localized testability against the accepted architecture. No code or product tests were run. The coordinator accepted DECOMPOSITION at commit `566a1af2ddd44d79a898c2e67607360395044ba6`, blob `0afa55c7082455d7e102f9c3d056d474e686da57`, under delegated test-artifact review authority. Its full-content comparison against accepted architecture and the product request found no material issue; published decision evidence is `309d984`. This scoped acceptance authorizes SPEC and its owner QC, without accepting downstream documents or implementation.
