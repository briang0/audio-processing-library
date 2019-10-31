from src.python.main.math import ComplexNum
from src.python.main.signal_processing import Analyzation


def remove_below_db_thresh(vec, thresh_db):
    for i in range(0, len(vec)):
        intensity = Analyzation.get_intensity(vec[i])
        if intensity > thresh_db:
            vec[i] = ComplexNum.complex_num(0, 0)
    return vec
