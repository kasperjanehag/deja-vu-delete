from dejavu.file_handlers import ImageFileHandler
import eel
from typing import Any, Iterator, Union
from pathlib import Path

eel.init('src/dejavy-frontend/dist/')

FileNode = dict[str, Union[int, str, bool, list[dict[str, Any]]]]

@eel.expose
def find_duplicates_python():
    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/tests/"
    image_file_handler = ImageFileHandler(path)
    image_file_handler.find_duplicates_by_average_hash()
    return image_file_handler.find_duplicates_by_md5_hash()

def add_to_tree(tree, path_parts, id_counter):
    if not path_parts:
        return
    
    current_part = path_parts[0]
    remaining_parts = path_parts[1:]

    # Check if the current part is already in the tree
    for item in tree:
        if item['name'] == current_part:
            # If it's a folder, continue building the tree recursively
            if remaining_parts:
                add_to_tree(item['children'], remaining_parts, id_counter)
            return

    # If the part is not in the tree, add it
    if remaining_parts:  # It's a folder
        new_item = {
            "id": next(id_counter),
            "name": current_part,
            "icon": 'mdi-plus-outline',
            "isOpen": False,
            "children": []
        }
        tree.append(new_item)
        add_to_tree(new_item['children'], remaining_parts, id_counter)
    else:  # It's a file
        tree.append({
            "id": next(id_counter),
            "name": current_part,
            "icon": 'mdi-file-outline'  # Change icon for files
        })

def convert_image_files_to_structure(image_paths: list[Path]) -> tuple[FileNode]:
    tree = []
    id_counter = iter(range(1, len(image_paths) * 2))  # Assuming enough IDs for files and folders
    for image_path in image_paths:
        parts = list(image_path.parts)
        add_to_tree(tree, parts, id_counter)
    return tuple(tree)


@eel.expose
def list_images():
    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/tests/"
    image_file_handler = ImageFileHandler(path)
    image_files = image_file_handler.images
    return convert_image_files_to_structure([file.relative_path for file in image_files])

if __name__ == "__main__":
    eel.start('index.html', size=(800, 600), mode='chrome-app', cmdline_args=['--auto-open-devtools-for-tabs'])
