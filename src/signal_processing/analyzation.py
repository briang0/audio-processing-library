import os, sys
sys.path.insert(0, os.path.abspath("../.."))
import src.math.Complex as cmplx
import numpy as np

max16bit = 32768

def get_magnitude(complex):
    real = complex.real
    imag = complex.imag
    return np.sqrt(real * real + imag * imag)

def get_intensity(complex, FFTSize):
    magnitude = get_magnitude(complex)
    intensity = 20 * np.log10(magnitude/(max16bit))
    return np.abs(intensity)

def bin_to_hz(bin, fft_size, sample_rate):
    step = sample_rate / fft_size
    return bin * step

def get_max_intensity_cmplx_vec(vec):
    fft_size = len(vec)
    max = get_intensity(vec[0], fft_size)
    for num in vec:
        cur_intensity = get_intensity(num, fft_size)
        if (cur_intensity > max):
            max = cur_intensity
    return max

def get_min_intensity_cmplx_vec(vec):
    fft_size = len(vec)
    min = get_intensity(vec[0], fft_size)
    for num in vec:
        cur_intensity = get_intensity(num, fft_size)
        if (cur_intensity < min):
            min = cur_intensity
    return min

def get_signal_intensity_similarity(signal1, signal2, tolerance):
    len1 = len(signal1)
    len2 = len(signal2)
    num_similar = 0
    if (len1 is not len2):
        raise Exception("The length of the two signals are not the same")
        return

    for i in range(0, len1):
        intensity1 = get_intensity(signal1[i], len1)
        intensity2 = get_intensity(signal2[i], len2)
        dif = intensity1 - intensity2
        abs_dif = np.abs(dif)
        if (abs_dif <= tolerance):
            num_similar += 1

    similarity = num_similar / len1

    return similarity

def get_signal_magnitude_similarity(signal1, signal2, tolerance):
    len1 = len(signal1)
    len2 = len(signal2)
    num_similar = 0
    if (len1 is not len2):
        raise Exception("The length of the two signals are not the same")
        return

    for i in range(0, len1):
        magnitude1 = get_magnitude(signal1[i])
        magnitude2 = get_magnitude(signal2[i])
        dif = magnitude1 - magnitude2
        abs_dif = np.abs(dif)
        if (abs_dif <= tolerance):
            num_similar += 1

    similarity = num_similar / len1

    return similarity

def check_if_intensity_subset(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)

    if (len1 is not len2):
        return False

    for i in range(0, len1):
        intensity1 = get_intensity(signal1[i], len1)
        intensity2 = get_intensity(signal2[i], len2)
        if (intensity2 >= intensity1):
            return False

    return True
