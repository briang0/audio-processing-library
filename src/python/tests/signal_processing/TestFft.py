from src.python.main.math.ComplexNum import ComplexNum
from src.python.main.signal_processing import Fft
from src.python.main.util import RandomUtil
import unittest


class FftTest(unittest.TestCase):

    def test_fft_1(self):
        expected = [ComplexNum.ComplexNum(3, 0), ComplexNum.ComplexNum(-1, 0)]
        num1 = ComplexNum.ComplexNum(1, 0)
        num2 = ComplexNum.ComplexNum(2, 0)
        actual = Fft.fft([num1, num2])
        self.assertEqual(expected, actual)

    def test_fft_2(self):
        expected = [ComplexNum.ComplexNum(6, 0), ComplexNum.ComplexNum(-2, -2), ComplexNum.ComplexNum(2, 0), ComplexNum.ComplexNum(-2, 2)]
        num1 = ComplexNum.ComplexNum(1, 0)
        num2 = ComplexNum.ComplexNum(2, 0)
        num3 = ComplexNum.ComplexNum(3, 0)
        actual = Fft.fft([num1, num2, num3])
        for i in range(0, len(actual)):
            actual[i] = actual[i].round()
        print(actual[0], actual[1], actual[2])
        self.assertEqual(expected, actual)

    def test_ifft_1(self):
        expected = [ComplexNum.ComplexNum(1, 0), ComplexNum.ComplexNum(2, 0)]
        num1 = ComplexNum.ComplexNum(1, 0)
        num2 = ComplexNum.ComplexNum(2, 0)
        actual = Fft.fft([num1, num2])
        actual = Fft.ifft(actual)
        self.assertEqual(expected, actual)

    def test_fft_ifft_random(self):
        n = 1024
        expected = RandomUtil.get_random_complex_vec(n, -100000, 100000)
        actual_temp = Fft.fft(expected)
        actual = Fft.ifft(actual_temp)
        for i in range(0, len(expected)):
            assert expected[i].round() == actual[i].round(), "Expected value did no match actual"
        assert len(actual) == n, "Resulting vector length did not match expected size"
        self.assertEqual(n, len(actual))
        self.assertNotEqual(expected, actual_temp)


if __name__ == "__main__":
    print("test_fft")
    unittest.main()
