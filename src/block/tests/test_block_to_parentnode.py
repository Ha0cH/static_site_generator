import unittest
from block.block_to_parentnode import block_to_parentnode

class TestBlockToParentNode(unittest.TestCase):
    def test_paragraph(self):
        node = block_to_parentnode("This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_heading(self):
        node = block_to_parentnode("## This is a heading")
        self.assertEqual(node.to_html(), "<h2>This is a heading</h2>")

    def test_unordered_list(self):
        node = block_to_parentnode("- Item 1\n- Item 2")
        self.assertEqual(node.to_html(), "<ul><li>Item 1</li><li>Item 2</li></ul>")

    def test_ordered_list(self):
        node = block_to_parentnode("1. Item 1\n2. Item 2")
        self.assertEqual(node.to_html(), "<ol><li>Item 1</li><li>Item 2</li></ol>")

    def test_quote(self):
        node = block_to_parentnode("> This is a quote\n> second line")
        self.assertEqual(node.to_html(), "<blockquote>This is a quote second line</blockquote>")

    def test_code(self):
        node = block_to_parentnode("```\ndef hello():\n    print('hi')\n```")
        self.assertEqual(
            node.to_html(),
            "<pre><code>def hello():\n    print('hi')</code></pre>",
        )

    def test_inline_markdown_in_paragraph(self):
        node = block_to_parentnode("This is **bold** and _italic_.")
        self.assertEqual(
            node.to_html(),
            "<p>This is <b>bold</b> and <i>italic</i>.</p>",
        )