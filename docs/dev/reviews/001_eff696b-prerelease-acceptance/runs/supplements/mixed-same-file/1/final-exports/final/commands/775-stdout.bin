# TextStats architecture

## Scope and governing input

This document describes the intended architecture for the capabilities and staged scope in the accepted [project brief](PROJECT.md). No product implementation exists. The public surface is an importable `textstats` API and `python -m textstats`; counting has no runtime dependencies beyond Python 3.11+ and the standard library.

## Major blocks and dependency direction

| Block | Responsibility and dependencies |
| --- | --- |
| Counting core | Own immutable statistics and text semantics: BOM normalization, CRLF/CR/LF logical-line handling and Unicode whitespace word counting. It depends on Python strings and immutable results, with no filesystem, CLI or process-stream dependency. |
| Input acquisition | Own strict UTF-8 decoding and named-file handle lifetime. It supplies decoded text to the counting pipeline and propagates acquisition/decode errors. Future stdin acquisition uses bytes and retains external stream ownership. |
| Public API facade | Directly expose the three requested public exports. `count_text` invokes the text pipeline; `count_file` acquires named-file text and invokes equivalent whole-input counting. Both return statistics silently, retaining API exceptions. |
| CLI orchestration | Parse and validate the requested invocation before acquiring input, select BOM/output policies, invoke the counting pipeline and translate input failures into CLI diagnostics/status. It depends on acquisition and core contracts; neither depends on CLI. |
| Presentation | Format a completed result as the required text output or the later JSON object. The CLI owns stdout/stderr effects and process status; presentation contains no input acquisition or counting rules. |

These are logical responsibility blocks, not a requirement for separate files or classes. Detailed collaborating components belong in decomposition and physical allocation in layout. There is no dependency cycle or global mutable counting state. The API and CLI share counting and decoding semantics rather than maintaining independent algorithms.

## Text pipeline and ownership

Acquisition finishes strict decoding before a result can be computed or emitted. The text pipeline removes at most one leading BOM according to the selected policy, then operates on normalized text. Whole-input API calls never select a range. The pipeline provides a counting path for already normalized text so the later CLI range path cannot strip a newly exposed interior BOM.

A shared logical-line representation or traversal recognizes only CRLF, CR and LF and preserves terminators and content. Both counting and future selection must use this semantic boundary; Python's broader Unicode `splitlines` behavior is unsuitable. Word counting remains independent, using `str.split` semantics on the counted content. Decomposition will settle the small internal interfaces without adding public exports.

The future range pipeline is acquisition and complete decode, BOM normalization once, logical-line selection, then counting and presentation. Parsing/validation precedes acquisition. Selection does not depend on whether text originated from a file or stdin. This supports the requested compatibility constraint without implementing the range feature or moving stdin into its delivery scope.

Input acquisition owns handles it opens and closes them on success and failure. Callers retain ownership of supplied process streams, including future stdin. No block writes input content. Statistics are immutable values; transient decoded strings and selected content have invocation-local lifetime. The default architecture holds complete decoded input in memory, which simplifies strict complete-decode and no-partial-result guarantees. No bounded-memory target was requested; streaming remains a future reconsideration if a concrete input-size constraint arises.

## Failure and output boundaries

API adapters allow the required filesystem and decode exception types to reach callers and produce no output. CLI orchestration distinguishes usage failures from input/read/decode failures and maps them to the prescribed statuses. Successful acquisition and counting must complete before stdout emission; diagnostics identify the affected input, and expected user failures do not expose a traceback. Presentation receives a complete immutable result, preventing partial count output during read/decode failure.

The CLI selects text output by default; JSON is a later output policy over the same statistics. Byte acquisition for future stdin keeps strict UTF-8 decoding independent of locale. Option parsing is a CLI concern and does not alter public whole-input API signatures.

## Consequential choices and verification seams

Use plain functions and a small immutable result value. Separate pure text processing from I/O and process effects because they have different failure/lifetime rules and verification seams. A monolithic CLI would couple reusable API behavior to streams; a class hierarchy, plugin system or configurable decoding layer would introduce unsupported variation. The selected function pipeline provides the required extension seams with less state and indirection.

Unit tests can exercise immutable results, BOM policy and logical-line/word semantics directly. Integration tests can exercise named-file acquisition, subprocess CLI output/status, later JSON/stdin behavior and extracted-source module execution. Product suites remain nonempty and discoverable under the requested unit/integration directories; coordinator workflow fixtures stay separately owned. API/module documentation and README usage will expose the same contracts used by these checks.

The distribution boundary is a source package that remains importable and supports module execution after extraction. Package contents and the executable verification command are planning/layout decisions. No additional runtime dependency, installed console-script entry or network service is required.

## Review and next stage

Owner review checked responsibility ownership, acyclic dependency direction, strict UTF-8 and handle lifetime, no-partial-result boundaries, BOM normalization exactly once, shared terminator semantics and source-independent future selection against the accepted PROJECT. No unresolved architectural decision blocks decomposition. No focused children are needed for this compact system, and no code or performance test has been run for the proposed arrangement.

ARCHITECTURE is pending delegated coordinator assessment under the user's test-review instruction. Recommend accepting this architecture and proceeding to decomposition; that dependent stage remains held until the coordinator accepts the exact published architecture state. This recommendation does not accept unseen downstream artifacts.
