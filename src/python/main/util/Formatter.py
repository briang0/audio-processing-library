from src.python.main.math.ComplexNum import ComplexNum


def vec_to_mat(vec, cols):
    mat = []
    cur_element = 0
    length = len(vec)
    num_rows = length // cols
    for i in range(0, num_rows):
        mat.append([])
        for j in range(0, cols):
            if cur_element < length:
                mat[i].append(vec[cur_element])
            else:
                mat[i].append(0)
            cur_element += 1
    return mat


def string_to_complex_num(num):
    parts = num.split("+")
    real = float(parts[0])
    imag = parts[1].lstrip()
    imag = imag.replace("i", "")
    imag = float(imag)
    return ComplexNum(real, imag)
