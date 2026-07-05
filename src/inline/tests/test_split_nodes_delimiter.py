import unittest
from inline.textnode import TextNode, TextType
from inline.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [
            TextNode("This is a text node with **bold** and *italic* text.", TextType.TEXT),
            TextNode("This is another text node.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        expected_result = [
            TextNode("This is a text node with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and *italic* text.", TextType.TEXT),
            TextNode("This is another text node.", TextType.TEXT)
        ]
        
        self.assertEqual(result, expected_result)

        def test_split_nodes_delimiter_italic(self):
            old_nodes = [
                TextNode("This is a text node with **bold** and _italic_ text.", TextType.TEXT),
                TextNode("This is another text node.", TextType.TEXT)
            ]
            delimiter = "_"
            text_type = TextType.ITALIC
            result = split_nodes_delimiter(old_nodes, delimiter, text_type)
            
            expected_result = [
                TextNode("This is a text node with **bold** and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
                TextNode("This is another text node.", TextType.TEXT)
            ]
            
            self.assertEqual(result, expected_result)
        
        def test_split_nodes_delimiter_unmatched_delimiter(self):
            old_nodes = [
                TextNode("This is a text node with **bold and *italic* text.", TextType.TEXT),
                TextNode("This is another text node.", TextType.TEXT)
            ]
            delimiter = "**"
            text_type = TextType.BOLD
            
            with self.assertRaises(Exception) as context:
                split_nodes_delimiter(old_nodes, delimiter, text_type)
            
            self.assertEqual(str(context.exception), "Unmatched delimiter found in text node.")
        
        def test_split_nodes_delimiter_code(self):
            old_nodes = [
                TextNode("This is a text node with `code` and **bold** text.", TextType.TEXT),
                TextNode("This is another text node.", TextType.TEXT)
            ]
            delimiter = "`"
            text_type = TextType.CODE
            result = split_nodes_delimiter(old_nodes, delimiter, text_type)
            
            expected_result = [
                TextNode("This is a text node with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and **bold** text.", TextType.TEXT),
                TextNode("This is another text node.", TextType.TEXT)
            ]
            
            self.assertEqual(result, expected_result)
        
if __name__ == "__main__":
    unittest.main()