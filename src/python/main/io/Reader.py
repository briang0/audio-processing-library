from src.python.main.util import Formatter


def read_cmplx_matrix_from_csv(output_dir):
    f = open(output_dir)
    data = f.read()
    rows = data.split("\n")
    output = []

    for i in range(0, len(rows) - 1):
        elems = rows[i].split(",")
        output.append([])
        for j in range(0, len(elems) - 1):
            cmplx_str = elems[j]
            num = Formatter.string_to_complex_num(cmplx_str)
            output[i].append(num)
    f.close()
    return output
