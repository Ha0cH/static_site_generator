import os
from generate_page import generate_page

def generate_pages_from_directory(source_dir, template_path, destination_dir, basepath):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, source_dir)

                relative_no_ext = os.path.splitext(relative_path)[0]

                if os.path.basename(relative_no_ext) == "index":

                    dest_path = os.path.join(destination_dir, os.path.dirname(relative_no_ext), "index.html")

                else:

                    dest_path = os.path.join(destination_dir, relative_no_ext, "index.html")
                generate_page(from_path, template_path, dest_path, basepath)