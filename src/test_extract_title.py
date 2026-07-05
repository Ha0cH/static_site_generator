import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# My Title"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_with_no_title(self):
        md = "This is a paragraph."
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_extract_title_multiple_lines(self):
        md = "Some text here.\n# My Title\nMore text."
        self.assertEqual(extract_title(md), "My Title")