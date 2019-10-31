from src.python.main.math.complex_num import complex_num
from src.python.main.signal_processing import fft
from src.python.main.util import random_util
import unittest


class FftTest(unittest.TestCase):

    def test_fft_1(self):
        expected = [complex_num(3, 0), complex_num(-1, 0)]
        num1 = complex_num(1, 0)
        num2 = complex_num(2, 0)
        actual = fft.fft([num1, num2])
        self.assertEqual(expected, actual)

    def test_fft_2(self):
        expected = [complex_num(6, 0), complex_num(-2, -2), complex_num(2, 0), complex_num(-2, 2)]
        num1 = complex_num(1, 0)
        num2 = complex_num(2, 0)
        num3 = complex_num(3, 0)
        actual = fft.fft([num1, num2, num3])
        for i in range(0, len(actual)):
            actual[i] = actual[i].round()
        print(actual[0], actual[1], actual[2])
        self.assertEqual(expected, actual)

    def test_ifft_1(self):
        expected = [complex_num(1, 0), complex_num(2, 0)]
        num1 = complex_num(1, 0)
        num2 = complex_num(2, 0)
        actual = fft.fft([num1, num2])
        actual = fft.ifft(actual)
        self.assertEqual(expected, actual)

    def test_fft_ifft_random(self):
        n = 1024
        expected = random_util.get_random_complex_vec(n, -100000, 100000)
        actual_temp = fft.fft(expected)
        actual = fft.ifft(actual_temp)
        for i in range(0, len(expected)):
            assert expected[i].round() == actual[i].round(), "Expected value did no match actual"
        assert len(actual) == n, "Resulting vector length did not match expected size"
        self.assertEqual(n, len(actual))
        self.assertNotEqual(expected, actual_temp)


if __name__ == "__main__":
    print("test_fft")
    unittest.main()
