from src.python.main.math import ComplexNum


def real_to_cmplx_obj_vec(vec):
    return list(map(ComplexNum.ComplexNum, vec))


def real_to_cmplx_obj_mat(mat):
    out = []

    for vec in mat:
        out.append(real_to_cmplx_obj_vec(vec))

    return out
