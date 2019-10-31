import numpy as np
import unittest

from src.python.main.math.ComplexNum import ComplexNum
from src.python.main.signal_processing import Analyzation
from src.python.main.util import Mapping
from src.python.main.util.Exceptions import VectorLengthMismatchException

VEC_1 = [1, 2, 83, 4, 7, 7, 7, 9]


class AnalyzationTest(unittest.TestCase):

    def test_get_sum_of_cmplx_comp_squares(self):
        num1 = ComplexNum(2, 2)
        num2 = ComplexNum(-2, 2)
        num3 = ComplexNum(0, 1)
        num4 = ComplexNum(1, 0)
        expected1 = 8
        expected2 = 8
        expected3 = 1
        expected4 = 1
        actual1 = Analyzation.get_sum_of_cmplx_comp_squares(num1)
        actual2 = Analyzation.get_sum_of_cmplx_comp_squares(num2)
        actual3 = Analyzation.get_sum_of_cmplx_comp_squares(num3)
        actual4 = Analyzation.get_sum_of_cmplx_comp_squares(num4)

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_magnitude(self):
        num1 = ComplexNum(2, 2)
        num2 = ComplexNum(-2, 2)
        num3 = ComplexNum(0, 1)
        num4 = ComplexNum(4, 4)
        expected1 = 3
        expected2 = 3
        expected3 = 1
        expected4 = 6
        actual1 = np.ceil(Analyzation.get_magnitude(num1))
        actual2 = np.ceil(Analyzation.get_magnitude(num2))
        actual3 = Analyzation.get_magnitude(num3)
        actual4 = np.ceil(Analyzation.get_magnitude(num4))

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_intensity_1(self):
        expected = 180
        signal = ComplexNum(32768, 0)
        actual = np.floor(Analyzation.get_intensity(signal))
        self.assertEqual(expected, actual)

    def test_intensity_2(self):
        expected = 0
        signal = ComplexNum(1, 0)
        actual = np.floor(Analyzation.get_intensity(signal))
        self.assertEqual(expected, actual)

    def test_bin_to_hz(self):
        fs = 44100
        fft_size = 128
        bin1 = 128
        bin2 = 0
        bin3 = 64
        bin4 = 15
        expected1 = fs
        expected2 = 0
        expected3 = 22050
        expected4 = 5168
        actual1 = Analyzation.bin_to_hz(bin1, fft_size, fs)
        actual2 = Analyzation.bin_to_hz(bin2, fft_size, fs)
        actual3 = Analyzation.bin_to_hz(bin3, fft_size, fs)
        actual4 = Analyzation.bin_to_hz(bin4, fft_size, fs)

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_get_max_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        expected = Analyzation.get_intensity(ComplexNum(5, 0))
        actual = Analyzation.get_max_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_max_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        expected = Analyzation.get_intensity(ComplexNum(0, 0))
        actual = Analyzation.get_max_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_min_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        expected = Analyzation.get_intensity(ComplexNum(1, 0))
        actual = Analyzation.get_min_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_min_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        expected = Analyzation.get_intensity(ComplexNum(0, 0))
        actual = Analyzation.get_min_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_1(self):
        vec1 = VEC_1
        vec2 = [1, 2, 21, 4, 3, 3, 3, 9]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0.5
        actual = Analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_2(self):
        vec1 = VEC_1
        vec2 = [1, 2, 21, 4, 3, 7, 3, 9]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 5 / 8
        actual = Analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_3(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [4.01, 4, 6, 7]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0
        actual = Analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_4(self):
        vec1 = [5, 10, 15, 20]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = Analyzation.get_intensity(ComplexNum(2, 0)) / 2
        expected = 1.0
        actual = Analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_5(self):
        vec1 = [2, 10, 15, 20, 4]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = Analyzation.get_intensity(ComplexNum(2, 0)) / 2
        raised = None
        try:
            Analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        except VectorLengthMismatchException as e:
            raised = e
        if not raised:
            self.fail("Exception not thrown for vector length mismatch")

    def test_get_signal_magnitude_similarity_1(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 3, 3, 9]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0.5
        actual = Analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_magnitude_similarity_2(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 7, 3, 9]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 5 / 8
        actual = Analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_magnitude_similarity_3(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [4.01, 4, 6, 7]
        cmplx_vec1 = Mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = Mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0
        actual = Analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_1(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [5, 4, 9, 10]
        expected = True
        actual = Analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_2(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [6, 4, 9, 1]
        expected = False
        actual = Analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_3(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [5, 5, 10, 10]
        expected = True
        actual = Analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_get_signal_difference_1(self):
        vec1 = [ComplexNum(0, 0), ComplexNum(5, 10), ComplexNum(10, 20), ComplexNum(2, -1)]
        vec2 = [ComplexNum(2, 2), ComplexNum(5, 10), ComplexNum(1, 2), ComplexNum(2, -1)]
        expected = [ComplexNum(-2, -2), ComplexNum(0, 0), ComplexNum(9, 18), ComplexNum(0, 0)]
        actual = Analyzation.get_signal_difference(vec1, vec2)
        for i in range(0, len(actual)):
            self.assertEqual(actual[i], expected[i])


if __name__ == "__main__":
    unittest.main()
