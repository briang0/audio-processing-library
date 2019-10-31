import unittest

from src.python.main.math.ComplexNum import ComplexNum
from src.python.main.util import Formatter


class TestFormat(unittest.TestCase):

    def test_str_cmplx_1(self):
        expected = ComplexNum.ComplexNum(1, 2)
        cmplx_string = "1 + 2i"
        actual = Formatter.string_to_complex_num(cmplx_string)
        self.assertEqual(expected, actual)

    def test_str_cmplx_2(self):
        expected = ComplexNum.ComplexNum(1, -2)
        cmplx_string = "1 + -2i"
        actual = Formatter.string_to_complex_num(cmplx_string)
        self.assertEqual(expected, actual)

    def test_str_cmplx_3(self):
        expected = ComplexNum.ComplexNum(-461, -23567)
        cmplx_str = "-461 + -23567i"
        actual = Formatter.string_to_complex_num(cmplx_str)
        self.assertEqual(expected, actual)

    def test_str_cmplx_4(self):
        expected = ComplexNum.ComplexNum(0, 0)
        cmplx_str = "0 + -0i"
        actual = Formatter.string_to_complex_num(cmplx_str)
        self.assertEqual(expected, actual)

    def test_str_cmplx_5(self):
        expected = ComplexNum.ComplexNum(-0.5, 0.00025)
        complx_num = "-0.5 + 0.00025i"
        actual = Formatter.string_to_complex_num(complx_num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
