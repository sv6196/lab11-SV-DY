import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions

        self.assertEqual(multiply(3,3), 9)
        self.assertEqual(multiply(1,4), 4)
        self.assertEqual(multiply(6,7), 42)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(3, 3), 1)
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(49, 7), 7)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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