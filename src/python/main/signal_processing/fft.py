import os, sys
sys.path.insert(0, os.path.abspath(".."))
import python.main.math.complex_num as cmplx
import numpy as np

max16bit = 32768

def fft(vec):
    N = len(vec)
    return fft_cmplx(vec)

def fft_cmplx(vec):
    N = len(vec)

    if N == 1:
        return [vec[0]]

    fftEvens = []
    fftOdds = []
    output = [0] * N

    for i in range(0, N // 2):
        fftEvens.append(vec[2 * i])
    fftEvens = fft(fftEvens)

    for i in range(0, N // 2):
        fftOdds.append(vec[2 * i + 1])
    fftOdds = fft(fftOdds)

    T = 0

    for k in range(0, N // 2):
        exp = cmplx.complex_num(np.cos(-2 * np.pi * k / N), np.sin(-2 * np.pi * k / N))
        product = exp.mult(fftOdds[k])
        output[k] = (fftEvens[k].add(product))
        output[k + N // 2] = (fftEvens[k].sub(product))
    return output

def ifft(vec):
    N = len(vec)
    output = vec.copy()

    for i in range(0, N):
        output[i] = vec[i].conj()
    output = fft(output)

    for i in range(0, N):
        output[i] = output[i].conj().scale(1 / N)

    return output

def fft_mat(mat):
    out = []
    for vec in mat:
        out.append(fft(vec))
    return out

def matrixToCSV(mat, outputDir):
    f = open(outputDir+".csv", 'w')
    mag = open(outputDir + "mag.csv", 'w')
    db = open(outputDir + "db.csv", "w")
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            f.write(str(mat[i][j]) + ", ")
            real = mat[i][j].real
            imag = mat[i][j].imag
            magnitude = np.sqrt(real * real + imag * imag)
            intensity = getIntensity(mat[i][j], 256)
            mag.write(str(magnitude) + ", ")
            db.write(str(intensity) +  ", ")
        f.write("\n")
        mag.write("\n")
        db.write("\n")
