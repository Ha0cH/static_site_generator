from platform import node
import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )
    
    def test_heading(self):
        md = "# This is a heading"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
        "<div><h1>This is a heading</h1></div>",
        )


    def test_unordered_list(self):
        md = """
- Apple
- Banana
- Cherry
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul></div>",
        )


    def test_ordered_list(self):
        md = """
1. Apple
2. Banana
3. Cherry
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>Apple</li><li>Banana</li><li>Cherry</li></ol></div>",
        )


    def test_blockquote(self):
        md = """
> This is a quote
> spanning two lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spanning two lines</blockquote></div>",
        )


    def test_heading_with_inline_markdown(self):
        md = "# This is **bold** and _italic_"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>This is <b>bold</b> and <i>italic</i></h1></div>",
        )


    def test_list_with_inline_markdown(self):
        md = """
- **Bold**
- _Italic_
- `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li><b>Bold</b></li><li><i>Italic</i></li><li><code>code</code></li></ul></div>",
        )


    def test_mixed_document(self):
        md = """
# My Title

This is a paragraph.

- Apple
- Banana

> A famous quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>My Title</h1><p>This is a paragraph.</p><ul><li>Apple</li><li>Banana</li></ul><blockquote>A famous quote</blockquote></div>",
        )