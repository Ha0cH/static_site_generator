import re

def extract_markdown_images(text: str) -> list[tuple]:
    result = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result

def extract_markdown_links(text: str) -> list[tuple]:
    result = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return result

