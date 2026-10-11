"""Pure whole-text statistics with CRLF/CR/LF lines and Unicode words.

Normalization belongs at the whole-input boundary. Counting normalized text
and traversing preserved logical segments are separate internal operations so
future selection can reuse them without removing an exposed interior BOM.
"""

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TextStats:
    """Immutable, equal-by-value line and word counts.

    Attributes:
        lines: Nonnegative integer line count; bool is excluded.
        words: Nonnegative integer word count; bool is excluded.

    Raises:
        TypeError: Either count is not an integer or is a bool.
        ValueError: Either integer count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        """Validate both fields before construction returns a value."""
        for value in (self.lines, self.words):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("Statistics counts must be integers, excluding bool")
        if self.lines < 0 or self.words < 0:
            raise ValueError("Statistics counts must be nonnegative")


def _normalize_text(text: str, strip_bom: bool) -> str:
    """Remove exactly one complete-input leading BOM when requested."""
    if strip_bom and text.startswith("\ufeff"):
        return text[1:]
    return text


def _logical_lines(text: str) -> Iterator[str]:
    """Yield logical segments preserving only CRLF, CR and LF terminators.

    Blank terminated segments count as lines; a trailing terminator adds no
    empty segment. Other Unicode separators remain segment content.
    """
    start = 0
    end = 0
    while end < len(text):
        character = text[end]
        end += 1
        if character == "\r":
            if end < len(text) and text[end] == "\n":
                end += 1
        elif character != "\n":
            continue
        yield text[start:end]
        start = end
    if start < len(text):
        yield text[start:]


def _count_normalized(text: str) -> TextStats:
    """Count preserved logical lines and str.split words without normalization."""
    return TextStats(sum(1 for _ in _logical_lines(text)), len(text.split()))


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Return whole-input counts without writing to stdout or stderr.

    Args:
        text: Complete decoded input. CRLF, CR and LF terminate lines; words
            use Python's Unicode whitespace str.split semantics.
        strip_bom: Remove exactly one leading U+FEFF when true (the default).
            A second leading BOM and every interior BOM remain unchanged.

    Returns:
        Immutable counts. Empty normalized text has zero lines and words;
        a final nonempty unterminated segment contributes one line.
    """
    return _count_normalized(_normalize_text(text, strip_bom))
