from math import Complex as cmplx

def getIntensity(complex, FFTSize):
    real = complex.real
    imag = complex.imag
    magnitude = np.sqrt(real * real + imag * imag)
    intensity = -20 * np.log10(magnitude/max16bit)
    return intensity
