def write_cmplx_matrix_to_csv(mat, output_dir):
    f = open(output_dir, 'w+')
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            f.write(str(mat[i][j]) + ",")
        f.write("\n")
    f.close()
