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
        self._files = []
        self.image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}

    @property
    @abstractmethod
    def files(self) -> list[ImageFile]:
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
    def files(self) -> list[ImageFile]:
        """
        Property to get a list of ImageFile instances representing the image files 
        in the instance's directory, done recursively.

        Returns:
            List[ImageFile]: A list of ImageFile instances.

        Raises:
            ValueError: If the specified path is not a valid directory.
        """
        if not self.path.is_dir():
            raise ValueError(f"{self.path} is not a valid directory.")

        self._files = []  # Reset the list
        for ext in self.image_extensions:
            for file_path in self.path.rglob(f'*{ext}'):
                if file_path.is_file():
                    self._files.append(ImageFile(file_path))
        return self._files