"""Owned byte acquisition failures and lifetime are portable controlled seams."""

import io
import unittest
from unittest.mock import patch

from textstats import TextStats, count_file


class FileAcquisitionTests(unittest.TestCase):
    def test_success_closes_owned_binary_handle_and_preserves_terminators(self):
        stream = io.BytesIO(b"a\r\nb\rc\n")
        with patch("textstats.io.open", return_value=stream, create=True) as opener:
            self.assertEqual(count_file("named"), TextStats(3, 3))
        opener.assert_called_once_with("named", "rb")
        self.assertTrue(stream.closed)

    def test_decode_failure_closes_and_returns_no_partial_count(self):
        stream = io.BytesIO(b"valid\n\xff")
        with patch("textstats.io.open", return_value=stream, create=True):
            with self.assertRaises(UnicodeDecodeError):
                count_file("named")
        self.assertTrue(stream.closed)

    def test_read_failure_preserves_exception_and_closes(self):
        class BrokenReader(io.BytesIO):
            def read(self, *args):
                raise OSError("controlled read failure")
        stream = BrokenReader()
        with patch("textstats.io.open", return_value=stream, create=True):
            with self.assertRaisesRegex(OSError, "controlled read failure"):
                count_file("named")
        self.assertTrue(stream.closed)

    def test_open_failure_preserves_oserror_subclasses(self):
        for failure in [PermissionError("unreadable"), FileNotFoundError("missing"), IsADirectoryError("directory")]:
            with self.subTest(failure=type(failure)):
                with patch("textstats.io.open", side_effect=failure, create=True):
                    with self.assertRaises(type(failure)) as raised:
                        count_file("named")
                self.assertIs(raised.exception, failure)
