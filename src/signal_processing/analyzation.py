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
