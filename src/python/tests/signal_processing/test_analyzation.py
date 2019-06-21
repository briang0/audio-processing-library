import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import python.main.signal_processing.analyzation as anlyz
import python.main.util.random_util as ru
import python.main.util.mapping as map
from python.main.util.exceptions import VectorLengthMismatchException
import numpy as np
import unittest

class fft_test(unittest.TestCase):

    def test_get_sum_of_cmplx_comp_squares(self):
        num1 = cmplx.complex_num(2, 2)
        num2 = cmplx.complex_num(-2, 2)
        num3 = cmplx.complex_num(0, 1)
        num4 = cmplx.complex_num(1, 0)
        expected1 = 8
        expected2 = 8
        expected3 = 1
        expected4 = 1
        actual1 = anlyz.get_sum_of_cmplx_comp_squares(num1)
        actual2 = anlyz.get_sum_of_cmplx_comp_squares(num2)
        actual3 = anlyz.get_sum_of_cmplx_comp_squares(num3)
        actual4 = anlyz.get_sum_of_cmplx_comp_squares(num4)

        assert expected1 == actual1, ""
        assert expected2 == actual2, ""
        assert expected3 == actual3, ""
        assert expected4 == actual4, ""

    def test_magnitude(self):
        num1 = cmplx.complex_num(2, 2)
        num2 = cmplx.complex_num(-2, 2)
        num3 = cmplx.complex_num(0, 1)
        num4 = cmplx.complex_num(4, 4)
        expected1 = 3
        expected2 = 3
        expected3 = 1
        expected4 = 6
        actual1 = np.ceil(anlyz.get_magnitude(num1))
        actual2 = np.ceil(anlyz.get_magnitude(num2))
        actual3 = anlyz.get_magnitude(num3)
        actual4 = np.ceil(anlyz.get_magnitude(num4))

        assert expected1 == actual1, ""
        assert expected2 == actual2, ""
        assert expected3 == actual3, ""
        assert expected4 == actual4, ""

    def test_intensity_1(self):
        expected = 180
        signal = cmplx.complex_num(32768, 0)
        actual = np.floor(anlyz.get_intensity(signal))
        assert actual == expected, "The computed intensity didn't match the expected"

    def test_intensity_2(self):
        expected = 0
        signal = cmplx.complex_num(1, 0)
        actual = np.floor(anlyz.get_intensity(signal))
        assert actual == expected, "The computed intensity didn't match the expected"

    def test_bin_to_hz(self):
        Fs = 44100
        fft_size = 128
        bin1 = 128
        bin2 = 0
        bin3 = 64
        bin4 = 15
        expected1 = Fs
        expected2 = 0
        expected3 = 22050
        expected4 = 5168
        actual1 = anlyz.bin_to_hz(bin1, fft_size, Fs)
        actual2 = anlyz.bin_to_hz(bin2, fft_size, Fs)
        actual3 = anlyz.bin_to_hz(bin3, fft_size, Fs)
        actual4 = anlyz.bin_to_hz(bin4, fft_size, Fs)

        assert expected1 == actual1, ""
        assert expected2 == actual2, ""
        assert expected3 == actual3, ""
        assert expected4 == actual4, ""

    def test_get_max_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        cmplx_vec = map.real_to_cmplx_obj_vec(vec)
        expected = anlyz.get_intensity(cmplx.complex_num(5, 0))
        actual = anlyz.get_max_intensity_cmplx_vec(vec)
        assert actual == expected, ""

    def test_get_max_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        cmplx_vec = map.real_to_cmplx_obj_vec(vec)
        expected = anlyz.get_intensity(cmplx.complex_num(0, 0))
        actual = anlyz.get_max_intensity_cmplx_vec(vec)
        assert actual == expected, ""

    def test_get_min_intensity_cmplx_vec_1(self):
        vec = [1, 2, 3, 2, 2, 3, 5, 4]
        cmplx_vec = map.real_to_cmplx_obj_vec(vec)
        expected = anlyz.get_intensity(cmplx.complex_num(1, 0))
        actual = anlyz.get_min_intensity_cmplx_vec(vec)
        assert actual == expected, ""

    def test_get_min_intensity_cmplx_vec_2(self):
        vec = [0, 0, 0, 0, 0, 0, 0, 0]
        cmplx_vec = map.real_to_cmplx_obj_vec(vec)
        expected = anlyz.get_intensity(cmplx.complex_num(0, 0))
        actual = anlyz.get_min_intensity_cmplx_vec(vec)
        assert actual == expected, ""

    def test_get_signal_intensity_similarity_1(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 3, 3, 9]
        cmplx_vec1 = map.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = map.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0.5
        actual = anlyz.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        assert actual == expected, ""

    def test_get_signal_intensity_similarity_2(self):
        vec1 = [1, 2, 83, 4, 7, 7, 7, 9]
        vec2 = [1, 2, 21, 4, 3, 7, 3, 9]
        cmplx_vec1 = map.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = map.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 5 / 8
        actual = anlyz.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        assert actual == expected, ""

    def test_get_signal_intensity_similarity_3(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [4.01, 4, 6, 7]
        cmplx_vec1 = map.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = map.real_to_cmplx_obj_vec(vec2)
        tolerance = 0
        expected = 0
        actual = anlyz.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        assert actual == expected, ""

    def test_get_signal_intensity_similarity_4(self):
        vec1 = [5, 10, 15, 20]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = map.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = map.real_to_cmplx_obj_vec(vec2)
        tolerance = anlyz.get_intensity(cmplx.complex_num(2,0)) / 2
        expected = 1.0
        actual = anlyz.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        assert actual == expected, ""

    def test_get_signal_intensity_similarity_5(self):
        vec1 = [2, 10, 15, 20, 4]
        vec2 = [7, 8, 17, 22]
        cmplx_vec1 = map.real_to_cmplx_obj_vec(vec1)
        cmplx_vec2 = map.real_to_cmplx_obj_vec(vec2)
        tolerance = anlyz.get_intensity(cmplx.complex_num(2,0)) / 2
        raised = None
        try:
            anlyz.get_signal_intensity_similarity(cmplx_vec1, cmplx_vec2, tolerance)
        except VectorLengthMismatchException as e:
            raised = e
        if not raised:
            self.fail("Exception not thrown for vector length mismatch")

if __name__ == "__main__":
    unittest.main()
