import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self): # Testing add function
        result = calc.add(10, 5), calc.add(-1, -1), calc.add(1, -1), calc.add(10.2, 9.8)
        self.assertEqual(result[0], 15)
        self.assertEqual(result[1], -2)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 20)

    def test_subtract(self): # Testing subtract function
        result = calc.subtract(5, 3), calc.subtract(-1, -1), calc.subtract(0, 0), calc.subtract(10, 9.8)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0.1999999999999993)
    
    def test_divide(self): # Testing multiply function
        result = calc.divide(9, 3), calc.divide(-1, -1), calc.divide(0.6, 2)
        self.assertEqual(result[0], 3)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 0.3)
    
        with self.assertRaises(ValueError):
            calc.divide(0,0)
    
    def test_multiply(self):  # Testing divide function
        result = calc.multiply(5, 3), calc.multiply(-1, -1), calc.multiply(0, 0), calc.multiply(10, 9.8)
        self.assertEqual(result[0], 15)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 98)


if __name__ == '__main__':
    unittest.main()