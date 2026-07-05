from copy_files_from_source_to_destination_dir import copy_files_from_source_to_destination_dir, delete_contents_in_directory
from content_generation import generate_pages_from_directory
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    source_dir = "static"
    destination_dir = "docs"

    # Delete contents of the destination directory
    delete_contents_in_directory(destination_dir)

    # Copy files from source to destination
    copy_files_from_source_to_destination_dir(source_dir, destination_dir)

    # Generate HTML pages from Markdown files
    generate_pages_from_directory("./content", "./template.html", destination_dir, basepath)

if __name__ == "__main__":
    main()