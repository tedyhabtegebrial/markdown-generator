from .helper import MarkdownTestCase

from markdown_generator.emphasis import (
    emphasis,
    strikethrough,
    strong,
    wrap,
)


class EmphasisTest(MarkdownTestCase):
    def test_wrap(self):
        self.assertEqual(wrap('test', 'tag'), 'tagtesttag')

    def test_wrap_empty_tag(self):
        self.assertEqual(wrap('test', ''), 'test')

    def test_wrap_empty_text(self):
        self.assertEqual(wrap('', 'tag'), '')

    def test_emphasis(self):
        self.assertEqual(emphasis('text'), '*text*')

    def test_emphasis_empty(self):
        self.assertEqual(emphasis(''), '')

    def test_strikethrough(self):
        self.assertEqual(strikethrough('text'), '~~text~~')

    def test_strikethrough_empty(self):
        self.assertEqual(strikethrough(''), '')

    def test_strong(self):
        self.assertEqual(strong('text'), '**text**')

    def test_strong_empty(self):
        self.assertEqual(strong(''), '')
