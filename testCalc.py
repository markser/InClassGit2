import unittest
from calc import calc

# def calcTwoPositiveNumbers(a,b):
#     return calc(a,b)

# def calcTwoNegativeNumbers(a,b):
#     return calc(a,b)

# def calcTwoZeroNumbers(a,b):
#     checker = True
#     try:
#         calc(a,b)
#     except ZeroDivisionError:
#         checker = False
#     return checker

class TestCalculator(unittest.TestCase):
    def test_two_pos(self):
        actual = calc(1,2)
        expected = [3, -1, 2, 0]
        self.assertEqual(actual, expected)
    
    def test_two_neg(self):
        actual = calc(-8,-1)
        expected = [-9, -7, 8, 8]
        self.assertEqual(actual, expected)

    def test_two_zero(self):
        # with self.assertRaises(ZeroDivisionError):
            calc(0,0)

    def test_invalid_input(self):
        # with self.assertRaises(TypeError):
            calc("a","b")

    def test_two_pos_fail(self):
        actual = calc(1,2)
        expected = [3, -1, 2, 1]
        self.assertEqual(actual, expected)
    
    def test_two_neg_fail(self):
        actual = calc(-8,-1)
        expected = [-9, -7, 2, 8]
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()