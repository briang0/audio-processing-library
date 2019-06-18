import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.util.math_util as mutil
import unittest

class test_format(unittest.TestCase):

    def test_is_power_of_2_1(self):
        expected = False
        val1 = 129
        val2 = 127
        actual1 = mutil.is_power_of_2(val1)
        actual2 = mutil.is_power_of_2(val2)
        assert actual1 == actual2 == expected, "Expected doesn't match actual"

    def test_is_power_of_2_2(self):
        expected = True
        val1 = 128
        val2 = 1024
        actual1 = mutil.is_power_of_2(val1)
        actual2 = mutil.is_power_of_2(val2)
        assert actual1 == actual2 == expected, "Expected doesn't match actual"

if __name__ == "__main__":
    unittest.main()
