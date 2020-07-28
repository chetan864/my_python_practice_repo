import unittest
from hundred_percent_test_coverage_in_python.app import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)

if __name__ == '__main__':
    unittest.main()