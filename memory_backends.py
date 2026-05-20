class MemoryStorageBackend:
    """
    An abstract backend interface for managing persistent memory state.
    Subclass this for platform-specific storage (e.g., in-memory, file, browser, mobile, etc.).
    """
    def load(self):
        raise NotImplementedError("Subclasses must implement load()")

    def save(self, data):
        raise NotImplementedError("Subclasses must implement save(data)")

class FileStorageBackend(MemoryStorageBackend):
    """
    Concrete backend using local JSON file storage (for CLI/dev environments).
    """
    def __init__(self, file_path="realai_brain.json"):
        self.file_path = file_path

    def load(self):
        import os, json
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {"word_fix": {}, "history_log": [], "user_profile": {}}

    def save(self, data):
        import json
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

class InMemoryStorageBackend(MemoryStorageBackend):
    """
    Pure in-memory backend (for WASM, testing, or web/mobile sandboxes).
    """
    def __init__(self):
        self._data = {"word_fix": {}, "history_log": [], "user_profile": {}}

    def load(self):
        return self._data.copy()

    def save(self, data):
        self._data = data.copy()
