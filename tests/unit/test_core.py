"""Independent examples protecting the accepted whole-text contracts."""

import unittest
from textstats import TextStats, count_text


class StatisticsTests(unittest.TestCase):
    def test_value_fields_and_equality(self):
        value = TextStats(2, 3)
        self.assertEqual((value.lines, value.words), (2, 3))
        self.assertEqual(value, TextStats(2, 3))
        self.assertNotEqual(value, TextStats(3, 2))
        self.assertEqual(TextStats(0, 0).lines, 0)

    def test_fields_cannot_be_changed_or_deleted(self):
        value = TextStats(2, 3)
        for field in ("lines", "words"):
            with self.subTest(field=field):
                with self.assertRaises(AttributeError):
                    setattr(value, field, 9)
                with self.assertRaises(AttributeError):
                    delattr(value, field)
        self.assertEqual((value.lines, value.words), (2, 3))

    def test_negative_values_are_rejected_in_either_field(self):
        for counts in ((-1, 0), (0, -1), (-1, -1)):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                TextStats(*counts)

    def test_nonintegers_including_booleans_are_rejected(self):
        for invalid in (True, False, 1.0, -1.0, "1", None, [], complex(1)):
            for counts in ((invalid, 0), (0, invalid)):
                with self.subTest(counts=counts), self.assertRaises(TypeError):
                    TextStats(*counts)


class WholeTextTests(unittest.TestCase):
    def test_complete_spec_matrix_under_both_policies(self):
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
            for policy, expected in ((True, stripped), (False, retained)):
                with self.subTest(text=text, strip_bom=policy):
                    actual = count_text(text, strip_bom=policy)
                    self.assertEqual((actual.lines, actual.words), expected)

    def test_mixed_and_adjacent_terminators_with_final_segment(self):
        for text, expected in [
            ("\r\n\r\n", (2, 0)), ("\r\r\n\n", (3, 0)),
            ("a\r\nb\rc\nd", (4, 4)), ("\n\r", (2, 0)),
            ("a\r\n\nlast", (3, 2)),
        ]:
            with self.subTest(text=text):
                actual = count_text(text)
                self.assertEqual((actual.lines, actual.words), expected)

    def test_unicode_whitespace_does_not_add_line_terminators(self):
        text = "café\u0085茶\u2028beta\u2029gamma\u00a0delta\vfinal\f"
        actual = count_text(text)
        self.assertEqual((actual.lines, actual.words), (1, 6))

    def test_bom_normalized_only_once_and_interior_preserved(self):
        for text, stripped, retained in [
            ("\ufeff\n", (1, 0), (1, 1)),
            ("\ufeff\ufeff\n", (1, 1), (1, 1)),
            ("\ufeff\ufeff ", (1, 1), (1, 1)),
            ("a\n\ufeff", (2, 2), (2, 2)),
            (" \ufeff", (1, 1), (1, 1)),
        ]:
            for policy, expected in ((True, stripped), (False, retained)):
                with self.subTest(text=text, strip_bom=policy):
                    actual = count_text(text, strip_bom=policy)
                    self.assertEqual((actual.lines, actual.words), expected)


if __name__ == "__main__":
    unittest.main()
