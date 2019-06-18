import os, sys
sys.path.insert(0, os.path.abspath("../.."))
import python.main.math.complex_num as cmplx
import python.main.signal_processing.analyzation as anlyz
import numpy as np

def remove_below_db_thresh(vec, thresh_db):
    for i in range(0, len(vec)):
        intensity = anlyz.get_intensity(vec[i])
        if (intensity > thresh_db):
            vec[i] = cmplx.complex_num(0, 0)
    return vec
