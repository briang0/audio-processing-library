import numpy as np

class complex_num:
    real = 0.0
    imag = 0.0

    def __init__(self, real, complex = None):
        self.real = real
        if complex is None:
            self.imag = 0
        else:
            self.imag = complex

    def __call__(self,realVal):
        self.real = realVal
        self.imag = imgVal

    def add(self, c):
        real1 = self.real + c.real
        imag1 = self.imag + c.imag
        return complex_num(real1, imag1)

    def sub(self, c):
        real1 = self.real - c.real
        imag1 = self.imag - c.imag
        return complex_num(real1, imag1)

    def mult(self, c):
        real1 = self.real * c.real - self.imag * c.imag
        imag1 = self.real * c.imag + self.imag * c.real
        return complex_num(real1, imag1)

    def abs(self, c):
        real1 = abs(real)
        iamg1 = abs(imag)
        return complex_num(real, imag)

    def scale(self, scalar):
        return complex_num(self.real * scalar, self.imag * scalar)

    def getPhase(self):
        real = self.real
        imag = self.imag
        return np.arctan2(imag, real)

    def getConj(self):
        real = self.real
        imag = -1 * self.imag
        return complex_num(real, imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"
