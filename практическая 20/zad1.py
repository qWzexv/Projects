import math


class Complex:
    def __init__(self, real, imag):
        self.R = real
        self.M = imag

    def __add__(self, other):
        return Complex(self.R + other.R, self.M + other.M)

    def __sub__(self, other):
        return Complex(self.R - other.R, self.M - other.M)

    def __mul__(self, other):
        real = self.R * other.R - self.M * other.M
        imag = self.R * other.M + self.M * other.R
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.R ** 2 + other.M ** 2
        real = (self.R * other.R + self.M * other.M) / denom
        imag = (self.M * other.R - self.R * other.M) / denom
        return Complex(real, imag)

    def modulus(self):
        return math.sqrt(self.R ** 2 + self.M ** 2)

    def power(self, n):
        if n == 0:
            return Complex(1, 0)
        result = Complex(self.R, self.M)
        for _ in range(1, n):
            result = result * Complex(self.R, self.M)
        return result

    def __repr__(self):
        return f"{self.R} + {self.M}i"


z1 = Complex(3, 4)
z2 = Complex(1, 2)


def modum(A):
    C = []
    for i in range(len(A) - 1):
        sum_complex = A[i] + A[i + 1]
        C.append(sum_complex.modulus())
    return C


A = [Complex(3, 4), Complex(1, 2), Complex(5, 6), Complex(7, 8)]
C = modum(A)
print("Модуль сумм рядом стоящих чисел:", C)


def power(A, M):
    matrix = []
    for i in range(M):
        row = []
        for j in range(M):
            row.append(A[i].power(j + 1))
        matrix.append(row)
    return matrix


M = 4
A = [Complex(1, 1), Complex(2, 3), Complex(3, 2), Complex(4, 1)]
matrix = power(A, M)
print("Матрица с результатами возведения в степень:")
for row in matrix:
    print([repr(z) for z in row])