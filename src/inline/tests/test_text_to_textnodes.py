import unittest
from inline.textnode import TextNode, TextType
from inline.text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is a **bold** text and this is _italic_ text. Here is a `code` snippet."
        result = text_to_textnodes(text)
        
        expected_result = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text and this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text. Here is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet.", TextType.TEXT)
        ]
        
        self.assertListEqual(result, expected_result)
    
    def test_text_to_textnodes_with_links_and_images(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://youtube.com)"
        result = text_to_textnodes(text)
        
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://youtube.com"),
        ]
        
        self.assertListEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()