import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.math.complex_num as cmplx
import python.main.util.format as fmt

def read_cmplx_matrix_from_csv(outputDir):
    f = open(outputDir)
    data = f.read()
    rows = data.split("\n")
    output = []

    for i in range(0, len(rows) - 1):
        elems = rows[i].split(",")
        output.append([])
        for j in range(0, len(elems) - 1):
            cmplx_str = elems[j]
            num = fmt.string_to_complex_num(cmplx_str)
            output[i].append(num)
    return output
