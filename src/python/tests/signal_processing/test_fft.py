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
        assert expected == actual, "Assertion error in fft_test_1"

    def test_fft_2(self):
        expected = [cmplx.complex_num(6, 0), cmplx.complex_num(-2, -2), cmplx.complex_num(2, 0), cmplx.complex_num(-2, 2)]
        num1 = cmplx.complex_num(1, 0)
        num2 = cmplx.complex_num(2, 0)
        num3 = cmplx.complex_num(3, 0)
        actual = fft.fft([num1, num2, num3])
        for i in range(0, len(actual)):
            actual[i] = actual[i].round()
        print(actual[0], actual[1], actual[2])
        assert expected == actual, "Assertion error in fft_test_1"


    def test_ifft_1(self):
        expected = [cmplx.complex_num(1, 0), cmplx.complex_num(2, 0)]
        num1 = cmplx.complex_num(1, 0)
        num2 = cmplx.complex_num(2, 0)
        actual = fft.fft([num1, num2])
        actual = fft.ifft(actual)
        assert expected == actual, "Assertion error in fft_test_1"

    def test_fft_ifft_random(self):
        N = 1024
        expected = ru.get_random_complex_vec(N, -100000, 100000)
        actualTemp = fft.fft(expected)
        actual = fft.ifft(actualTemp)
        for i in range(0, len(expected)):
            assert expected[i].round() == actual[i].round(), "Expected value did no match actual"
        assert len(actual) == N, "Resulting vector length did not match expected size"
        assert actualTemp is not expected, "IFFT resulting vector is equal to the FFT resulting vector"

if __name__ == "__main__":
    print("test_fft")
    unittest.main()
