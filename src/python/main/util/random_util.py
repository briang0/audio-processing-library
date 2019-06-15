import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import random

def get_random_complex_vec(n, low, high):
    output = []
    for i in range(0, n):
        output.append(get_random_complex(low, high))

    return output

def get_random_complex(low, high):
    r1 = random.randint(low, high)
    r2 = random.randint(low, high)
    return cmplx.complex_num(r1, r2)
