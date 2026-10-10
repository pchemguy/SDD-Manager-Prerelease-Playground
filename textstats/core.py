"""Pure statistics, BOM normalization and shared CRLF/CR/LF traversal.

Counting operates on complete strings and never acquires input or writes output.
The normalized counting seam preserves BOMs exposed by future line selection.
"""

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TextStats:
    """Immutable counts with value equality.

    Attributes:
        lines: Nonnegative integer number of logical lines.
        words: Nonnegative integer number of Unicode-whitespace-delimited words.

    Raises:
        TypeError: Either count is not an integer, or is a boolean.
        ValueError: Either count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        for name, value in (("lines", self.lines), ("words", self.words)):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError(f"{name} must be an integer, excluding bool")
            if value < 0:
                raise ValueError(f"{name} must be nonnegative")


def _normalize_text(text: str, strip_bom: bool) -> str:
    """Remove exactly one leading U+FEFF when selected; retain all other text."""
    return text[1:] if strip_bom and text.startswith("\ufeff") else text


def _logical_lines(text: str) -> Iterator[str]:
    """Yield original logical segments including their CRLF/CR/LF terminators.

    Blank terminated lines are segments; a trailing terminator adds no phantom
    segment. Other Unicode separators are content. Input is already normalized;
    this traversal never strips a BOM or rewrites characters.
    """
    start = position = 0
    while position < len(text):
        character = text[position]
        position += 1
        if character == "\r":
            if position < len(text) and text[position] == "\n":
                position += 1
        elif character != "\n":
            continue
        yield text[start:position]
        start = position
    if start < len(text):
        yield text[start:]


def _count_normalized(text: str) -> TextStats:
    """Count shared logical segments and str.split words without normalization."""
    return TextStats(sum(1 for _ in _logical_lines(text)), len(text.split()))


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Return whole-string line and word counts without output or input mutation.

    CRLF is one line terminator, and lone CR or LF is one. A nonempty final
    unterminated segment adds one line; empty text has zero. Words follow
    Python's str.split Unicode whitespace semantics.

    Args:
        text: Complete string to count.
        strip_bom: Remove exactly one leading U+FEFF by default. False retains
            every BOM; interior and additional leading BOMs always remain.

    Returns:
        An immutable TextStats value for the counted text.
    """
    return _count_normalized(_normalize_text(text, strip_bom))
