import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import python.main.signal_processing.fft as fft
import python.main.util.random_util as ru
import unittest

class fft_test(unittest.TestCase):

    def test_fft_1(self):
        expected = [cmplx.complex_num(3, 0), cmplx.complex_num(-1, 0)]
        num1 = cmplx.complex_num(1, 0)
        num2 = cmplx.complex_num(2, 0)
        actual = fft.fft([num1, num2])
        print(expected, actual)
        assert expected == actual, "Assertion error in fft_test_1"

    def test_ifft_1(self):
        expected = [cmplx.complex_num(1, 0), cmplx.complex_num(2, 0)]
        num1 = cmplx.complex_num(1, 0)
        num2 = cmplx.complex_num(2, 0)
        actual = fft.fft([num1, num2])
        actual = fft.ifft(actual)
        assert expected == actual, "Assertion error in fft_test_1"

    def test_fft_ifft_random(self):
        N = 32
        expected = ru.get_random_complex_vec(N, -100, 100)
        actualTemp = fft.fft(expected)
        actual = fft.ifft(actualTemp)
        assert actual == expected, "FFT and IFFT output not the same"
        assert len(actual) == N, "Resulting vector length did not match expected size"
        assert actualTemp is not expected, "IFFT resulting vector is equal to the FFT resulting vector"

if __name__ == "__main__":
    unittest.main()
