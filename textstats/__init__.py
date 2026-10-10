"""Silent whole-text statistics API.

Directly exports immutable TextStats and count_text with a keyword-only BOM
policy. File acquisition and count_file are delivered by the subsequent task.
"""

from .core import TextStats, count_text

__all__ = ["TextStats", "count_text"]
