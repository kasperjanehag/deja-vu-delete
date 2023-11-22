from abc import ABC, abstractmethod
from pathlib import Path


class FileHandler(ABC):
    """
    Abstract base class for file handling.
    """
    def __init__(self, path):
        self.path = Path(path)
        self.files = []
        self.image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}

    @abstractmethod
    def list_files(self):
        """
        Abstract method to list files.
        """
        pass

class ImageFileHandler(FileHandler):
    """
    Handles image files, inheriting from FileHandler.
    """

    def list_files(self):
        """
        List all image files in the instance's directory recursively.
        """
        if not self.path.is_dir():
            raise ValueError(f"{self.path} is not a valid directory.")

        self.files = []  # Reset the list
        for ext in self.image_extensions:
            for file in self.path.rglob(f'*{ext}'):
                if file.is_file():
                    self.files.append(file)
