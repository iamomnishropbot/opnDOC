import os
import json
from datetime import datetime
from copy import deepcopy
from memory_backends import normalize_brain_data, DEFAULT_BRAIN_DATA

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
                return normalize_brain_data(json.load(f))
        return deepcopy(DEFAULT_BRAIN_DATA)

    def save_local_brain(self):
        with open(self.storage_path, 'w') as f:
            json.dump(normalize_brain_data(self.memory), f, indent=4)

    def log_thought(self, message):
        """Replicates the classic RealAI thought_log visibility"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[94m[thought_log - {timestamp}] {message}\033[0m")

    def apply_word_fix(self, raw_input):
        """Locally intercepts text to apply custom user vocabulary rules"""
        processed_text = raw_input
        for wrong_word, corrected_word in self.memory.get("word_fix", {}).items():
            if wrong_word in processed_text:
                self.log_thought(f"WordFix Match Found: Replacing '{wrong_word}' with '{corrected_word}'")
                processed_text = processed_text.replace(wrong_word, corrected_word)
        return processed_text

    def _update_user_profile_from_prompt(self, prompt):
        profile = self.memory.setdefault("user_profile", {})
        interaction_count = int(profile.get("interaction_count", "0")) + 1
        prompt_words = prompt.split()
        prompt_word_count = len(prompt_words)
        prompt_char_count = len(prompt)

        prev_avg_words = float(profile.get("avg_prompt_words", "0"))
        prev_avg_chars = float(profile.get("avg_prompt_chars", "0"))
        avg_prompt_words = ((prev_avg_words * (interaction_count - 1)) + prompt_word_count) / interaction_count
        avg_prompt_chars = ((prev_avg_chars * (interaction_count - 1)) + prompt_char_count) / interaction_count

        letter_count = sum(1 for c in prompt if c.isalpha())
        lower_count = sum(1 for c in prompt if c.islower())
        upper_count = sum(1 for c in prompt if c.isupper())
        if letter_count and lower_count / letter_count >= 0.8:
            casing_style = "lowercase"
        elif letter_count and upper_count / letter_count >= 0.8:
            casing_style = "uppercase"
        else:
            casing_style = "mixed"

        exclamation_count = prompt.count("!")
        question_count = prompt.count("?")
        if exclamation_count > question_count:
            punctuation_style = "exclamatory"
        elif question_count > exclamation_count:
            punctuation_style = "questioning"
        else:
            punctuation_style = "neutral"

        if avg_prompt_words <= 8:
            verbosity_style = "concise"
        elif avg_prompt_words >= 24:
            verbosity_style = "detailed"
        else:
            verbosity_style = "balanced"

        profile.update(
            {
                "interaction_count": str(interaction_count),
                "avg_prompt_words": f"{avg_prompt_words:.2f}",
                "avg_prompt_chars": f"{avg_prompt_chars:.2f}",
                "casing_style": casing_style,
                "punctuation_style": punctuation_style,
                "verbosity_style": verbosity_style,
                "last_user_prompt": prompt,
            }
        )
        self.memory["user_profile"] = profile

    def _build_style_guidance(self):
        profile = self.memory.get("user_profile", {})
        return (
            "Adapt response style to user profile: "
            f"verbosity={profile.get('verbosity_style', 'balanced')}, "
            f"casing={profile.get('casing_style', 'mixed')}, "
            f"punctuation={profile.get('punctuation_style', 'neutral')}."
        )

    def _align_response_to_user_style(self, response):
        profile = self.memory.get("user_profile", {})
        styled_response = str(response)

        if profile.get("verbosity_style") == "concise" and len(styled_response.split()) > 35:
            styled_response = " ".join(styled_response.split()[:35]) + "..."

        if profile.get("casing_style") == "lowercase":
            styled_response = styled_response.lower()
        elif profile.get("casing_style") == "uppercase":
            styled_response = styled_response.upper()

        punctuation_style = profile.get("punctuation_style")
        if punctuation_style == "exclamatory" and styled_response and styled_response[-1] not in ".!?":
            styled_response += "!"
        elif punctuation_style == "questioning" and styled_response and styled_response[-1] not in ".!?":
            styled_response += "?"

        return styled_response

    def process_prompt(self, raw_prompt, generation_backend_callback):
        self.log_thought("Initializing local lexical validation pass...")
        clean_prompt = self.apply_word_fix(raw_prompt)
        self._update_user_profile_from_prompt(clean_prompt)
        
        # Injecting local conversation history context right into the pipeline
        self.log_thought("Injecting localized memory logs into execution context.")
        contextual_payload = {
            "local_history": self.memory.get("history_log", [])[-5:], # Grab last 5 iterations
            "current_prompt": clean_prompt,
            "user_profile": dict(self.memory.get("user_profile", {})),
            "style_guidance": self._build_style_guidance(),
        }
        
        self.log_thought("Dispatching execution payload to generation engine...")
        # Execute the modern generative generation step via the callback loop
        response = generation_backend_callback(contextual_payload)
        styled_response = self._align_response_to_user_style(response)
        
        # Committing the entire exchange back to local disk space natively
        self.log_thought("Generation successful. Appending token metrics to local memory storage.")
        self.memory.setdefault("user_profile", {})["last_agent_response"] = styled_response
        timestamp = datetime.now().isoformat()
        profile = self.memory.get("user_profile", {})
        history_entry = (
            f"[{timestamp}] user={clean_prompt} | response={styled_response} "
            f"| style={profile.get('verbosity_style', 'balanced')}/"
            f"{profile.get('casing_style', 'mixed')}/"
            f"{profile.get('punctuation_style', 'neutral')}"
        )
        self.memory.setdefault("history_log", []).append(history_entry)
        self.memory = normalize_brain_data(self.memory)
        self.save_local_brain()
        
        return styled_response
