import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()
    title = extract_title(content)

    final_html = (
            template
            .replace("{{ Title }}", title)
            .replace("{{ Content }}", html_content)
            .replace('href="/', f'href="{basepath}')
            .replace('src="/', f'src="{basepath}')
    )
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(final_html)