import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNERS = {
    'python': ROOT / 'languages/python/par-parallel-reduction/run.sh',
    'typescript': ROOT / 'languages/typescript/par-parallel-reduction/run.sh',
    'go': ROOT / 'languages/go/par-parallel-reduction/run.sh',
    'rust': ROOT / 'languages/rust/par-parallel-reduction/run.sh',
    'java': ROOT / 'languages/java/par-parallel-reduction/run.sh',
    'csharp': ROOT / 'languages/csharp/par-parallel-reduction/run.sh',
}

def _run(runner, n=2000):
    return json.loads(subprocess.run([str(runner), str(n)], check=True, capture_output=True, text=True).stdout)

def expected_sum(n):
    return sum(((i * 7 + 11) % 1000) for i in range(n))

class TestParallelReduction(unittest.TestCase):
    def test_cross_language_consistency(self):
        results = {lang: _run(r) for lang, r in RUNNERS.items()}
        canonical = json.dumps(results['python'], sort_keys=True)
        for lang, payload in results.items():
            self.assertEqual(json.dumps(payload, sort_keys=True), canonical, lang)

    def test_expected_aggregate(self):
        payload = _run(RUNNERS['python'])
        self.assertEqual(payload['item_count'], 2000)
        self.assertEqual(payload['value_sum'], expected_sum(2000))

if __name__ == '__main__':
    unittest.main()
