import os, sys
sys.path.insert(0, os.path.abspath(".."))
import main.math.Complex as cmplx

def real_to_cmplx_obj_vec(vec):
  return list(map(cmplx.Complex, vec))

def real_to_cmplx_obj_mat(mat):
    out = []

    for vec in mat:
        out.append(real_to_cmplx_obj_vec(vec))

    return out
