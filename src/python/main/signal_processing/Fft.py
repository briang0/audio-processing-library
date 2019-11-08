import numpy as np

from src.python.main.math.ComplexNum import ComplexNum
from src.python.main.util import MathUtil

max16bit = 32768


def ifft_matrix(vec, samples, sample_rate):
    ifft_mat = [[ComplexNum(0, 0) for x in range(samples)] for y in range(sample_rate)]
    for i in range(0, samples):
        ifft_mat[i] = ifft(vec[i:i + sample_rate])
    return ifft_mat


def short_time_fft(vec, fft_size, overlap):
    print(len(vec))
    samples_per_bins = len(vec) // fft_size
    overlap_ratio = fft_size // overlap
    print((samples_per_bins // overlap) * overlap_ratio)
    fft_mat = [[ComplexNum(0, 0) for x in range(fft_size)] for y in range(((samples_per_bins // overlap) * overlap_ratio) + 2)]
    index = 0
    for i in range(0, samples_per_bins, overlap//2):
        # print(fft_size, overlap, overlap_ratio, samples_per_bins, i, overlap // 2, index)
        sliced_vector = vec[i:i+fft_size]
        fft_mat[index] = fft(sliced_vector)
        index += 1
    return fft_mat


def fft(vec):
    n = len(vec)
    if not MathUtil.is_power_of_2(n):
        next_pow = MathUtil.next_power_of_2(n)
        zeros = next_pow - n
        pad = [ComplexNum(0, 0)] * zeros
        vec.extend(pad)

    return fft_cmplx(vec)


def fft_cmplx(vec):
    n = len(vec)

    if n == 1:
        return [vec[0]]

    fft_evens = [ComplexNum(0, 0)] * (n // 2)
    fft_odds = [ComplexNum(0, 0)] * (n // 2)
    output = [ComplexNum(0, 0)] * n

    for i in range(0, len(fft_evens)):
        fft_evens[i] = vec[2 * i]
        fft_odds[i] = vec[2 * i + 1]
    fft_evens = fft(fft_evens)
    fft_odds = fft(fft_odds)

    for k in range(0, n // 2):
        exp = ComplexNum(np.cos(-2 * np.pi * k / n), np.sin(-2 * np.pi * k / n))
        product = exp.mult(fft_odds[k])
        output[k] = (fft_evens[k].add(product))
        output[k + n // 2] = (fft_evens[k].sub(product))
    return output


def ifft(vec):
    n = len(vec)
    output = vec.copy()

    for i in range(0, n):
        output[i] = vec[i].conj()
    output = fft(output)

    for i in range(0, n):
        output[i] = output[i].conj().scale(1 / n)

    return output
