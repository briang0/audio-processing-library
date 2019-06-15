import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import python.main.util.format as fmt
import unittest

class test_format(unittest.TestCase):

    def test_str_cmplx_1(self):
        expected = cmplx.complex_num(1, 2)
        str = "1 + 2i"
        actual = fmt.string_to_complex_num(str)
        assert expected == actual, ("Expected: ", expected.real, expected.imag, " Actual: ", actual.real, actual.imag)

    def test_str_cmplx_2(self):
        expected = cmplx.complex_num(1, -2)
        str = "1 + -2i"
        actual = fmt.string_to_complex_num(str)
        assert expected == actual, ("Expected: ", expected.real, expected.imag, " Actual: ", actual.real, actual.imag)

    def test_str_cmplx_3(self):
        expected = cmplx.complex_num(-461, -23567)
        str = "-461 + -23567i"
        actual = fmt.string_to_complex_num(str)
        assert expected == actual, ("Expected: ", expected.real, expected.imag, " Actual: ", actual.real, actual.imag)

    def test_str_cmplx_4(self):
        expected = cmplx.complex_num(0, 0)
        str = "0 + -0i"
        actual = fmt.string_to_complex_num(str)
        assert expected == actual, ("Expected: ", expected.real, expected.imag, " Actual: ", actual.real, actual.imag)

    def test_str_cmplx_4(self):
        expected = cmplx.complex_num(-0.5, 0.00025)
        str = "-0.5 + 0.00025i"
        actual = fmt.string_to_complex_num(str)
        assert expected == actual, ("Expected: ", expected.real, expected.imag, " Actual: ", actual.real, actual.imag)

if __name__ == "__main__":
    unittest.main()
