import os

def delete_contents_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            delete_contents_in_directory(file_path)

def copy_files_from_source_to_destination_dir(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Destination directory '{destination_dir}' created.")

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        if os.path.isfile(source_file):
            with open(source_file, 'rb') as src_file:
                with open(destination_file, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            print(f"Copied '{source_file}' to '{destination_file}'.")
        elif os.path.isdir(source_file):
            if not os.path.exists(destination_file):
                os.makedirs(destination_file)
            copy_files_from_source_to_destination_dir(source_file, destination_file)
