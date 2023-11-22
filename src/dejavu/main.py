from dejavu.file_handlers import ImageFileHandler

if __name__ == "__main__":

    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/tests/test_set_1"
    file_handler = ImageFileHandler(path)
    for image in file_handler.files[0:5]:
        print(image)
