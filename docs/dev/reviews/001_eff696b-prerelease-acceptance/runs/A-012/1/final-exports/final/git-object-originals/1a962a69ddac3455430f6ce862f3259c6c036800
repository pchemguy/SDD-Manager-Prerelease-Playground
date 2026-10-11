# TextStats public API and module reference

TextStats exposes exactly `TextStats`, `count_text` and `count_file` directly from the `textstats` package. It requires Python 3.11+ and only the standard library. Importing the package and calling either counting function are silent: no stdout or stderr. The API always counts complete input.

## Signatures and immutable values

```python
from pathlib import Path
from textstats import TextStats, count_text, count_file

assert TextStats(lines=2, words=3) == TextStats(2, 3)
assert count_text("a b\nc") == TextStats(2, 3)
assert count_text("\ufeff", strip_bom=False) == TextStats(1, 1)
assert count_file(Path("sample.txt"), strip_bom=True) == TextStats(3, 5)
```

| Export | Signature / domain | Result and failures |
| --- | --- | --- |
| `TextStats` | `TextStats(lines: int, words: int)` | Immutable, equal-by-value fields. Nonnegative integers only; bool/non-integers raise TypeError, negative integers raise ValueError. Fields cannot be assigned or deleted. |
| `count_text` | `count_text(text: str, *, strip_bom: bool = True) -> TextStats` | Complete decoded string to immutable statistics, without I/O or shared mutable counting state. |
| `count_file` | `count_file(path: str \| os.PathLike[str], *, strip_bom: bool = True) -> TextStats` | String or string-valued path-like named file to equivalent whole-text counts. OSError subclasses propagate for open/read failures; invalid bytes raise UnicodeDecodeError. |

BOM policy is keyword-only. Behavior outside the stated argument domains is unspecified beyond the explicit statistics constructor validation.

## Counting semantics

Only CRLF, CR and LF terminate logical lines. CRLF is one terminator; each terminator contributes one line, and a final nonempty unterminated segment contributes one. Empty normalized input contributes zero; a trailing terminator creates no phantom line. U+0085, U+2028 and U+2029 remain line content. Word count is `len(text.split())`, using Python Unicode whitespace semantics independently of line terminators.

With the default `strip_bom=True`, remove exactly one leading U+FEFF from the complete input before counting. Preserve a second leading BOM and all interior BOMs. With `False`, retain every BOM as ordinary non-whitespace content. No other normalization occurs.

| Input (escaped) | Default lines / words | Retaining BOM |
| --- | --- | --- |
| Empty | 0 / 0 | 0 / 0 |
| `alpha\n` | 1 / 1 | 1 / 1 |
| `alpha\r\nbeta\rgamma\n` | 3 / 3 | 3 / 3 |
| `alpha\u2028beta` | 1 / 2 | 1 / 2 |
| `\ufeff` | 0 / 0 | 1 / 1 |
| `\ufeff\ufeff` | 1 / 1 | 1 / 1 |

## File acquisition and resource ownership

`count_file` reads complete bytes and decodes strict UTF-8, preserving newline characters. No locale-dependent or fallback decoding and no replacement characters are used. Every file handle opened by the utility closes on success, read failure and decode failure. No partial result is returned after failure. Input bytes remain unchanged. The implementation holds complete decoded input in memory; it makes no bounded-memory promise.

## Module command

Use `python -m textstats [--keep-bom] [--json] INPUT` from the source root. Exactly one named UTF-8 file is required. Recognized options work before or after INPUT; `--` terminates option parsing for dash-prefixed filenames. Until stdin delivery, literal `-` is a named file. Help (`-h` or `--help`) requires no acquisition.

| Outcome | Status | stdout | stderr |
| --- | --- | --- | --- |
| Count success | 0 | Exactly `lines=<N> words=<N>` plus newline | Empty |
| JSON count success (`--json`) | 0 | One object plus newline, only integer `lines` and `words` fields, same counts; key order/spacing unrestricted | Empty |
| Help | 0 | Useful usage/options | Empty |
| File open/read or strict decode failure | 1 | Empty | Identifies input and cause, no traceback |
| Missing/extra input or unknown option | 2 | Empty | Useful usage/error, no traceback |

The command validates invocation before opening input and prints counts only after complete acquisition, decode and counting. CLI error translation does not change the API exception contract. JSON composes with `--keep-bom`; text remains the default. Stdin and ranges are future work. Runnable examples and setup/check instructions are in the [README](../README.md).

## Module responsibilities

| Module | Responsibility |
| --- | --- |
| `textstats.core` | Immutable statistics, once-only BOM normalization, shared CRLF/CR/LF traversal and whole-text counting. |
| `textstats.io` | Strict named-file acquisition and owned-handle lifetime, then shared whole-text counting. |
| `textstats` | Direct public exports; import has no input or process effects. |
| `textstats.cli` | Invocation validation, BOM policy, expected failure translation and text/JSON rendering. |
| `textstats.__main__` | Minimal module-entry adapter returning the CLI process status. |

Internal helpers are not additional public exports. Future range selection can reuse preserved logical segments without renormalizing an exposed interior BOM.
