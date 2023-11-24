from PIL import Image
import imagehash
import hashlib
from pathlib import Path

class ImageFile:
    """
    Class representing an individual image file, with hash calculation.
    """
    def __init__(self, base_path, file_path, hash_size=20):
        
        self.file_path = Path(file_path)
        self.base_path = Path(base_path)
        self.relative_path = self.file_path.relative_to(self.base_path)

        self._average_hash = None  # Private attribute to store the average hash
        self._md5_hash = None  # Private attribute to store the MD5 hash
        self._average_hash_size = hash_size

    @property
    def md5_hash(self):
        """
        Property to get the hash of the image. 
        Calculate the hash only if it hasn't been calculated yet.
        """
        if self._md5_hash is None:
            self._md5_hash = self.calculate_average_hash()
        return self._md5_hash
    
    @property
    def average_hash(self):
        """
        Property to get the hash of the image. 
        Calculate the hash only if it hasn't been calculated yet.
        """
        if self._average_hash is None:
            self._average_hash = self.calculate_average_hash()
        return self._average_hash

    def calculate_average_hash(self):
        """
        Calculate the hash of the image file.
        """
        with Image.open(self.file_path) as img:
            return imagehash.average_hash(img, self._average_hash_size)

    def calculate_md5(self):
        hash_md5 = hashlib.md5()
        with open(self.file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def __repr__(self):
        return f"ImageFile({self.file_path}, Average Hash: {self.average_hash})"