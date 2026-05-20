import os
import json
from datetime import datetime

class RealAILocalController:
    """
    Fuses local pattern matching, stateful memory logs, and 
    lexical overrides inspired by the RealAI architecture.
    """
    def __init__(self, storage_path="realai_brain.json"):
        self.storage_path = storage_path
        self.memory = self.load_local_brain()
        
    def load_local_brain(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        # Default state template if no local file exists
        return {"word_fix": {}, "history_log": [], "user_profile": {}}

    def save_local_brain(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def log_thought(self, message):
        """Replicates the classic RealAI thought_log visibility"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[94m[thought_log - {timestamp}] {message}\033[0m")

    def apply_word_fix(self, raw_input):
        """Locally intercepts text to apply custom user vocabulary rules"""
        processed_text = raw_input
        for wrong_word, corrected_word in self.memory["word_fix"].items():
            if wrong_word in processed_text:
                self.log_thought(f"WordFix Match Found: Replacing '{wrong_word}' with '{corrected_word}'")
                processed_text = processed_text.replace(wrong_word, corrected_word)
        return processed_text

    def process_prompt(self, raw_prompt, generation_backend_callback):
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
        response = generation_backend_callback(contextual_payload)
        
        # Committing the entire exchange back to local disk space natively
        self.log_thought("Generation successful. Appending token metrics to local memory storage.")
        self.memory["history_log"].append({
            "user": clean_prompt, 
            "response": response, 
            "timestamp": datetime.now().isoformat()
        })
        self.save_local_brain()
        
        return response
