from .textnode import TextNode, TextType
from .split_nodes_delimiter import split_nodes_delimiter
from .split_images_links import split_nodes_images, split_nodes_links

def text_to_textnodes(text: str) -> list[TextNode]:
    if not text:
        return []
    
    # Initialize a single TextNode of type TEXT with the input text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split by images first
    nodes = split_nodes_images(nodes)
    
    # Then split by links
    nodes = split_nodes_links(nodes)
    
    # Then split by bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Then split by italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Finally, split by code (`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    return nodes