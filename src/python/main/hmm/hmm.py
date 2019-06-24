import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.util.matrix_util as matutil

def forward(A, B, pi, O):
    N = len(A)
    T = len(O)
    alpha = []
    for i in range(0, N):
        alpha.append([])
        alpha[i][0].append(pi[i] * B[i][O[0]]
    for t in range(0, T):
        for j in range(0, N):
            alpha[j][t] += alpha[i][t - 1] * A[j][i]
        alpha[j][t] *= B[j][O[t]]
    return alpha

def forward_backward(A, B, pi, O):
    N = len(A)
    T = len(O)
    alpha = forward(A, B, pi, O)
    beta = []
    for i in range(0 , N):
        beta.append([])
        beta[i] = [0] * T
        beta[i][T - 1] = 1

    for t in range(T-2, 0, -1):
        for j in range(0, N):
            for i in range(0, N):
                beta[j][t] += beta[j][t + 1] * A[j][i] * B[i][O[t + 1]]

    return beta
