import numpy as np

from src.python.main.math.ComplexNum import ComplexNum
from src.python.main.util import MathUtil

max16bit = 32768


def fft(vec):
    n = len(vec)
    if not MathUtil.is_power_of_2(n):
        next_pow = MathUtil.next_power_of_2(n)
        zeros = next_pow - n
        pad = [ComplexNum.ComplexNum(0, 0)] * zeros
        print(zeros)
        vec.extend(pad)

    return fft_cmplx(vec)


def fft_cmplx(vec):
    n = len(vec)

    if n == 1:
        return [vec[0]]

    fft_evens = []
    fft_odds = []
    output = [] * n

    for i in range(0, n // 2):
        fft_evens.append(vec[2 * i])
    fft_evens = fft(fft_evens)

    for i in range(0, n // 2):
        fft_odds.append(vec[2 * i + 1])
    fft_odds = fft(fft_odds)

    for k in range(0, n // 2):
        exp = ComplexNum.ComplexNum(np.cos(-2 * np.pi * k / n), np.sin(-2 * np.pi * k / n))
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
