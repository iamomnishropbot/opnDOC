import unittest

from memory_backends import normalize_brain_data, InMemoryStorageBackend


class MemoryBackendNormalizationTests(unittest.TestCase):
    def test_normalize_converts_history_dict_entries_to_strings(self):
        normalized = normalize_brain_data(
            {
                "word_fix": {"teh": "the"},
                "history_log": [{"user": "hello", "response": "hi"}, 42],
                "user_profile": {"name": "Omni"},
            }
        )

        self.assertEqual(normalized["word_fix"], {"teh": "the"})
        self.assertEqual(normalized["user_profile"], {"name": "Omni"})
        self.assertEqual(normalized["history_log"], ["user=hello | response=hi", "42"])

    def test_inmemory_backend_always_returns_normalized_schema(self):
        backend = InMemoryStorageBackend()
        backend.save({"history_log": [{"response": "ok"}]})

        loaded = backend.load()

        self.assertEqual(loaded["word_fix"], {})
        self.assertEqual(loaded["user_profile"], {})
        self.assertEqual(loaded["history_log"], ["response=ok"])


if __name__ == "__main__":
    unittest.main()
