"""Independent expectations from SPEC R-001 and R-003 through R-005."""

import dataclasses
import unittest

from textstats.core import TextStats, count_text


class TextStatsTests(unittest.TestCase):
    def test_value_equality_and_integer_fields(self):
        value = TextStats(2, 3)
        self.assertEqual(value, TextStats(lines=2, words=3))
        self.assertNotEqual(value, TextStats(3, 2))
        self.assertEqual((value.lines, value.words), (2, 3))
        self.assertIs(type(value.lines), int)
        self.assertIs(type(value.words), int)

    def test_zero_and_large_counts(self):
        self.assertEqual(TextStats(0, 0).lines, 0)
        self.assertEqual(TextStats(10**100, 10**100).words, 10**100)

    def test_fields_cannot_be_changed_or_deleted(self):
        value = TextStats(1, 2)
        for field in ('lines', 'words'):
            with self.subTest(field=field):
                with self.assertRaises(dataclasses.FrozenInstanceError):
                    setattr(value, field, 9)
                with self.assertRaises(dataclasses.FrozenInstanceError):
                    delattr(value, field)

    def test_negative_count_in_either_field(self):
        for fields in ((-1, 0), (0, -1), (-1, -1)):
            with self.subTest(fields=fields):
                with self.assertRaises(ValueError):
                    TextStats(*fields)

    def test_noninteger_count_in_either_field(self):
        for invalid in (True, False, 0.0, 1.5, '1', None, [], object()):
            for fields in ((invalid, 0), (0, invalid)):
                with self.subTest(fields=fields):
                    with self.assertRaises(TypeError):
                        TextStats(*fields)


class CountingTests(unittest.TestCase):
    def test_spec_whole_input_matrix(self):
        cases = (
            ('', (0, 0)), ('alpha beta', (1, 2)), ('alpha\n', (1, 1)),
            ('\n', (1, 0)), ('alpha\r\nbeta\rgamma\n', (3, 3)),
            ('alpha\n\n', (2, 1)), (' \t', (1, 0)),
            ('alpha\u2028beta', (1, 2)), ('\ufeff', (0, 0)),
            ('\ufeff\ufeff', (1, 1)), ('\ufeffalpha beta', (1, 2)),
            ('a\ufeffb', (1, 1)), ('\r\n', (1, 0)), ('\r', (1, 0)),
        )
        for text, expected in cases:
            for strip_bom in (True, False):
                retained = (1, 1) if text == '\ufeff' else expected
                result = expected if strip_bom else retained
                with self.subTest(text=text, strip_bom=strip_bom):
                    self.assertEqual(count_text(text, strip_bom=strip_bom),
                                     TextStats(*result))

    def test_mixed_terminators_and_final_segments(self):
        cases = (('\r\n\r\n', (2, 0)), ('\n\r', (2, 0)),
                 ('a\r\nb\rc\nd', (4, 4)), ('\r\r\n\n', (3, 0)),
                 ('a\r\n\r', (2, 1)), ('\nlast', (2, 1)))
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_text(text), TextStats(*expected))

    def test_unicode_whitespace_does_not_broaden_line_terminators(self):
        for separator in ('\u0085', '\u2028', '\u2029', '\v', '\f',
                          '\u00a0', '\u2003', '\u3000', '\t'):
            with self.subTest(separator=separator):
                self.assertEqual(count_text('α' + separator + 'β'), TextStats(1, 2))
                self.assertEqual(count_text(separator), TextStats(1, 0))

    def test_normalization_removes_one_bom_only(self):
        for text, expected in (('\ufeff\n', (1, 0)),
                               ('\ufeff\ufeff\n', (1, 1)),
                               ('\n\ufeff', (2, 1)),
                               ('\ufeff\ufeff\ufeff', (1, 1)),
                               ('\ufeff \ufeff', (1, 1))):
            with self.subTest(text=text):
                self.assertEqual(count_text(text), TextStats(*expected))
        self.assertEqual(count_text('\ufeff\n', strip_bom=False), TextStats(1, 1))

    def test_unicode_words_and_whitespace_runs(self):
        self.assertEqual(count_text('你好\t café  \nnaïve'), TextStats(2, 3))
        self.assertEqual(count_text('  \t\r\n \u2029'), TextStats(2, 0))


if __name__ == '__main__':
    unittest.main()
