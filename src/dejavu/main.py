from dejavu.file_handlers import ImageFileHandler

if __name__ == "__main__":

    path = "/Users/kasper_janehag/Documents/repos/deja-vu-delete/tests/test_set_1"
    image_file_handler = ImageFileHandler(path)
    image_file_handler.find_duplicates_by_average_hash()
    image_file_handler.find_duplicates_by_md5_hash()
