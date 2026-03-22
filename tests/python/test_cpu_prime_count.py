import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[2] / "languages/python/cpu-prime-count/prime_count.py"
spec = importlib.util.spec_from_file_location("prime_count", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestCpuPrimeCount(unittest.TestCase):
    def test_small_known_values(self):
        self.assertEqual(module.count_primes(1), 0)
        self.assertEqual(module.count_primes(2), 1)
        self.assertEqual(module.count_primes(10), 4)
        self.assertEqual(module.count_primes(100), 25)

    def test_monotonic_growth(self):
        self.assertLessEqual(module.count_primes(1000), module.count_primes(2000))

    def test_stability(self):
        self.assertEqual(module.count_primes(300000), module.count_primes(300000))


if __name__ == "__main__":
    unittest.main()
