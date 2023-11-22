from PIL import Image
import imagehash

class ImageFile:
    """
    Class representing an individual image file, with hash calculation.
    """
    def __init__(self, file_path, hash_size=20):
        self.file_path = file_path
        self._average_hash = None  # Private attribute to store the hash
        self._average_hash_size = hash_size

    @property
    def average_hash(self):
        """
        Property to get the hash of the image. 
        Calculate the hash only if it hasn't been calculated yet.
        """
        if self._average_hash is None:
            self._average_hash = self.calculate_hash()
        return self._average_hash

    def calculate_hash(self):
        """
        Calculate the hash of the image file.
        """
        with Image.open(self.file_path) as img:
            return imagehash.average_hash(img, self._average_hash_size)

    def __repr__(self):
        return f"ImageFile({self.file_path}, Average Hash: {self.average_hash})"