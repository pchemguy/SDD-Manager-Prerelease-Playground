"""Silent whole-input statistics API: TextStats, count_text and count_file."""

from .core import TextStats, count_text
from .io import count_file

__all__ = ["TextStats", "count_text", "count_file"]
