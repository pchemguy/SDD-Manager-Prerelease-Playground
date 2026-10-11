"""Public text/file API imports, signatures, silence and real-file preservation."""

import contextlib
import inspect
import io
import unittest
import tempfile
from os import PathLike
from pathlib import Path

import textstats
from textstats import TextStats, count_text, count_file


class PublicTextApiTests(unittest.TestCase):
    def test_public_exports_match_the_core(self):
        from textstats import core
        self.assertIs(TextStats, core.TextStats)
        self.assertIs(count_text, core.count_text)
        self.assertEqual(set(textstats.__all__), {'TextStats', 'count_text', 'count_file'})
        from textstats import io as file_io
        self.assertIs(count_file, file_io.count_file)

    def test_signature_is_whole_text_with_keyword_only_policy(self):
        signature = inspect.signature(count_text)
        self.assertEqual(list(signature.parameters), ['text', 'strip_bom'])
        self.assertEqual(signature.parameters['text'].kind,
                         inspect.Parameter.POSITIONAL_OR_KEYWORD)
        self.assertEqual(signature.parameters['strip_bom'].kind,
                         inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(signature.parameters['strip_bom'].default, True)
        self.assertIs(signature.parameters['text'].annotation, str)
        self.assertIs(signature.return_annotation, TextStats)
        with self.assertRaises(TypeError):
            count_text('text', False)

    def test_public_calls_are_silent_and_preserve_input(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        text = '\ufeffalpha\r\nbeta\rgamma\n'
        original = text
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            default = count_text(text)
            retained = count_text(text, strip_bom=False)
            value = TextStats(3, 3)
        self.assertEqual(default, value)
        self.assertEqual(retained, value)
        self.assertEqual(text, original)
        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(stderr.getvalue(), '')

    def test_public_bom_and_empty_results(self):
        for text, default, retained in (('', (0, 0), (0, 0)),
                                        ('\ufeff', (0, 0), (1, 1)),
                                        ('\ufeff\ufeff', (1, 1), (1, 1)),
                                        ('alpha\u2028beta', (1, 2), (1, 2))):
            with self.subTest(text=text):
                self.assertEqual(count_text(text), TextStats(*default))
                self.assertEqual(count_text(text, strip_bom=False), TextStats(*retained))


class PublicFileApiTests(unittest.TestCase):
    def test_file_signature_and_keyword_only_policy(self):
        signature = inspect.signature(count_file)
        self.assertEqual(list(signature.parameters), ['path', 'strip_bom'])
        self.assertEqual(signature.parameters['path'].kind,
                         inspect.Parameter.POSITIONAL_OR_KEYWORD)
        self.assertEqual(signature.parameters['strip_bom'].kind,
                         inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(signature.parameters['strip_bom'].default, True)
        self.assertEqual(signature.parameters['path'].annotation, str | PathLike[str])
        self.assertIs(signature.parameters['strip_bom'].annotation, bool)
        self.assertIs(signature.return_annotation, TextStats)
        with self.assertRaises(TypeError):
            count_file('sample', False)

    def test_real_file_spec_matrix_matches_text_and_preserves_bytes_silently(self):
        cases = (('', (0, 0)), ('alpha beta', (1, 2)), ('alpha\n', (1, 1)),
                 ('\n', (1, 0)), ('alpha\r\nbeta\rgamma\n', (3, 3)),
                 ('alpha\n\n', (2, 1)), (' \t', (1, 0)),
                 ('alpha\u2028beta', (1, 2)), ('\ufeff', (0, 0)),
                 ('\ufeff\ufeff', (1, 1)), ('\ufeffalpha beta', (1, 2)),
                 ('a\ufeffb', (1, 1)), ('\r\n', (1, 0)), ('\r', (1, 0)),
                 ('你好\t café\nnaïve', (2, 3)))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            for text, expected in cases:
                original = text.encode('utf-8')
                path.write_bytes(original)
                for value in (str(path), path):
                    for policy in (True, False):
                        result = (1, 1) if text == '\ufeff' and not policy else expected
                        with self.subTest(text=text, path_type=type(value), policy=policy):
                            stdout, stderr = io.StringIO(), io.StringIO()
                            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                                actual = count_file(value, strip_bom=policy)
                            self.assertEqual(actual, TextStats(*result))
                            self.assertEqual(actual, count_text(text, strip_bom=policy))
                            self.assertEqual(path.read_bytes(), original)
                            self.assertEqual((stdout.getvalue(), stderr.getvalue()), ('', ''))

    def test_real_missing_file_and_invalid_bytes_preserve_exception_and_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.txt'
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                with self.assertRaises(FileNotFoundError):
                    count_file(path)
                original = b'valid prefix\xff'
                path.write_bytes(original)
                with self.assertRaises(UnicodeDecodeError):
                    count_file(path)
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual((stdout.getvalue(), stderr.getvalue()), ('', ''))


if __name__ == '__main__':
    unittest.main()
