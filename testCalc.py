import unittest
from calc import calc

# run with python3 command 

class TestCalculator(unittest.TestCase):
    def test_add_pass(self):
        actual = calc.add(1,2)
        expected = 3
        self.assertEqual(actual, expected)
    
    def test_add_fail(self):
        actual = calc.add(1,2)
        expected = -1
        self.assertEqual(actual, expected)

    def test_sub_pass(self):
        actual = calc.sub(1,2)
        expected = -1
        self.assertEqual(actual, expected)
    
    def test_sub_fail(self):
        actual = calc.sub(1,2)
        expected = 10
        self.assertEqual(actual, expected)

    def test_mul_pass(self):
        actual = calc.mul(1,2)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_mul_fail(self):
        actual = calc.mul(1,2)
        expected = -1
        self.assertEqual(actual, expected)

    def test_div_pass(self):
        actual = calc.div(1,2)
        expected = 0.5
        self.assertEqual(actual, expected)
    
    def test_div_fail(self):
        actual = calc.div(1,2)
        expected = 1
        self.assertEqual(actual, expected)
    

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calc.add("a","b")
            calc.sub("a","b")
            calc.mul("a","b")
            calc.div("a","b")





if __name__ == '__main__':
    unittest.main()