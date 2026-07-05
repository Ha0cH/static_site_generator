import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    QUOTE = "quote"
    CODE= "code"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    #checking for heading
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
    
    #checking for code block
    if lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE

    #checking for quote block
    quote_block = True
    for line in lines:
        if not re.match(r"^>", line):
             quote_block = False
             break
    if quote_block:
        return BlockType.QUOTE
    
    #checking for unordered list
    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    
    #checking for ordered list
    expected_number = 1
    ordered_list = True
    for line in lines:
        if line.startswith(f"{expected_number}. "):
            expected_number += 1
        else:
            ordered_list = False
            break
    if ordered_list:
        return BlockType.ORDERED_LIST
    
    #none of the above conditions are met, so it's a paragraph
    return BlockType.PARAGRAPH