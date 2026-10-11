"""Complete strict UTF-8 named-file acquisition, preserving raw terminators.

This module owns only handles it opens. Acquisition and decoding finish before
counting; filesystem and decode exceptions propagate without output or results.
"""

from os import PathLike
from .core import TextStats, count_text


def count_file(path: str | PathLike[str], *, strip_bom: bool = True) -> TextStats:
    """Return whole-file counts silently without changing input bytes.

    Args:
        path: Named file as a string or string-valued path-like object.
        strip_bom: Remove exactly one leading U+FEFF when true (default).

    Returns:
        Immutable counts with the same semantics as count_text.

    Raises:
        OSError: Opening or reading the named file fails (subclasses retained).
        UnicodeDecodeError: Complete bytes are not strict UTF-8.

    Every opened handle closes on success or failure. Binary input prevents
    newline translation; no partial count is returned after read/decode failure.
    """
    return count_text(_read_file_text(path), strip_bom=strip_bom)


def _read_file_text(path: str | PathLike[str]) -> str:
    """Acquire complete strict UTF-8 text before any normalization or selection.

    Binary mode preserves terminators; the owned handle closes on every path.
    File/read/decode exceptions propagate unchanged and no partial text returns.
    """
    with open(path, "rb") as stream:
        return stream.read().decode("utf-8", errors="strict")
