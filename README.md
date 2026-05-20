> **opnDOC** is a high-speed, scriptable command-line interface (CLI) that enables native interaction with an agentic AI backend directly from your terminal. Built for workflows where browser-based GUIs cause unnecessary friction, openDOC processes structured arguments, tracks internal states natively, and outputs perfectly compiled technical and narrative documentation files.

---

## 1. Project Overview

### The Problem

Modern AI tools heavily rely on browser windows or heavy graphical interfaces. For engineers, researchers, and developers operating in terminal-centric environments, constantly context-switching and copy-pasting text streams breaks focus, introduces formatting bugs, and makes AI tools impossible to integrate into repeatable shell scripts.

### The Solution

**openDOC** provides an optimized, scriptable terminal executable. It acts as an isolated entry point to a localized multi-agent network, executing complex documentation compilation tasks natively, tracking local token states, and outputting structured Markdown assets directly to disk.

---

## 2. Core Pillars & Architecture

Project openDOC is engineered around three major structural deliverables, backed by a stateful local execution module:

1. **Prompt & Tag Interface:** A robust terminal subsystem designed to parse advanced arguments, handle POSIX-compliant flags, and enforce interface input contracts.
2. **APA 7 Narrative Engine:** A localized multi-agent algorithmic module responsible for compiling raw text blocks and executing rigorous academic APA 7th edition citation and pacing validation rules.
3. **Document Builder Output:** A file generation pipeline that translates backend token outputs into error-free, localized, structured Markdown structures.

### 🧠 The RealAI Brain Fusion Layer

To ensure complete system transparency and user control, openDOC integrates a module-based state controller inspired by legacy local NLP mechanics (`realai_local_controller`):

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

### Installation (Development Setup)

Clone the repository and prepare your local environment hooks:

```bash
git clone https://github.com/iamomnishropbot/openDOC.git
cd openDOC
pip install -r requirements.txt

```

### Initial Execution

To view configuration guidelines, query parameters, and system inputs:

```bash
python opendoc.py --help

```

### Running a Documentation Pass

Execute a structured prompt and stream the automated compilation process with verbose thought logging active:

```bash
python opendoc.py --format APA7 --input "draft_notes.txt" --output "academic_manifesto.md" --verbose

```

### Managing Local Lexical Fixes

Train your local engine profile directly from the terminal to override backend token parsing rules:

```bash
# Add a persistent string substitution rule
python opendoc_cli.py add "teh" "the"

# List all current localized dictionary rules
python opendoc_cli.py list

```

---

## 5. Success Criteria

The development lifecycle of openDOC v1.0.0 will be validated against three simple, definitive benchmarks:

* **Atomic Triggering:** Execution of a single CLI command triggers the agent backend and prints or saves valid text streams seamlessly without manual copying.
* **Formatting Compliance:** The engine consistently generates error-free, completely valid Markdown files conforming strictly to programmatic structural guidelines.
* **System Cleanliness:** The application exits with standard POSIX system codes (`0` for success, non-zero for handled execution failures), making it fully reliable for pipeline automation.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
