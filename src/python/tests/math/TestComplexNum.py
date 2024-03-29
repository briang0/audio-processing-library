import os, sys
import unittest

from src.python.main.math.ComplexNum import ComplexNum


class ComplexNumTests(unittest.TestCase):

    def test_init(self):
        expected = [1, 2]
        num = ComplexNum(1, 2)
        actual = [num.real, num.imag]
        self.assertEqual(expected, actual)

    def test_add_1(self):
        expected = [2, 4]
        num = ComplexNum(1, 2)
        num = num.add(num)
        actual = [num.real, num.imag]
        self.assertEqual(expected, actual)

    def test_add_2(self):
        expected = [-1, -2]
        num1 = ComplexNum(1, 2)
        num2 = ComplexNum(-2, -4)
        num1 = num1.add(num2)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_sub_1(self):
        expected = [0, 0]
        num = ComplexNum(1, 2)
        num = num.sub(num)
        actual = [num.real, num.imag]
        self.assertEqual(expected, actual)

    def test_sub_2(self):
        expected = [-1, -2]
        num1 = ComplexNum(1, 2)
        num2 = ComplexNum(2, 4)
        num1 = num1.sub(num2)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_mult_1(self):
        expected = [850, 11]
        num1 = ComplexNum(13, 2)
        num2 = ComplexNum(64, -9)
        num1 = num1.mult(num2)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_mult_2(self):
        expected = [0, 0]
        num1 = ComplexNum(13, 2)
        num2 = ComplexNum(0, 0)
        num1 = num1.mult(num2)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_abs(self):
        expected = [13, 2]
        num = ComplexNum(-13, -2)
        num = num.abs()
        actual = [num.real, num.imag]
        self.assertEqual(expected, actual)

    def test_scale_1(self):
        expected = [2, 4]
        num1 = ComplexNum(1, 2)
        num1 = num1.scale(2)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_scale_2(self):
        expected = [0.5, 1]
        num1 = ComplexNum(1, 2)
        num1 = num1.scale(0.5)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_scale_3(self):
        expected = [0, 0]
        num1 = ComplexNum(1, 2)
        num1 = num1.scale(0)
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_conjugate_1(self):
        expected = [1, -2]
        num1 = ComplexNum(1, 2)
        num1 = num1.conj()
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_conjugate_2(self):
        expected = [-1, 2]
        num1 = ComplexNum(-1, -2)
        num1 = num1.conj()
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)

    def test_comprehensive(self):
        expected = [24877, -3593]
        num1 = ComplexNum(-1, -67)
        num2 = ComplexNum(45, 356)
        num3 = ComplexNum(-67, 234)
        num4 = ComplexNum(1003, -12)
        num1 = num1.mult(num2).sub(num3).add(num4.conj())
        actual = [num1.real, num1.imag]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    print("test_complex_num")
    unittest.main()
