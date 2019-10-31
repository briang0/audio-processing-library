class ComplexNum:
    real = 0.0
    imag = 0.0

    def __init__(self, real, complex_part=None):
        self.real = real
        if complex_part is None:
            self.imag = 0
        else:
            self.imag = complex_part

    def __call__(self, real_val):
        self.real = real_val
        self.imag = 0

    def add(self, c):
        real1 = self.real + c.real
        imag1 = self.imag + c.imag
        return ComplexNum(real1, imag1)

    def sub(self, c):
        real1 = self.real - c.real
        imag1 = self.imag - c.imag
        return ComplexNum(real1, imag1)

    def mult(self, c):
        real1 = self.real * c.real - self.imag * c.imag
        imag1 = self.real * c.imag + self.imag * c.real
        return ComplexNum(real1, imag1)

    def abs(self):
        real1 = abs(self.real)
        imag1 = abs(self.imag)
        return ComplexNum(real1, imag1)

    def round(self):
        real1 = round(self.real)
        imag1 = round(self.imag)
        return ComplexNum(real1, imag1)

    def scale(self, scalar):
        return ComplexNum(self.real * scalar, self.imag * scalar)

    def conj(self):
        return ComplexNum(self.real, -1 * self.imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)
