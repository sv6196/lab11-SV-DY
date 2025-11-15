import unittest
from calculator import *

#https://github.com/sv6196/lab11-SV-DY.git
#Partner 1: Sean Vong
#Partner 2: Daniel Yoffe

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions


        self.assertEqual(mul(3,3), 9)
        self.assertEqual(mul(1,4), 4)
        self.assertEqual(mul(6,7), 42)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 3), 1)
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(49, 7), 7)

    # def test_divide(self): # 3 assertions
    #     fill in code
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(math.e, math.e ** 2), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # invalid base
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(math.e, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse( 8,6), 10)
        self.assertAlmostEqual(hypotenuse( 3,4), 16)
        self.assertAlmostEqual(hypotenuse( 5,12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-321)
        with self.assertRaises(ValueError):
            square_root(-0.232)

    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()