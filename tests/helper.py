import unittest


class MarkdownTestCase(unittest.TestCase):
    def assertRenderedEqual(self, obj, expected):
        return self.assertEqual(str(obj), expected)
