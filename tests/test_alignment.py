import unittest

from markdown_generator import Alignment


class AlignmentTest(unittest.TestCase):
    def test_alignment_none(self):
        with self.assertRaises(ValueError):
            Alignment(None)

    def test_alignment_from_value(self):
        self.assertEqual(Alignment(1), 1)

    def test_invalid_alignment(self):
        with self.assertRaises(ValueError):
            Alignment(999)

    def test_left_or_right_is_center(self):
        self.assertEqual(Alignment.LEFT | Alignment.RIGHT, Alignment.CENTER)
