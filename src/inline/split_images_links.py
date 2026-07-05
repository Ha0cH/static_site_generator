from .textnode import TextNode, TextType
from .extract_markdown_images_links import extract_markdown_images, extract_markdown_links

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return []

    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue

        #loop version:
        remaining_text = node.text
        for alt_text, url in images:
            strings = remaining_text.split(f"![{alt_text}]({url})", 1)
            if strings[0] != "": #if not empty string
                result.append(TextNode(strings[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = strings[1] #update remaining text to the part after the image
        if remaining_text != "": #if not empty string
            result.append(TextNode(remaining_text, TextType.TEXT)) #append any remaining text after the last image
        

        #recursion version:
        #alt_text, url = images[0]
        #strings = node.text.split(f"![{alt_text}]({url})", 1)
        #if strings[0] != "": #if not empty string
        #    result.append(TextNode(strings[0], TextType.TEXT))
        #result.append(TextNode(alt_text, TextType.IMAGE, url))
        #if strings[1] != "": #if not empty string
        #   sub_result = split_nodes_images([TextNode(strings[1], TextType.TEXT)]) #recursively split the remaining text
        #   result.extend(sub_result)
    
    return result

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return []
    
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue

        remaining_text = node.text
        for text, url in links:
            strings = remaining_text.split(f"[{text}]({url})", 1)
            if strings[0] != "":
                result.append(TextNode(strings[0], TextType.TEXT))
            result.append(TextNode(text, TextType.LINK, url))
            remaining_text = strings[1] #update remaining text to the part after the link for the next iteration
        
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT)) #append any remaining text after the last link
        
    return result
            