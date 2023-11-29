from dejavu.file_handlers import ImageFileHandler
import eel

eel.init('src/dejavy-frontend/dist/')

@eel.expose
def find_duplicates_python():
    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/"
    image_file_handler = ImageFileHandler(path)
    image_file_handler.find_duplicates_by_average_hash()
    return image_file_handler.find_duplicates_by_md5_hash()


@eel.expose
def list_images():
    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/"  # Specify the directory
    image_file_handler = ImageFileHandler(path)
    image_files = image_file_handler.images
    # return [str(image.relative_path) for image in image_files]
    return (
        {
            "id": 1,
            "name": 'File 1',
            "icon": 'mdi-account-multiple-outline',
        },
        {
            "id": 2,
            "name": 'Folder 1',
            "icon": 'mdi-plus-outline',
            "isOpen": False,
            "children": [
                {
                    "id": 3,
                    "name": 'File 2',
                    "icon": 'mdi-account-multiple-outline',
                },
                {
                    "id": 4,
                    "name": 'File 3',
                    "icon": 'mdi-cog-outline',
                },
                {
                    "id": 5,
                    "name": 'Sub Folder 1',
                    "icon": 'mdi-plus-outline',
                    "isOpen": False,
                    "children": [
                        {
                            "id": 6,
                            "name": 'File 2',
                            "icon": 'mdi-account-multiple-outline',
                        },
                        {
                            "id": 7,
                            "name": 'File 3',
                            "icon": 'mdi-cog-outline',
                        },
                    ],
                },
                {
                    "id": 8,
                    "name": 'Sub Folder 2',
                    "isOpen": False,
                    "icon": 'mdi-database',
                    "children": [
                        { "id": 9, "name": 'Create', "icon": 'mdi-plus-outline' },
                        { "id": 10, "name": 'Read', "icon": 'mdi-file-outline' },
                        { "id": 11, "name": 'Update', "icon": 'mdi-update' },
                        { "id": 12, "name": 'Delete', "icon": 'mdi-delete' },
                    ],
                },
            ],
        },
    )

if __name__ == "__main__":
    eel.start('index.html', size=(800, 600), mode='chrome-app', cmdline_args=['--auto-open-devtools-for-tabs'])
