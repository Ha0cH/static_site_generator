import unittest
from inline.parentnode import ParentNode
from inline.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_init(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        node = ParentNode(tag="div", children=[child1, child2], props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, {"class": "container"})
    
    def test_nested_parent_nodes(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent_node = ParentNode(tag="div", children=[child1, child2])
        grandparent_node = ParentNode(tag="section", children=[parent_node])
        self.assertEqual(grandparent_node.tag, "section")
        self.assertEqual(grandparent_node.value, None)
        self.assertEqual(grandparent_node.children, [parent_node])
        self.assertEqual(grandparent_node.props, None)
    
    def test_init_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[])
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_init_with_no_tag(self):
        child1 = LeafNode(tag="span", value="Child 1")
        with self.assertRaises(ValueError):
            ParentNode(tag="", children=[child1])


    def test_to_html_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("b", "two")
        node = ParentNode("div", [child1, child2])

        self.assertEqual(
            node.to_html(),
            "<div><span>one</span><b>two</b></div>"
            )
    
    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        node = ParentNode("div", [child], {"class": "container"})

        self.assertEqual(
            node.to_html(),
            '<div class="container"><span>child</span></div>'
        )

if __name__ == "__main__":
    unittest.main()