import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import python.main.signal_processing.fft as fft
import unittest

class fft_test(unittest.TestCase):

    def test_fft_1(self):
        expected = [cmplx.complex_num(3, 0), cmplx.complex_num(-1, 0)]
        num1 = cmplx.complex_num(1, 0)
        num2 = cmplx.complex_num(2, 0)
        actual = fft.fft([num1, num2])
        print(expected, actual)
        assert expected == actual, "Assertion error in fft_test_1"


if __name__ == "__main__":
    unittest.main()
