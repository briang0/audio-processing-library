import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import unittest

class complex_num_tests(unittest.TestCase):

    def test_init(self):
        expected = [1, 2]
        num = cmplx.complex_num(1, 2)
        actual = [num.real, num.imag]
        assert expected == actual, "Assertion error in test_init"

    def test_add_1(self):
        expected = [2, 4]
        num = cmplx.complex_num(1, 2)
        num = num.add(num)
        actual = [num.real, num.imag]
        assert expected == actual, "Assertion error in test_add_1"

    def test_add_2(self):
        expected = [-1, -2]
        num1 = cmplx.complex_num(1, 2)
        num2 = cmplx.complex_num(-2, -4)
        num1 = num1.add(num2)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_add_2"

    def test_sub_1(self):
        expected = [0, 0]
        num = cmplx.complex_num(1, 2)
        num = num.sub(num)
        actual = [num.real, num.imag]
        assert expected == actual, "Assertion error in test_sub_1"

    def test_sub_2(self):
        expected = [-1, -2]
        num1 = cmplx.complex_num(1, 2)
        num2 = cmplx.complex_num(2, 4)
        num1 = num1.sub(num2)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_sub_1"

    def test_mult_1(self):
        expected = [850, 11]
        num1 = cmplx.complex_num(13, 2)
        num2 = cmplx.complex_num(64, -9)
        num1 = num1.mult(num2)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_mult_1"

    def test_mult_2(self):
        expected = [0, 0]
        num1 = cmplx.complex_num(13, 2)
        num2 = cmplx.complex_num(0, 0)
        num1 = num1.mult(num2)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_mult_2"

    def test_abs(self):
        expected = [13, 2]
        num = cmplx.complex_num(-13, -2)
        num = num.abs(num)
        actual = [num.real, num.imag]
        assert expected == actual, "Assertion error in test_abs"

    def test_scale_1(self):
        expected = [2, 4]
        num1 = cmplx.complex_num(1, 2)
        num1 = num1.scale(2)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_scale_1"

    def test_scale_2(self):
        expected = [0.5, 1]
        num1 = cmplx.complex_num(1, 2)
        num1 = num1.scale(0.5)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_scale_2"

    def test_scale_3(self):
        expected = [0, 0]
        num1 = cmplx.complex_num(1, 2)
        num1 = num1.scale(0)
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_scale_2"

    def test_conjugate_1(self):
        expected = [1, -2]
        num1 = cmplx.complex_num(1, 2)
        num1 = num1.conj()
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_conjugate_1"

    def test_conjugate_2(self):
        expected = [-1, 2]
        num1 = cmplx.complex_num(-1, -2)
        num1 = num1.conj()
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_conjugate_2"

    def test_comprehensive(self):
        expected = [24877, -3593]
        num1 = cmplx.complex_num(-1, -67)
        num2 = cmplx.complex_num(45, 356)
        num3 = cmplx.complex_num(-67, 234)
        num4 = cmplx.complex_num(1003, -12)
        num1 = num1.mult(num2).sub(num3).add(num4.conj())
        actual = [num1.real, num1.imag]
        assert expected == actual, "Assertion error in test_comprehensive"


if __name__ == "__main__":
    print("test_complex_num")
    unittest.main()
