import unittest
from inline.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "text"})
    
    def test_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "text"})
        expected_html = '<p class="text">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)
    
    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Hello, World!")
        expected_html = 'Hello, World!'
        self.assertEqual(node.to_html(), expected_html)
    
    def test_to_html_no_props(self):
        node = LeafNode(tag="span", value="Hello, World!")
        expected_html = '<span>Hello, World!</span>'
        self.assertEqual(node.to_html(), expected_html)
    
    def test_repr(self):
        node = LeafNode(tag="div", value="Hello, World!", props={"id": "main"})
        expected_repr = "LeafNode(tag: div, value: Hello, World!, props: {'id': 'main'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()