import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.math.complex_num as cmplx

def write_cmplx_matrix_to_csv(mat, outputDir):
    f = open(outputDir, 'w+')
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            f.write(str(mat[i][j]) + ",")
        f.write("\n")
