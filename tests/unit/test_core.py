"""Independent examples for R-001 and R-003 through R-005."""

from dataclasses import FrozenInstanceError
import unittest

from textstats import TextStats, count_text


class StatisticsTests(unittest.TestCase):
    def test_nonnegative_values_and_equality(self):
        self.assertEqual(TextStats(0, 0), TextStats(0, 0))
        self.assertEqual(TextStats(2, 3).lines, 2)
        self.assertEqual(TextStats(2, 3).words, 3)
        self.assertNotEqual(TextStats(2, 3), TextStats(3, 2))

    def test_each_field_rejects_negative_counts(self):
        for values in [(-1, 0), (0, -1), (-1, -1)]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                TextStats(*values)

    def test_each_field_rejects_nonintegers_including_booleans(self):
        for value in [True, False, 1.0, "1", None, complex(1, 0)]:
            for values in [(value, 0), (0, value)]:
                with self.subTest(values=values), self.assertRaises(TypeError):
                    TextStats(*values)

    def test_fields_cannot_be_assigned_or_deleted(self):
        stats = TextStats(2, 3)
        for field in ["lines", "words"]:
            with self.subTest(field=field), self.assertRaises((AttributeError, FrozenInstanceError)):
                setattr(stats, field, 99)
            with self.subTest(field=field), self.assertRaises((AttributeError, FrozenInstanceError)):
                delattr(stats, field)
        self.assertEqual(stats, TextStats(2, 3))


class CountingTests(unittest.TestCase):
    def test_whole_input_spec_matrix_under_both_policies(self):
        cases = [
            ("", (0, 0), (0, 0)),
            ("alpha beta", (1, 2), (1, 2)),
            ("alpha\n", (1, 1), (1, 1)),
            ("\n", (1, 0), (1, 0)),
            ("alpha\r\nbeta\rgamma\n", (3, 3), (3, 3)),
            ("alpha\n\n", (2, 1), (2, 1)),
            (" \t", (1, 0), (1, 0)),
            ("alpha\u2028beta", (1, 2), (1, 2)),
            ("\ufeff", (0, 0), (1, 1)),
            ("\ufeff\ufeff", (1, 1), (1, 1)),
            ("\ufeffalpha beta", (1, 2), (1, 2)),
            ("a\ufeffb", (1, 1), (1, 1)),
            ("\r\n", (1, 0), (1, 0)),
            ("\r", (1, 0), (1, 0)),
        ]
        for text, stripped, retained in cases:
            for policy, expected in [(True, stripped), (False, retained)]:
                with self.subTest(text=text, strip_bom=policy):
                    result = count_text(text, strip_bom=policy)
                    self.assertEqual((result.lines, result.words), expected)

    def test_only_crlf_cr_and_lf_terminate_lines(self):
        cases = [("\r\n\r\n", (2, 0)), ("\n\r", (2, 0)),
                 ("a\r\nb\rc\nd", (4, 4)), ("\r\nlast", (2, 1))]
        for text, expected in cases:
            with self.subTest(text=text):
                result = count_text(text)
                self.assertEqual((result.lines, result.words), expected)

    def test_unicode_separators_are_whitespace_without_new_lines(self):
        for separator in ["\u0085", "\u2028", "\u2029", "\v", "\f"]:
            with self.subTest(separator=separator):
                self.assertEqual(count_text("a" + separator + "b"), TextStats(1, 2))
                self.assertEqual(count_text(separator), TextStats(1, 0))

    def test_unicode_whitespace_and_non_ascii_words(self):
        self.assertEqual(count_text("  café\u00a0猫\u2003κόσμος\t\n"), TextStats(1, 3))

    def test_normalization_removes_exactly_one_leading_bom(self):
        cases = [("\ufeff\ufeff\n", (1, 1)), ("\ufeff\n\ufeff", (2, 1)),
                 (" \ufeff", (1, 1)), ("\ufeff\r\n", (1, 0))]
        for text, expected in cases:
            with self.subTest(text=text):
                result = count_text(text)
                self.assertEqual((result.lines, result.words), expected)

    def test_repeated_calls_have_no_shared_state(self):
        first = count_text("alpha beta\n")
        self.assertEqual(count_text(""), TextStats(0, 0))
        self.assertEqual(count_text("alpha beta\n"), first)


class SelectionTests(unittest.TestCase):
    def test_preserved_normalized_logical_segments_and_eof(self):
        from textstats.core import _select_lines
        cases = [
            ('', 1, 99, ''), ('alpha beta\nbeta\nlast two', 2, 3, 'beta\nlast two'),
            ('alpha beta\nbeta\nlast two', 2, 99, 'beta\nlast two'),
            ('alpha beta\nbeta\nlast two', 1, 1, 'alpha beta\n'),
            ('alpha beta\nbeta\nlast two', 4, 99, ''),
            ('a\n\n', 2, 9, '\n'), ('a\r\nb c\rd\n', 2, 3, 'b c\rd\n'),
            ('a\n\ufeff', 2, 2, '\ufeff'), ('\n', 1, 1, '\n'),
            ('alpha\u2028beta', 1, 1, 'alpha\u2028beta'),
            ('\ufeff\ufeff', 1, 1, '\ufeff\ufeff'),
        ]
        huge = 10 ** 5000
        cases += [('a\nb', 1, huge, 'a\nb'), ('a\nb', huge, huge, '')]
        for text, start, end, expected in cases:
            with self.subTest(text=text, endpoint_class='huge' if end>100 else 'small'):
                self.assertEqual(_select_lines(text, start, end), expected)

    def test_selection_and_normalized_counting_do_not_strip_exposed_bom(self):
        from textstats.core import _select_lines, _count_normalized, _normalize_text
        for policy in (True, False):
            normalized = _normalize_text('\ufeffa\n\ufeff', policy)
            selected = _select_lines(normalized, 2, 2)
            self.assertEqual(selected, '\ufeff')
            self.assertEqual(_count_normalized(selected), TextStats(1, 1))
        self.assertEqual(_count_normalized(_select_lines('\ufeff', 1, 1)), TextStats(1, 1))


if __name__ == "__main__":
    unittest.main()
