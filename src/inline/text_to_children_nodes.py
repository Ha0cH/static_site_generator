from .text_to_textnodes import text_to_textnodes
from .textnode import TextNode, TextType, text_node_to_html_node
from .leafnode import LeafNode

#for inline markdown text, we want to convert it to a list of LeafNode objects, which can be used to generate HTML.
def text_to_children_nodes(text: str) -> list[LeafNode]:
    textnodes = text_to_textnodes(text)
    children_nodes = [text_node_to_html_node(node) for node in textnodes]
    return children_nodes
