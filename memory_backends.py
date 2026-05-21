from copy import deepcopy


DEFAULT_BRAIN_DATA = {"word_fix": {}, "history_log": [], "user_profile": {}}


def normalize_brain_data(data):
    """
    Normalize to the cross-language schema used by Rust/Kotlin:
    - word_fix: dict[str, str]
    - history_log: list[str]
    - user_profile: dict[str, str]
    """
    if not isinstance(data, dict):
        data = {}

    normalized = deepcopy(DEFAULT_BRAIN_DATA)

    word_fix = data.get("word_fix", {})
    if isinstance(word_fix, dict):
        normalized["word_fix"] = {str(k): str(v) for k, v in word_fix.items()}

    user_profile = data.get("user_profile", {})
    if isinstance(user_profile, dict):
        normalized["user_profile"] = {str(k): str(v) for k, v in user_profile.items()}

    history_log = data.get("history_log", [])
    if isinstance(history_log, list):
        normalized["history_log"] = [_history_entry_to_string(entry) for entry in history_log]

    return normalized


def _history_entry_to_string(entry):
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        timestamp = str(entry.get("timestamp", "")).strip()
        user = str(entry.get("user", "")).strip()
        response = str(entry.get("response", "")).strip()
        prefix = f"[{timestamp}] " if timestamp else ""
        if user and response:
            return f"{prefix}user={user} | response={response}"
        if user:
            return f"{prefix}user={user}"
        if response:
            return f"{prefix}response={response}"
        if timestamp:
            return f"[{timestamp}]"
        return "history_entry"
    return str(entry)


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
                return normalize_brain_data(json.load(f))
        return deepcopy(DEFAULT_BRAIN_DATA)

    def save(self, data):
        import json
        with open(self.file_path, 'w') as f:
            json.dump(normalize_brain_data(data), f, indent=4)

class InMemoryStorageBackend(MemoryStorageBackend):
    """
    Pure in-memory backend (for WASM, testing, or web/mobile sandboxes).
    """
    def __init__(self):
        self._data = deepcopy(DEFAULT_BRAIN_DATA)

    def load(self):
        return normalize_brain_data(self._data)

    def save(self, data):
        self._data = normalize_brain_data(data)
