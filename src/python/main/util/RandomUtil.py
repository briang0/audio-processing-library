import random

from src.python.main.math import ComplexNum


def get_random_complex_vec(n, low, high):
    output = []
    for i in range(0, n):
        output.append(get_random_complex(low, high))

    return output


def get_random_complex(low, high):
    r1 = float(random.randint(low, high))
    r2 = float(random.randint(low, high))
    return ComplexNum.ComplexNum(r1, r2)
