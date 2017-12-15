from .helper import MarkdownTestCase
from markdown_generator import Image


class ImageTest(MarkdownTestCase):
    def test_url_empty(self):
        self.assertRenderedEqual(Image(''), '')

    def test_url_none(self):
        self.assertRenderedEqual(Image(''), '')

    def test_valid_url(self):
        self.assertRenderedEqual(Image('image.png'), '![](image.png)')

    def test_valid_url_with_alt_text(self):
        self.assertRenderedEqual(Image('image.png', 'image of thing'),
                                 '![image of thing](image.png)')
