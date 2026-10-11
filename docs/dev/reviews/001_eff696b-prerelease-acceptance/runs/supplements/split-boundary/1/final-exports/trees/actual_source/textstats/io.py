"""Complete named-file acquisition with strict UTF-8 and owned-handle cleanup.

Files are read as bytes so CRLF, CR, LF and BOMs reach the pure counting core
unchanged. This module never writes inputs or process streams. Borrowed stdin
acquisition remains a later capability.
"""

from os import PathLike

from .core import TextStats, count_text


def count_file(path: str | PathLike[str], *, strip_bom: bool = True) -> TextStats:
    """Return silent whole-file counts after complete strict UTF-8 decoding.

    Args:
        path: Named file, supplied as a string or string-valued path-like object.
        strip_bom: Remove exactly one leading U+FEFF by default; False retains it.
            All other count semantics are identical to ``count_text``.

    Returns:
        Immutable statistics for the complete decoded file, without changing
        its bytes. No partial result is returned after acquisition failure.

    Raises:
        OSError: Opening or reading fails; the original subclass propagates.
        UnicodeDecodeError: Complete file bytes are not valid strict UTF-8.

    The handle opened here is closed on success, read failure or decode failure.
    No caller-owned stream is accepted or closed by this API.
    """
    with open(path, 'rb') as source:
        text = source.read().decode('utf-8', errors='strict')
    return count_text(text, strip_bom=strip_bom)
