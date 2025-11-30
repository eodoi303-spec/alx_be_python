import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Addition tests ---
    def test_add_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)
        self.assertAlmostEqual(self.calc.add(-1.5, 0.5), -1.0)

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    # --- Subtraction tests ---
    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(-1.0, -2.5), 1.5)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # --- Multiplication tests ---
    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiply_floats_and_negatives(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, -2.0), 3.0)

    # --- Division tests ---
    def test_divide_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_divide_result_float(self):
        # check float result and precision
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1.0 / 3.0, places=7)

    def test_divide_negative(self):
        self.assertAlmostEqual(self.calc.divide(-6, 2), -3)
        self.assertAlmostEqual(self.calc.divide(6, -2), -3)
        self.assertAlmostEqual(self.calc.divide(-6, -2), 3)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    # --- Mixed-type tests (int/float) ---
    def test_mixed_types(self):
        self.assertAlmostEqual(self.calc.add(1, 2.5), 3.5)
        self.assertAlmostEqual(self.calc.subtract(5.0, 2), 3.0)
        self.assertAlmostEqual(self.calc.multiply(3, 2.5), 7.5)
        self.assertAlmostEqual(self.calc.divide(5, 2.0), 2.5)

    # --- Optional: sanity / identity checks ---
    def test_commutativity_add(self):
        self.assertEqual(self.calc.add(4, 5), self.calc.add(5, 4))

    def test_non_commutativity_subtract(self):
        self.assertNotEqual(self.calc.subtract(4, 5), self.calc.subtract(5, 4))

if __name__ == "__main__":
    unittest.main()
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.