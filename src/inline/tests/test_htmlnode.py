import unittest
from inline.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", props={"href": "https://example.com"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://example.com"})
    
    def test_init_with_children(self):
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        node = HTMLNode(tag="div", children=[child1, child2])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "my-class", "id": "my-id"})
        expected_html = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_html)
    
    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode(tag="span", value="Hello", props={"style": "color: red;"})
        expected_repr = "HTMLNode(tag: span, value: Hello, children: None, props: {'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)
    

if __name__ == "__main__":
    unittest.main()