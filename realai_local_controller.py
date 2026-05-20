import os
import json
import gzip
import tempfile
from datetime import datetime
from typing import Any, Callable

class RealAILocalController:
    """
    Fuses local pattern matching, stateful memory logs, and 
    lexical overrides inspired by the RealAI architecture.
    """
    def __init__(self, storage_path="realai_brain.json"):
        self.storage_path = storage_path
        self.memory = self.load_local_brain()

    @staticmethod
    def _default_memory():
        return {"word_fix": {}, "history_log": [], "user_profile": {}}

    @staticmethod
    def _emit_thought(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[94m[thought_log - {timestamp}] {message}\033[0m")

    @staticmethod
    def _is_gzip_path(path):
        return str(path).endswith(".gz")

    def _normalize_memory(self, memory_obj):
        if not isinstance(memory_obj, dict):
            return self._default_memory()

        normalized = self._default_memory()
        if isinstance(memory_obj.get("word_fix"), dict):
            normalized["word_fix"] = memory_obj["word_fix"]
        if isinstance(memory_obj.get("history_log"), list):
            normalized["history_log"] = memory_obj["history_log"]
        if isinstance(memory_obj.get("user_profile"), dict):
            normalized["user_profile"] = memory_obj["user_profile"]
        return normalized

    def _read_storage(self):
        if self._is_gzip_path(self.storage_path):
            with gzip.open(self.storage_path, "rt", encoding="utf-8") as f:
                return f.read()
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return f.read()

    def _write_storage_atomically(self, content):
        storage_dir = os.path.dirname(os.path.abspath(self.storage_path)) or "."
        fd, tmp_path = tempfile.mkstemp(prefix=".realai_brain_", dir=storage_dir)
        os.close(fd)
        try:
            if self._is_gzip_path(self.storage_path):
                with gzip.open(tmp_path, "wt", encoding="utf-8") as f:
                    f.write(content)
            else:
                with open(tmp_path, "w", encoding="utf-8") as f:
                    f.write(content)
            os.replace(tmp_path, self.storage_path)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        
    def load_local_brain(self):
        if os.path.exists(self.storage_path):
            try:
                loaded = json.loads(self._read_storage())
                return self._normalize_memory(loaded)
            except (OSError, json.JSONDecodeError):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                corrupt_backup = f"{self.storage_path}.corrupt.{timestamp}"
                try:
                    os.replace(self.storage_path, corrupt_backup)
                    self._emit_thought(f"Corrupted local brain moved to backup: {corrupt_backup}")
                except OSError:
                    self._emit_thought("Corrupted local brain detected; backup move failed.")
        # Default state template if no local file exists
        return self._default_memory()

    def save_local_brain(self):
        serializable_memory = self._normalize_memory(self.memory)
        content = json.dumps(serializable_memory, indent=4, ensure_ascii=False)
        self._write_storage_atomically(content)

    def log_thought(self, message):
        """Replicates the classic RealAI thought_log visibility"""
        self._emit_thought(message)

    def apply_word_fix(self, raw_input):
        """Locally intercepts text to apply custom user vocabulary rules"""
        processed_text = raw_input
        for wrong_word, corrected_word in self.memory["word_fix"].items():
            if wrong_word in processed_text:
                self.log_thought(f"WordFix Match Found: Replacing '{wrong_word}' with '{corrected_word}'")
                processed_text = processed_text.replace(wrong_word, corrected_word)
        return processed_text

    def process_prompt(self, raw_prompt, generation_backend_callback):
        if not callable(generation_backend_callback):
            raise TypeError("generation_backend_callback must be callable")

        self.log_thought("Initializing local lexical validation pass...")
        clean_prompt = self.apply_word_fix(raw_prompt)
        
        # Injecting local conversation history context right into the pipeline
        self.log_thought("Injecting localized memory logs into execution context.")
        contextual_payload = {
            "local_history": self.memory["history_log"][-5:], # Grab last 5 iterations
            "current_prompt": clean_prompt
        }
        
        self.log_thought("Dispatching execution payload to generation engine...")
        # Execute the modern generative generation step via the callback loop
        try:
            response = generation_backend_callback(contextual_payload)
        except Exception as exc:
            self.log_thought(f"Generation backend failed: {exc}")
            raise
        
        # Committing the entire exchange back to local disk space natively
        self.log_thought("Generation successful. Appending token metrics to local memory storage.")
        response_for_storage = response
        try:
            json.dumps(response_for_storage)
        except TypeError:
            response_for_storage = str(response_for_storage)
        self.memory["history_log"].append({
            "user": clean_prompt, 
            "response": response_for_storage,
            "timestamp": datetime.now().isoformat()
        })
        self.save_local_brain()
        
        return response


if __name__ == "__main__":
    controller = RealAILocalController()

    def demo_backend(payload: dict[str, Any]):
        return f"quantum-stable-response::{payload['current_prompt']}"

    prompt = os.environ.get("OPNDOC_PROMPT", "quantum stability check")
    print(controller.process_prompt(prompt, demo_backend))
