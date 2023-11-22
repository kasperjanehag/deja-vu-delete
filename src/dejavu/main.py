from dejavu.file_handlers import ImageFileHandler

if __name__ == "__main__":

    path = "D:\photos"
    file_handler = ImageFileHandler(path)
    file_handler.list_files()
    images = file_handler.files
    for image in images[0:5]:
        print(image)
