def extract_title(markdown: str) -> str:
    """
    Extracts the title from a markdown string. The title is defined as the first line that starts with a '#' character.
    If no title is found, returns an empty string.
    """
    lines = markdown.splitlines()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#"):
            return stripped_line.lstrip("#").strip()
    raise Exception("No title found in the markdown string.") 

