import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.math.complex_num as cmplx

def vec_to_mat(vec, cols):
    mat = []
    cur_element = 0
    length = len(vec)
    num_rows = length // cols
    for i in range(0, num_rows):
        mat.append([])
        for j in range(0, cols):
            if (cur_element < length):
                mat[i].append(vec[cur_element])
            else:
                mat[i].append(0)
            cur_element += 1
    return mat

def string_to_complex_num(num):
    parts = num.split("+")
    real = float(parts[0])
    imag = parts[1]
    imag = imag.replace("i", "")
    iamg = float(imag)
    return cmplx.complex_num(real, imag)
