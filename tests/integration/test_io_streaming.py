import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / 'benchmarks/datasets/generated/io-large-file-streaming-medium.txt'
RUNNERS = {
    'python': ROOT / 'languages/python/io-large-file-streaming/run.sh',
    'typescript': ROOT / 'languages/typescript/io-large-file-streaming/run.sh',
    'go': ROOT / 'languages/go/io-large-file-streaming/run.sh',
    'rust': ROOT / 'languages/rust/io-large-file-streaming/run.sh',
    'java': ROOT / 'languages/java/io-large-file-streaming/run.sh',
    'csharp': ROOT / 'languages/csharp/io-large-file-streaming/run.sh',
}


def _run(runner):
    return json.loads(subprocess.run([str(runner), str(DATASET)], check=True, capture_output=True, text=True).stdout)


class TestIoStreaming(unittest.TestCase):
    def test_cross_language_consistency(self):
        results = {lang: _run(r) for lang, r in RUNNERS.items()}
        canonical = json.dumps(results['python'], sort_keys=True)
        for lang, payload in results.items():
            self.assertEqual(json.dumps(payload, sort_keys=True), canonical, lang)

    def test_expected_shape(self):
        payload = _run(RUNNERS['python'])
        self.assertEqual(payload['total_records'], 200000)
        self.assertEqual(len(payload['categories']), 20)


if __name__ == '__main__':
    unittest.main()
