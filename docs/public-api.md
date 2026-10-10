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

## Input acquisition and resource ownership

`count_file` reads complete bytes and decodes strict UTF-8, preserving newline characters. No locale-dependent or fallback decoding and no replacement characters are used. Every file handle opened by the utility closes on success, read failure and decode failure. No partial result is returned after failure. Input bytes remain unchanged. The implementation holds complete decoded input in memory; it makes no bounded-memory promise.

CLI stdin acquisition reads the borrowed binary stream through EOF and decodes
complete strict UTF-8 independently of the text locale. It preserves raw newline
characters and leaves stdin open on success, read failure and decode failure.
There is no new public stdin export or stream argument on `count_file`.

## Module command

Use `python -m textstats [--keep-bom] [--lines START:END] INPUT` from the source root. Exactly one input is required: a named UTF-8 file or `-` for binary stdin. Recognized options work before or after INPUT; `--` terminates option parsing for dash-prefixed filenames. A `-` token after `--` also means stdin; use `./-` for a named file called `-`. Help (`-h` or `--help`) requires no acquisition.

| Outcome | Status | stdout | stderr |
| --- | --- | --- | --- |
| Count success | 0 | Exactly `lines=<N> words=<N>` plus newline | Empty |
| Help | 0 | Useful usage/options | Empty |
| File open/read, stdin read or strict decode failure | 1 | Empty | Identifies named input or stdin and cause, no traceback |
| Missing/extra input, unknown option or invalid/missing/repeated range | 2 | Empty | Useful usage/error, no traceback |

The command validates invocation before acquiring input and prints counts only after
complete acquisition, strict decode and counting. CLI error translation does not
change the API exception contract. Only exact text output is supported. `--json`, `--json=value` and `--j` fail
with usage status 2 before acquisition; after `--`, a literal `--json` filename
works in whole-input and range modes.

### Range grammar and ordering

One `--lines START:END` or `--lines=START:END` selects inclusive one-based logical
lines. Each endpoint contains only ASCII `0`–`9`, is nonempty and positive, and
START must not exceed END. Leading zeros are decimal. Endpoints have no digit or
value cap and do not change the interpreter's integer conversion guard. Repeated
range options, missing values, signs, whitespace, non-ASCII digits, zero,
reversed endpoints or anything other than one colon are usage errors before
acquisition, even when the file is missing or undecodable.

After complete strict UTF-8 decoding, apply the requested BOM policy exactly
once to the whole input, then number CRLF/CR/LF logical segments and preserve the
available selected segments verbatim. Count the resulting selection without
normalizing again. A selected blank terminated segment is a line with no words;
a final unterminated nonempty segment is a line. A trailing terminator produces
no phantom line. END beyond EOF truncates to available segments; START beyond
EOF or empty normalized input produces zero lines and words. U+0085/U+2028/U+2029
remain line content but may separate words through Unicode whitespace splitting.
An interior BOM exposed at the start of a selected line remains ordinary content.

Named-file or stdin bytes are fully acquired and decoded even if END is small: bad UTF-8
after END returns status 1 without partial output. Owned named-file handles close
and borrowed stdin stays open on success, read failure and decode failure.
Input bytes remain unchanged. Selection
makes no bounded-memory promise. Public `count_text` and `count_file` always
count whole input; `--lines` adds no public API argument or export.

Runnable setup, mixed-terminator/blank/interior-BOM/EOF, text, BOM-policy and
invalid/decode examples are in the [README](../README.md). Stdin uses this same
normalize/select/count rule after complete acquisition without changing public
API semantics. Empty stdin counts zero lines and words. A read/decode failure
identifies stdin and cause with status 1, empty stdout and no traceback;
strict decoding still covers bytes after the selected END.

## Module responsibilities

| Module | Responsibility |
| --- | --- |
| `textstats.core` | Immutable statistics, once-only BOM normalization, shared CRLF/CR/LF traversal, preserved normalized selection and whole-text counting. |
| `textstats.io` | Complete strict UTF-8 byte acquisition; owned named-file handles close and borrowed streams stay open, then shared whole-text counting. |
| `textstats` | Direct public exports; import has no input or process effects. |
| `textstats.cli` | Invocation/range validation before acquisition, BOM/selection ordering, expected failure translation and text rendering. |
| `textstats.__main__` | Minimal module-entry adapter returning the CLI process status. |

Internal helpers are not additional public exports. Range selection reuses preserved logical segments without renormalizing an exposed interior BOM.
