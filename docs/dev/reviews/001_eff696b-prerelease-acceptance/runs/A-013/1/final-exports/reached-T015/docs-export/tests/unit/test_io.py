"""Owned byte acquisition failures and lifetime are portable controlled seams."""

import io
import unittest
from unittest.mock import patch

from textstats import TextStats, count_file
from textstats import io as acquisition


class BorrowedAcquisitionTests(unittest.TestCase):
    def reader(self):
        reader = getattr(acquisition, '_read_stream_text', None)
        self.assertTrue(callable(reader), 'borrowed binary UTF-8 reader is required')
        return reader

    def test_complete_bytes_preserve_unicode_terminators_and_boms(self):
        reader = self.reader()
        for text in ['', 'α\r\n猫\rβ γ\n', '\ufeff', '\ufeff\ufeffa\n\ufeff']:
            with self.subTest(text=text):
                stream = io.BytesIO(text.encode('utf-8'))
                self.assertEqual(reader(stream), text)
                self.assertEqual(stream.read(), b'')
                self.assertFalse(stream.closed)

    def test_invalid_bytes_after_valid_prefix_preserve_borrowed_ownership(self):
        reader = self.reader()
        stream = io.BytesIO(b'valid\r\n\xff')
        with self.assertRaises(UnicodeDecodeError):
            reader(stream)
        self.assertFalse(stream.closed)

    def test_read_failure_propagates_without_closing_borrowed_stream(self):
        reader = self.reader()
        failure = OSError('controlled borrowed read failure')
        class BrokenReader(io.BytesIO):
            def read(self, *args):
                raise failure
        stream = BrokenReader()
        with self.assertRaises(OSError) as raised:
            reader(stream)
        self.assertIs(raised.exception, failure)
        self.assertFalse(stream.closed)


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
