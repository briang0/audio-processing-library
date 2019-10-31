import numpy as np


def is_power_of_2(num):
    if num == 0:
        return False
    log2 = np.log10(num) / np.log10(2)
    return np.ceil(log2) == np.floor(log2)


def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()
