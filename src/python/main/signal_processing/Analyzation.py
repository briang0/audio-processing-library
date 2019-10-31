import numpy as np

from src.python.main.util.Exceptions import VectorLengthMismatchException

max16bit = 32768


def get_sum_of_cmplx_comp_squares(complex_number):
    real = complex_number.real
    imag = complex_number.imag
    return real * real + imag * imag


def get_magnitude(complex_number):
    return np.sqrt(get_sum_of_cmplx_comp_squares(complex_number))


def get_intensity(complex_number):
    val = get_sum_of_cmplx_comp_squares(complex_number)
    intensity = 20 * np.log10(val)
    return np.abs(intensity)


def bin_to_hz(frequency_bin, fft_size, sample_rate):
    step = sample_rate / fft_size
    return np.round(frequency_bin * step)


def get_max_intensity_cmplx_vec(vec):
    max_intensity = get_intensity(vec[0])
    for num in vec:
        cur_intensity = get_intensity(num)
        if cur_intensity > max_intensity:
            max_intensity = cur_intensity
    return max_intensity


def get_min_intensity_cmplx_vec(vec):
    minimum_intensity = get_intensity(vec[0])
    for num in vec:
        cur_intensity = get_intensity(num)
        if cur_intensity < minimum_intensity:
            minimum_intensity = cur_intensity
    return minimum_intensity


def get_signal_intensity_similarity(signal1, signal2, tolerance):
    len1 = len(signal1)
    len2 = len(signal2)
    num_similar = 0
    if len1 is not len2:
        msg = "Signal 1 lenght =", len1, "Signal 2 length =", len2
        raise VectorLengthMismatchException(msg)

    for i in range(0, len1):
        intensity1 = get_intensity(signal1[i])
        intensity2 = get_intensity(signal2[i])
        dif = intensity1 - intensity2
        if intensity2 > intensity1:
            dif = intensity2 - intensity1

        if dif <= tolerance:
            num_similar += 1

    similarity = num_similar / len1

    return similarity


def get_signal_magnitude_similarity(signal1, signal2, tolerance):
    len1 = len(signal1)
    len2 = len(signal2)
    num_similar = 0
    if len1 is not len2:
        raise Exception("The length of the two signals are not the same")

    for i in range(0, len1):
        magnitude1 = get_magnitude(signal1[i])
        magnitude2 = get_magnitude(signal2[i])
        dif = magnitude1 - magnitude2
        abs_dif = np.abs(dif)
        if abs_dif <= tolerance:
            num_similar += 1

    similarity = num_similar / len1

    return similarity


def check_if_intensity_subset(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)

    if len1 is not len2:
        return False

    for i in range(0, len1):
        intensity1 = get_intensity(signal1[i])
        intensity2 = get_intensity(signal2[i])
        if intensity2 > intensity1:
            return False
    return True


def get_signal_difference(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)
    if len1 is not len2:
        return None
        # TODO throw an excpetion
    output = []
    for i in range(0, len1):
        output.append(signal1[i].sub(signal2[i]))
    return output


def get_signal_intensity_difference(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)
    if len1 is not len2:
        return None
        # TODO throw an excpetion
    output = []
    for i in range(0, len1):
        intensity1 = get_intensity(signal1[i])
        intensity2 = get_intensity(signal2[i])
        output.append(intensity1 - intensity2)
    return output
