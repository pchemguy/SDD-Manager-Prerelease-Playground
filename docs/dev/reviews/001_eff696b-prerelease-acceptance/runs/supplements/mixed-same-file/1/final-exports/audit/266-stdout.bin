"""Public text API imports, signature and silence at the T-001 boundary."""

import contextlib
import inspect
import io
import unittest

import textstats
from textstats import TextStats, count_text


class PublicTextApiTests(unittest.TestCase):
    def test_public_exports_match_the_core(self):
        from textstats import core
        self.assertIs(TextStats, core.TextStats)
        self.assertIs(count_text, core.count_text)
        self.assertEqual(set(textstats.__all__), {'TextStats', 'count_text'})
        self.assertFalse(hasattr(textstats, 'count_file'))

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


if __name__ == '__main__':
    unittest.main()
