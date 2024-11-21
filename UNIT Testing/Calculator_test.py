# Unit Tests for Calculator App

# Run with the following command:
# python3 -m unittest test_calculator.py
# or just press the Run button on the top right!

import unittest
import Calculator

# Unit tests
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(10, 5)
        self.assertEqual(result, 15)
        r = Calculator.divide(10, 5)
        self.assertEqual(r, 2)
        r2 = Calculator.divide(11, 5)
        self.assertEqual(r2,2.2)    
    # Similarly, test the other functions of the Calculator App.
        

# Run the tests
if __name__ == "__main__":
    unittest.main()