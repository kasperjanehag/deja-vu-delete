from dejavu.file_handlers import ImageFileHandler
import eel

eel.init('src/dejavy-frontend/dist/')

@eel.expose
def find_duplicates_python():
    base_path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/"
    image_file_handler = ImageFileHandler(path)
    image_file_handler.find_duplicates_by_average_hash()
    return image_file_handler.find_duplicates_by_md5_hash()

@eel.expose
def list_images():
    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/"  # Specify the directory
    image_file_handler = ImageFileHandler(path)
    image_files = image_file_handler.images
    return [str(image.relative_path) for image in image_files]

if __name__ == "__main__":
    eel.start('index.html', size=(800, 600), mode='chrome-app', cmdline_args=['--auto-open-devtools-for-tabs'])
