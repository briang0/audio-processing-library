import numpy as np

def is_power_of_2(num):
    if num == 0:
        return False
    log2 = np.log10(num) / np.log10(2)
    return np.ceil(log2) == np.floor(log2)
