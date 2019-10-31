import numpy as np
import unittest

from src.python.main.math.complex_num import complex_num
from src.python.main.signal_processing import analyzation
from src.python.main.util import mapping
from src.python.main.util.exceptions import VectorLengthMismatchException

VEC_1 = [1, 2, 83, 4, 7, 7, 7, 9]


class AnalyzationTest(unittest.TestCase):

    def test_get_sum_of_cmplx_comp_squares(self):
        num1 = complex_num(2, 2)
        num2 = complex_num(-2, 2)
        num3 = complex_num(0, 1)
        num4 = complex_num(1, 0)
        expected1 = 8
        expected2 = 8
        expected3 = 1
        expected4 = 1
        actual1 = analyzation.get_sum_of_cmplx_comp_squares(num1)
        actual2 = analyzation.get_sum_of_cmplx_comp_squares(num2)
        actual3 = analyzation.get_sum_of_cmplx_comp_squares(num3)
        actual4 = analyzation.get_sum_of_cmplx_comp_squares(num4)

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_magnitude(self):
        num1 = complex_num(2, 2)
        num2 = complex_num(-2, 2)
        num3 = complex_num(0, 1)
        num4 = complex_num(4, 4)
        expected1 = 3
        expected2 = 3
        expected3 = 1
        expected4 = 6
        actual1 = np.ceil(analyzation.get_magnitude(num1))
        actual2 = np.ceil(analyzation.get_magnitude(num2))
        actual3 = analyzation.get_magnitude(num3)
        actual4 = np.ceil(analyzation.get_magnitude(num4))

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_intensity_1(self):
        expected = 180
        signal = complex_num(32768, 0)
        actual = np.floor(analyzation.get_intensity(signal))
        self.assertEqual(expected, actual)

    def test_intensity_2(self):
        expected = 0
        signal = complex_num(1, 0)
        actual = np.floor(analyzation.get_intensity(signal))
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
        actual1 = analyzation.bin_to_hz(bin1, fft_size, fs)
        actual2 = analyzation.bin_to_hz(bin2, fft_size, fs)
        actual3 = analyzation.bin_to_hz(bin3, fft_size, fs)
        actual4 = analyzation.bin_to_hz(bin4, fft_size, fs)

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)
        self.assertEqual(expected4, actual4)

    def test_get_max_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        expected = analyzation.get_intensity(complex_num(5, 0))
        actual = analyzation.get_max_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_max_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        expected = analyzation.get_intensity(complex_num(0, 0))
        actual = analyzation.get_max_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_min_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        expected = analyzation.get_intensity(complex_num(1, 0))
        actual = analyzation.get_min_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_min_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        expected = analyzation.get_intensity(complex_num(0, 0))
        actual = analyzation.get_min_intensity_cmplx_vec(vec)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_1(self):
        vec1 = VEC_1
        vec2 = [1, 2, 21, 4, 3, 3, 3, 9]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0.5
        actual = analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_2(self):
        vec1 = VEC_1
        vec2 = [1, 2, 21, 4, 3, 7, 3, 9]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 5 / 8
        actual = analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_3(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [4.01, 4, 6, 7]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0
        actual = analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_4(self):
        vec1 = [5, 10, 15, 20]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = analyzation.get_intensity(complex_num(2, 0)) / 2
        expected = 1.0
        actual = analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_intensity_similarity_5(self):
        vec1 = [2, 10, 15, 20, 4]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = analyzation.get_intensity(complex_num(2, 0)) / 2
        raised = None
        try:
            analyzation.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        except VectorLengthMismatchException as e:
            raised = e
        if not raised:
            self.fail("Exception not thrown for vector length mismatch")

    def test_get_signal_magnitude_similarity_1(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 3, 3, 9]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0.5
        actual = analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_magnitude_similarity_2(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 7, 3, 9]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 5 / 8
        actual = analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_get_signal_magnitude_similarity_3(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [4.01, 4, 6, 7]
        cmplx_vec1 = mapping.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = mapping.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0
        actual = analyzation.get_signal_magnitude_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_1(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [5, 4, 9, 10]
        expected = True
        actual = analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_2(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [6, 4, 9, 1]
        expected = False
        actual = analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_check_if_intensity_subset_3(self):
        vec1 = [5, 5, 10, 10]
        vec2 = [5, 5, 10, 10]
        expected = True
        actual = analyzation.check_if_intensity_subset(vec1, vec2)
        self.assertEqual(expected, actual)

    def test_get_signal_difference_1(self):
        vec1 = [complex_num(0, 0), complex_num(5, 10), complex_num(10, 20), complex_num(2, -1)]
        vec2 = [complex_num(2, 2), complex_num(5, 10), complex_num(1, 2), complex_num(2, -1)]
        expected = [complex_num(-2, -2), complex_num(0, 0), complex_num(9, 18), complex_num(0, -2)]
        actual = analyzation.get_signal_difference(vec1, vec2)
        for i in range(0, len(actual)):
            print(actual[i], expected[i], vec1[i], vec2[i])
            self.assertEqual(actual[i], expected[i])


if __name__ == "__main__":
    unittest.main()
