import unittest
from block.block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_sub_heading(self):
        block = "## This is a subheading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_too_many_hashes(self):
        block = "####### This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_missing_space(self):
        block = "#This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_missing_space(self):
        block = "-Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_mixed_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n4. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_not_starting_at_one(self):
        block = "2. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_duplicate_ordered_list_number(self):
        block = "1. Item 1\n1. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_missing_space(self):
        block = "1.Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_empty_item(self):
        block = "1. \n2. "
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_quote(self):
        block = "> This is a quote.\n> It can span multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_without_space(self):
        block = ">This is still a quote\n>Second line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_mixed_quote_block(self):
        block = "> This is a quote\nThis line is not"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\ndef hello():\n    print('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_code_block_missing_closing_backticks(self):
        block = "```\ndef hello():\n    print('hi')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_missing_opening_backticks(self):
        block = "def hello():\n    print('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)