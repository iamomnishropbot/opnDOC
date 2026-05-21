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
            self.assertIn("user_profile", captured_payload)
            self.assertIn("style_guidance", captured_payload)
            self.assertEqual(captured_payload["user_profile"]["casing_style"], "lowercase")
            self.assertTrue(controller.memory["history_log"])
            self.assertIsInstance(controller.memory["history_log"][-1], str)
            self.assertIn("style=", controller.memory["history_log"][-1])
            self.assertEqual(controller.memory["user_profile"]["interaction_count"], "1")

            with open(storage_path, "r", encoding="utf-8") as f:
                saved = json.load(f)
            self.assertIsInstance(saved["history_log"][-1], str)

    def test_process_prompt_applies_learned_style_to_response(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            storage_path = Path(tmpdir) / "brain.json"
            controller = RealAILocalController(storage_path=str(storage_path))

            def backend(_payload):
                return "OK"

            result = controller.process_prompt("yo!!!", backend)

            self.assertEqual(result, "ok!")
            self.assertEqual(controller.memory["user_profile"]["punctuation_style"], "exclamatory")
            self.assertEqual(controller.memory["user_profile"]["casing_style"], "lowercase")


if __name__ == "__main__":
    unittest.main()
