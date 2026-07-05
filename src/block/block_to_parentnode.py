from .block_to_block_type import BlockType, block_to_block_type
from inline.parentnode import ParentNode
from inline.leafnode import LeafNode
from inline.text_to_children_nodes import text_to_children_nodes

def block_to_parentnode(block: str) -> ParentNode:
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        text = " ".join(line.strip() for line in block.split("\n"))
        children = text_to_children_nodes(text)
        return ParentNode(tag="p", children=children, props=None)
    
    elif block_type == BlockType.HEADING:
        heading_level = len(block.split(" ")[0])  # Count the number of '#' characters
        children = text_to_children_nodes(block[heading_level+1:])
        return ParentNode(tag=f"h{heading_level}", children=children, props=None)
    
    elif block_type == BlockType.UNORDERED_LIST:
        list_items = block.split("\n")
        list_items = [item[2:].strip() for item in list_items]  # Remove the '- ' prefix
        children = [ParentNode(tag="li", children=text_to_children_nodes(item), props=None) for item in list_items]
        return ParentNode(tag="ul", children=children, props=None)
    
    elif block_type == BlockType.ORDERED_LIST:
        list_items = block.split("\n")
        list_items = [item.split(". ", 1)[1] for item in list_items]  # Remove the '1. ', '2. ', etc. prefix
        children = [ParentNode(tag="li", children=text_to_children_nodes(item), props=None) for item in list_items]
        return ParentNode(tag="ol", children=children, props=None)

    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        lines = [line[1:].strip() for line in lines]  # Remove the '>' character and leading whitespace
        text = " ".join(lines)
        children = text_to_children_nodes(text)
        return ParentNode(tag="blockquote", children=children, props=None)

    #special case for code blocks:
    #everything inside the ``` markers should be treated as a single text node, preserving whitespace and newlines
    elif block_type == BlockType.CODE:
        lines = block.split("\n")
        lines = lines[1:-1]  # Remove the first and last lines (the ``` markers)
        code_text = "\n".join(lines)
        code_node = LeafNode(tag="code", value=code_text, props=None)
        return ParentNode(tag="pre", children=[code_node], props=None)
    
    else:
        raise ValueError(f"Unknown block type: {block_type}")