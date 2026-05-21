import json
import tempfile
import unittest
from pathlib import Path

from realai_local_controller import RealAILocalController


class RealAILocalControllerTests(unittest.TestCase):
    def test_process_prompt_keeps_history_log_as_strings(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            storage_path = Path(tmpdir) / "brain.json"
            controller = RealAILocalController(storage_path=str(storage_path))
            controller.memory["word_fix"] = {"teh": "the"}

            captured_payload = {}

            def backend(payload):
                captured_payload.update(payload)
                return "ok"

            result = controller.process_prompt("teh prompt", backend)

            self.assertEqual(result, "ok")
            self.assertEqual(captured_payload["current_prompt"], "the prompt")
            self.assertTrue(controller.memory["history_log"])
            self.assertIsInstance(controller.memory["history_log"][-1], str)

            with open(storage_path, "r", encoding="utf-8") as f:
                saved = json.load(f)
            self.assertIsInstance(saved["history_log"][-1], str)


if __name__ == "__main__":
    unittest.main()
