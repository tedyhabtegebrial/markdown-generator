from .helper import MarkdownTestCase

from markdown_generator import Code


class CodeTest(MarkdownTestCase):
    def test_empty(self):
        self.assertRenderedEqual(Code(), '')

    def test_empty_with_language(self):
        code = Code('Python')
        self.assertRenderedEqual(code, '')

    def test_single_line(self):
        code = Code()
        code.append('print("test")')
        self.assertRenderedEqual(code, '```\nprint("test")\n```\n')

    def test_single_line_with_language(self):
        code = Code('Python')
        code.append('print("test")')
        self.assertRenderedEqual(code, '```Python\nprint("test")\n```\n')

    def test_multiple_lines(self):
        code = Code()
        code.append('print("test")')
        code.append('print("test2")')
        self.assertRenderedEqual(
            code,
            '```\nprint("test")\nprint("test2")\n```\n'
        )

    def test_multiple_lines_with_language(self):
        code = Code('Python')
        code.append('print("test")')
        code.append('print("test2")')
        self.assertRenderedEqual(
            code,
            '```Python\nprint("test")\nprint("test2")\n```\n'
        )
