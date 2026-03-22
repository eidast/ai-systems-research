import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "benchmarks/datasets/generated/mem-large-json-transform-medium.json"

CPU_RUNNERS = {
    "python": ROOT / "languages/python/cpu-prime-count/run.sh",
    "typescript": ROOT / "languages/typescript/cpu-prime-count/run.sh",
    "go": ROOT / "languages/go/cpu-prime-count/run.sh",
    "rust": ROOT / "languages/rust/cpu-prime-count/run.sh",
    "java": ROOT / "languages/java/cpu-prime-count/run.sh",
    "csharp": ROOT / "languages/csharp/cpu-prime-count/run.sh",
}

MEM_RUNNERS = {
    "python": ROOT / "languages/python/mem-large-json-transform/run.sh",
    "typescript": ROOT / "languages/typescript/mem-large-json-transform/run.sh",
    "go": ROOT / "languages/go/mem-large-json-transform/run.sh",
    "rust": ROOT / "languages/rust/mem-large-json-transform/run.sh",
    "java": ROOT / "languages/java/mem-large-json-transform/run.sh",
    "csharp": ROOT / "languages/csharp/mem-large-json-transform/run.sh",
}


def _run(cmd):
    return subprocess.run([str(cmd[0]), *map(str, cmd[1:])], check=True, capture_output=True, text=True).stdout.strip()


class TestCrossLanguageConsistency(unittest.TestCase):
    def test_cpu_prime_count_cross_language_consistency(self):
        results = {lang: _run((runner, 1000)) for lang, runner in CPU_RUNNERS.items()}
        self.assertEqual(len(set(results.values())), 1, results)
        self.assertEqual(next(iter(results.values())), "168")

    def test_mem_transform_cross_language_consistency(self):
        results = {lang: json.loads(_run((runner, DATASET))) for lang, runner in MEM_RUNNERS.items()}
        canonical = json.dumps(results["python"], sort_keys=True)
        for lang, payload in results.items():
            self.assertEqual(json.dumps(payload, sort_keys=True), canonical, lang)


if __name__ == "__main__":
    unittest.main()
