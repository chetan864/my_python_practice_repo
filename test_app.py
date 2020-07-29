import unittest
from app import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1),1)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(1),89)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(1),1346269)

if __name__ == '__main__':
    unittest.main()