from abc import ABC, abstractmethod

class StorageService(ABC):
    @abstractmethod
    def upload_file(self, file, object_key: str) -> str:
        """Uploads the file and returns the public URL"""
        pass
