import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNERS = {
    "python": ROOT / "languages/python/con-producer-consumer-pipeline/run.sh",
    "typescript": ROOT / "languages/typescript/con-producer-consumer-pipeline/run.sh",
}


def _run(runner, n):
    return json.loads(subprocess.run([str(runner), str(n)], check=True, capture_output=True, text=True).stdout)


def expected_sum(n: int) -> int:
    return sum(((i * 3 + 7) % 1000) for i in range(n))


class TestConcurrencyPipeline(unittest.TestCase):
    def test_cross_language_consistency(self):
        outputs = {lang: _run(runner, 1000) for lang, runner in RUNNERS.items()}
        canonical = json.dumps(outputs["python"], sort_keys=True)
        for lang, payload in outputs.items():
            self.assertEqual(json.dumps(payload, sort_keys=True), canonical, lang)

    def test_expected_aggregate(self):
        payload = _run(RUNNERS["python"], 1000)
        self.assertEqual(payload["item_count"], 1000)
        self.assertEqual(payload["value_sum"], expected_sum(1000))


if __name__ == "__main__":
    unittest.main()
