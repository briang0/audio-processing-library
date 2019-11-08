import numpy as np


def hanning(vec):
    out = [0] * len(vec)
    for i in range(0, len(vec)):
        out[i] = vec[i] * (0.5 * (1-np.cos(2*3.14159*i/(len(vec)-1))))
    return out