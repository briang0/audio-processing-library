
def vec_to_mat(vec, cols):
    mat = []
    cur_element = 0
    length = len(vec)
    num_rows = length // cols
    for i in range(0, num_rows):
        mat.append([])
        for j in range(0, cols):
            if (cur_element < length):
                mat[i].append(vec[cur_element])
            else:
                mat[i].append(0)
            cur_element += 1
    return mat
