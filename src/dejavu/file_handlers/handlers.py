from abc import ABC, abstractmethod
from pathlib import Path
from dejavu.images import ImageFile
from typing import Generator

class FileHandler(ABC):
    """
    Abstract base class for file handling.
    """
    def __init__(self, path):
        self.path = Path(path)
        self._images = []
        self.image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}
        
        self.average_hash_duplicates = []
        self.average_hashes = {}
        self.md5_hashes = {}
        self.md5_hash_duplicates = []

    @property
    @abstractmethod
    def images(self) -> list[ImageFile]:
        """ Abstract property to get a list of files. """
        pass

class ImageFileHandler(FileHandler):
    """
    Handles image files, inheriting from FileHandler.
    """

    def get_files(self) -> Generator[ImageFile, None, None]:
        """
        Generate image files in the instance's directory recursively as ImageFile instances.
        """
        if not self.path.is_dir():
            raise ValueError(f"{self.path} is not a valid directory.")

        for ext in self.image_extensions:
            for file_path in self.path.rglob(f'*{ext}'):
                if file_path.is_file():
                    yield ImageFile(file_path)

    @property
    def images(self) -> list[ImageFile]:
        """
        Property to get a list of ImageFile instances representing the image files 
        in the instance's directory, done recursively.

        Returns:
            list[ImageFile]: A list of ImageFile instances.

        Raises:
            ValueError: If the specified path is not a valid directory.
        """
        if not self.path.is_dir():
            raise ValueError(f"{self.path} is not a valid directory.")

        self._images = []  # Reset the list
        for ext in self.image_extensions:
            for file_path in self.path.rglob(f'*{ext}'):
                if file_path.is_file():
                    self._images.append(ImageFile(file_path))
        return self._images
    
    def find_duplicates_by_average_hash(self):
        """
        Find duplicates based on average hash.
        """
        self.average_hash_duplicates = []  # Resetting the duplicates list
        self.average_hashes = {}  # Resetting the average hash dictionary

        for image in self.images:
            if image.average_hash in self.average_hashes:
                self.average_hash_duplicates.append(image)
            else:
                self.average_hashes[image.average_hash] = image

        if self.average_hash_duplicates:
            print(f"Found {len(self.md5_hash_duplicates)} duplicated images based on average hash.")

    def find_duplicates_by_md5_hash(self):
        """
        Find duplicates based on MD5 hash.
        """
        self.md5_hash_duplicates = []  # Resetting the duplicates list
        self.md5_hashes = {} # Resetting the MD5 hash dictionary

        for image in self.images:
            if image.md5_hash in self.md5_hashes:
                self.md5_hash_duplicates.append(image)
            else:
                self.md5_hashes[image.md5_hash] = image

        if self.md5_hash_duplicates:
            print(f"Found {len(self.md5_hash_duplicates)} duplicated images based on MD5 hash.")
            
        #     a = input("Do you want to delete these {} Images? Press Y or N:  ".format(len(duplicates)))
        #     space_saved = 0
        #     if(a.strip().lower() == "y"):
        #         for duplicate in duplicates:
        #             space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
        #             os.remove(os.path.join(self.dirname,duplicate))
        #             print("{} Deleted Succesfully!".format(duplicate))
    
        #         print("\n\nYou saved {} mb of Space!".format(round(space_saved/1000000),2))
        #     else:
        #         print("Thank you for Using Duplicate Remover")
        # else:
        #     print("No Duplicates Found :(")