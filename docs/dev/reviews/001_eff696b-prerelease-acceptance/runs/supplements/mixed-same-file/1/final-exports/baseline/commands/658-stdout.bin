"""Pure whole-text counts with CRLF/CR/LF lines and Unicode whitespace words.

Normalization and counting are separate so already normalized text can later
be selected without stripping an exposed interior BOM a second time. Logical
line traversal preserves terminators for that future source-independent seam.
This module performs no I/O or process-stream writes.
"""

from dataclasses import dataclass
from collections.abc import Iterator


@dataclass(frozen=True, slots=True)
class TextStats:
    """Immutable, value-equal nonnegative integer line and word counts.

    Args:
        lines: Logical line count.
        words: Unicode whitespace-separated word count.

    Raises:
        TypeError: Either count is not an integer, including boolean values.
        ValueError: Either count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        for name, value in (('lines', self.lines), ('words', self.words)):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError(f'{name} must be an integer other than bool')
            if value < 0:
                raise ValueError(f'{name} must be nonnegative')


def _normalize_text(text: str, *, strip_bom: bool) -> str:
    """Remove exactly one leading U+FEFF when requested; preserve other text."""
    if strip_bom and text.startswith('\ufeff'):
        return text[1:]
    return text


def _iter_logical_lines(text: str) -> Iterator[str]:
    """Yield CRLF/CR/LF-ended segments and a nonempty final segment.

    Other Unicode separators remain within segments. Terminators are preserved;
    empty text and a trailing terminator do not yield a phantom final segment.
    """
    start = index = 0
    while index < len(text):
        char = text[index]
        if char == '\r' or char == '\n':
            index += 1
            if char == '\r' and index < len(text) and text[index] == '\n':
                index += 1
            yield text[start:index]
            start = index
        else:
            index += 1
    if start < len(text):
        yield text[start:]


def _count_normalized(text: str) -> TextStats:
    """Count already normalized text without any further BOM processing."""
    return TextStats(sum(1 for _ in _iter_logical_lines(text)), len(text.split()))


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Return whole-input counts silently, preserving the caller's string.

    CRLF is one line terminator; lone CR and LF each terminate one line. A
    nonempty final segment adds one line. Words follow ``str.split()`` without
    a separator, including Unicode whitespace. No other normalization occurs.

    Args:
        text: Complete input text.
        strip_bom: Remove exactly one leading U+FEFF when True (the default).
            False retains every BOM as ordinary non-whitespace. Interior and
            repeated leading BOMs are preserved in either policy.

    Returns:
        Immutable line and word counts; empty normalized input gives (0, 0).
    """
    return _count_normalized(_normalize_text(text, strip_bom=strip_bom))
