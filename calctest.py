# https://github.com/Jsloy/lab11-EB-JS/tree/main
# Partner 1: Ethan Bond
# Partner 2: Jason Samim

import unittest
import math
from calculator import add, subtract, multiply, divide, logarithm, exponent, square_root, hypotenuse

class TestCalculator(unittest.TestCase):
    
    # Partner 2 Unit Tests
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 5)

    # Partner 1 Unit Tests
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)

if __name__ == '__main__':
    unittest.main()
