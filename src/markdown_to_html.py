from block.markdown_to_blocks import markdown_to_blocks
from block.block_to_parentnode import block_to_parentnode
from inline.parentnode import ParentNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    if not markdown:
        raise Exception("markdown document is empty.")

    blocks = markdown_to_blocks(markdown) #Split markdown into cleaned block strings

    children_nodes = []
    for block in blocks:
        parent_node = block_to_parentnode(block)
        children_nodes.append(parent_node)

    return ParentNode(tag="div", children=children_nodes)

