# opnDoc

> **opnDoc** is a high-speed, scriptable command-line interface (CLI) that enables native interaction with an agentic AI backend directly from your terminal. Built for workflows where browser-based GUIs cause unnecessary friction, opnDoc processes structured arguments, tracks internal states natively, and outputs perfectly compiled technical and narrative documentation files.

---

## 1. Project Overview

### The Problem
Modern AI tools heavily rely on browser windows or heavy graphical interfaces. For engineers, researchers, and developers operating in terminal-centric environments, constantly context-switching and copy-pasting text streams breaks focus, introduces formatting bugs, and makes AI tools impossible to integrate into repeatable shell scripts.

### The Solution
**opnDoc** provides an optimized, scriptable terminal executable. It acts as an isolated entry point to a localized multi-agent network, executing complex documentation compilation tasks natively, tracking local token states, and outputting structured Markdown assets directly to disk.

---

## 2. Core Pillars & Architecture

Project opnDoc is engineered around three major structural deliverables, backed by a stateful local execution module:

1. **Prompt & Tag Interface:** A robust terminal subsystem designed to parse advanced arguments, handle POSIX-compliant flags, and enforce interface input contracts.
2. **APA 7 Narrative Engine:** A localized multi-agent algorithmic module responsible for compiling raw text blocks and executing rigorous academic APA 7th edition citation and pacing validation rules.
3. **Document Builder Output:** A file generation pipeline that translates backend token outputs into error-free, localized, structured Markdown structures.

### 🧠 The RealAI Brain Fusion Layer
To ensure complete system transparency and user control, opnDoc integrates a module-based state controller inspired by legacy local NLP mechanics (`realai_local_controller`):

* **Stateful Local Memory:** Conversation logs, execution history, and style profiles are saved locally on disk in a structured JSON matrix (`realai_brain.json`).
* **The Transparent `thought_log`:** The CLI exposes verbose processing diagnostics in real time, streaming internal rule-matching and logic states directly to the console before printing output.
* **Overriding Lexicon Control (`word_fix`):** Users can explicitly train the local brain to intercept and replace custom text strings or structural parameters, strictly overriding the backend models on future runs.

---

## 3. High-Level Schedule & Target Baseline

The core development cycle operates on a high-focus **21-day critical path timeline** starting Monday, May 25, 2026:

| ID | Milestone | Depends On | Duration | Start Date | End Date | Critical Path? |
| --- | --- | --- | --- | --- | --- | --- |
| **M1** | CLI Architecture & Argument Contract Approved | — | 4 Days | 2026-05-25 | 2026-05-28 | **Yes** |
| **M2** | First End-to-End Local Generation of Markdown | M1 | 12 Days | 2026-05-29 | 2026-06-09 | **Yes** |
| **M3** | CLI v1.0.0 Executable Packaged for Distribution | M2 | 5 Days | 2026-06-10 | 2026-06-14 | **Yes** |

> ⚠️ **Active Schedule Compression Protocol:** To mitigate an anticipated 5-day predictive variance on the complex *APA 7 Narrative Engine* module, a compression protocol is integrated into Kickoff Week. Development of the text-parsing elements will run concurrently with initial narrative schema definitions to ensure a final deployment footprint matching the target deadline.

---

## 4. Quick Start & Basic Usage

### Installation & Environment Setup
Clone the repository and prepare your local environment hooks:
```bash
git clone [https://github.com/iamomnishropbot/opnDoc.git](https://github.com/iamomnishropbot/opnDoc.git)
cd opnDoc
pip install -r requirements.txt

```

*Note: Ensure `realai_brain.json` is appended to your local `.gitignore` file to protect local state logs.*

### Interface Help Parameters

To view compilation guidelines, query flags, and subcommand schemas:

```bash
python opndoc.py --help

```

### Running a Documentation Pass

Execute a structured narrative prompt and stream the automated compilation sequence with verbose blue execution logging active:

```bash
python opndoc.py run --format APA7 --input "draft_notes.txt" --output "academic_manifesto.md" --verbose

```

### Managing Local Lexical Fixes

Train your local engine profile directly from the terminal to override backend token parsing rules:

```bash
# Add a persistent string substitution rule
python opndoc.py fix add "teh" "the"

# List all current localized dictionary rules
python opndoc.py fix list

```

---

## 5. Core Architectural Implementation

The following core local state pattern controller maps your custom lexical corrections and manages the transparent `thought_log` outputs natively:

```python
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
        
        self.log_thought("Injecting localized memory logs into execution context.")
        contextual_payload = {
            "local_history": self.memory["history_log"][-5:], 
            "current_prompt": clean_prompt
        }
        
        self.log_thought("Dispatching execution payload to generation engine...")
        response = generation_backend_callback(contextual_payload)
        
        self.log_thought("Generation successful. Appending token metrics to local memory storage.")
        self.memory["history_log"].append({
            "user": clean_prompt, 
            "response": response, 
            "timestamp": datetime.now().isoformat()
        })
        self.save_local_brain()
        
        return response

```

---

## 6. Success Criteria

The development lifecycle of opnDoc v1.0.0 will be validated against three simple, definitive benchmarks:

* **Atomic Triggering:** Execution of a single CLI command triggers the agent backend and prints or saves valid text streams seamlessly without manual copying.
* **Formatting Compliance:** The engine consistently generates error-free, completely valid Markdown files conforming strictly to programmatic structural guidelines.
* **System Cleanliness:** The application exits with standard POSIX system codes (`0` for success, non-zero for handled execution failures), making it fully reliable for pipeline automation.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
