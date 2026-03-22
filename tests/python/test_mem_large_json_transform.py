import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "languages/python/mem-large-json-transform/run.sh"
DATASET = ROOT / "benchmarks/datasets/generated/mem-large-json-transform-medium.json"


class TestMemLargeJsonTransformPython(unittest.TestCase):
    def test_transform_returns_valid_json_summary(self):
        result = subprocess.run([str(RUNNER), str(DATASET)], check=True, capture_output=True, text=True)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["total_records"], 50000)
        self.assertEqual(len(payload["categories"]), 20)

    def test_transform_has_expected_bucket_shape(self):
        result = subprocess.run([str(RUNNER), str(DATASET)], check=True, capture_output=True, text=True)
        payload = json.loads(result.stdout)
        sample = payload["categories"]["cat-0"]
        self.assertEqual(set(sample.keys()), {"count", "value_sum", "weight_sum", "active_count"})


if __name__ == "__main__":
    unittest.main()
