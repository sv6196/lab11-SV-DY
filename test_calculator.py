import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-3, -2), -1)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions

<<<<<<< HEAD
        self.assertEqual(multiply(3,3), 9)
        self.assertEqual(multiply(1,4), 4)
        self.assertEqual(multiply(6,7), 42)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(3, 3), 1)
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(49, 7), 7)
=======
    # def test_divide(self): # 3 assertions
    #     fill in code
    ##########################
>>>>>>> a825d04fa0ac9506087e747cd7e5da261a273bcf

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(math.e, math.e ** 2), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)  # invalid base
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