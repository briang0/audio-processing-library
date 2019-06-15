import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.math.complex_num as cmplx
import python.main.util.format as fmt

def read_cmplx_matrix_from_csv(outputDir):
    f = open(outputDir)
    data = f.read()
    rows = data.split("\n")
    output = []

    for i in range(0, len(rows)):
        elems = data.split(",")
        output.append([])
        for j in range(0, len(elems) - 1):
            cmplx_str = elems[j]
            num = fmt.string_to_complex_num(cmplx_str)
            output[i].append(num)

    return num



    # f = open(outputDir+".csv", 'w')
    # mag = open(outputDir + "mag.csv", 'w')
    # db = open(outputDir + "db.csv", "w")
    # for i in range(0, len(mat)):
    #     for j in range(0, len(mat[i])):
    #         f.write(str(mat[i][j]) + ", ")
    #         real = mat[i][j].real
    #         imag = mat[i][j].imag
    #         magnitude = np.sqrt(real * real + imag * imag)
    #         intensity = getIntensity(mat[i][j], 256)
    #         mag.write(str(magnitude) + ", ")
    #         db.write(str(intensity) +  ", ")
    #     f.write("\n")
    #     mag.write("\n")
    #     db.write("\n")
