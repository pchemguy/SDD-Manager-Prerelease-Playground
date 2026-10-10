"""Strict UTF-8 acquisition and owned-handle lifetime under SPEC R-006."""

import contextlib
import io
import unittest
from unittest.mock import patch

from textstats import TextStats, count_file


class FailingRead(io.BytesIO):
    """Expose valid partial bytes, then fail instead of delivering a result."""

    error = BlockingIOError('controlled read failure')

    def read(self, *args):
        super().read(1)
        raise self.error


class FileAcquisitionTests(unittest.TestCase):
    def test_success_closes_owned_handle_without_newline_translation(self):
        stream = io.BytesIO('α\r\nβ\rγ\n'.encode('utf-8'))
        with patch('textstats.io.open', return_value=stream, create=True) as opener:
            self.assertEqual(count_file('sample'), TextStats(3, 3))
        self.assertTrue(stream.closed)
        opener.assert_called_once_with('sample', 'rb')

    def test_bom_policy_preserves_repeated_and_interior_boms(self):
        for data, default, retained in ((b'\xef\xbb\xbf', (0, 0), (1, 1)),
                                       ('\ufeff\ufeff'.encode(), (1, 1), (1, 1)),
                                       ('a\n\ufeff'.encode(), (2, 2), (2, 2))):
            for policy, expected in ((True, default), (False, retained)):
                with self.subTest(data=data, policy=policy):
                    stream = io.BytesIO(data)
                    with patch('textstats.io.open', return_value=stream, create=True):
                        self.assertEqual(count_file('sample', strip_bom=policy),
                                         TextStats(*expected))
                    self.assertTrue(stream.closed)

    def test_open_oserror_subclasses_propagate_unchanged_and_silently(self):
        for error in (FileNotFoundError('missing'), PermissionError('denied'),
                      IsADirectoryError('directory')):
            with self.subTest(error=error):
                stdout, stderr = io.StringIO(), io.StringIO()
                with patch('textstats.io.open', side_effect=error, create=True), \
                        contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    with self.assertRaises(type(error)) as caught:
                        count_file('sample')
                self.assertIs(caught.exception, error)
                self.assertEqual((stdout.getvalue(), stderr.getvalue()), ('', ''))

    def test_read_failure_closes_and_propagates_without_counting_partial_input(self):
        stream = FailingRead(b'valid partial input')
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch('textstats.io.open', return_value=stream, create=True), \
                patch('textstats.io.count_text', create=True) as counter, \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            with self.assertRaises(BlockingIOError) as caught:
                count_file('sample')
            self.assertIs(caught.exception, stream.error)
            counter.assert_not_called()
        self.assertTrue(stream.closed)
        self.assertEqual((stdout.getvalue(), stderr.getvalue()), ('', ''))

    def test_strict_decode_failure_closes_without_counting_partial_input(self):
        for invalid in (b'valid text\xff', b'\xef\xbb\xbfvalid\xc3', b'\xc0\xaf'):
            with self.subTest(invalid=invalid):
                stream = io.BytesIO(invalid)
                stdout, stderr = io.StringIO(), io.StringIO()
                with patch('textstats.io.open', return_value=stream, create=True), \
                        patch('textstats.io.count_text', create=True) as counter, \
                        contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    with self.assertRaises(UnicodeDecodeError):
                        count_file('sample')
                    counter.assert_not_called()
                self.assertTrue(stream.closed)
                self.assertEqual((stdout.getvalue(), stderr.getvalue()), ('', ''))


if __name__ == '__main__':
    unittest.main()
