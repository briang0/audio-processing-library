import unittest

from src.python.main.util import math_util


class TestMathUtil(unittest.TestCase):

    def test_is_power_of_2_1(self):
        expected = False
        val1 = 129
        val2 = 127
        actual1 = math_util.is_power_of_2(val1)
        actual2 = math_util.is_power_of_2(val2)
        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)

    def test_is_power_of_2_2(self):
        expected = True
        val1 = 128
        val2 = 1024
        actual1 = math_util.is_power_of_2(val1)
        actual2 = math_util.is_power_of_2(val2)
        assert actual1 == actual2 == expected, "Expected doesn't match actual"


if __name__ == "__main__":
    unittest.main()
