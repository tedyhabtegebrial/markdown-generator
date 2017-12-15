from .helper import MarkdownTestCase

from markdown_generator import BlockQuote


class TestBlockQuote(MarkdownTestCase):
    def assertRenderedEqual(self, bq, expected):
        self.assertEqual(str(bq), expected)

    def test_empty(self):
        self.assertRenderedEqual(BlockQuote(), '')

    def test_single_line(self):
        bq = BlockQuote()
        bq.append('My quote here')
        self.assertRenderedEqual(bq, '> My quote here\n\n')

    def test_multiple_lines(self):
        bq = BlockQuote()
        bq.append('My quote here')
        bq.append('Longer quote')
        bq.append('Even longer')
        expected = ('> My quote here\n'
                    '> Longer quote\n'
                    '> Even longer\n\n')
        self.assertRenderedEqual(bq, expected)

    def test_level_other_than_one_empty(self):
        self.assertRenderedEqual(BlockQuote(2), '')

    def test_level_other_than_one_single_line(self):
        bq = BlockQuote(3)
        bq.append('My quote here')
        self.assertRenderedEqual(bq, '>>> My quote here\n\n')

    def test_level_other_than_one_multi_line(self):
        bq = BlockQuote(2)
        bq.append('My quote here')
        bq.append('Longer quote')
        bq.append('Even longer')
        expected = ('>> My quote here\n'
                    '>> Longer quote\n'
                    '>> Even longer\n\n')
        self.assertRenderedEqual(bq, expected)
