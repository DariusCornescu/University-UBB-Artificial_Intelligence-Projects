import math
import cmath


class Polynom:
    def __init__(self, degree, coefficients):
        self.__degree = degree
        self.__coefficients = coefficients

    def get_derivative(self):
        new_degree = self.__degree - 1
        new_coefficients = [0] * (new_degree + 1)
        for index in range(len(new_coefficients)):
            new_coefficients[index] = (index + 1) * self.__coefficients[index + 1]
        return Polynom(new_degree, new_coefficients)

    def get_degree(self):
        return self.__degree

    def get_coefficients(self):
        return self.__coefficients

    def eval(self, x):
        rez = 0
        term = 1
        for index in range(self.__degree + 1):
            rez += self.__coefficients[index] * term
            term *= x
        return rez

    def __str__(self):
        terms = []
        for index, coef in enumerate(self.__coefficients):
            terms.append(f"{coef}*x^{index}")
        return " + ".join(terms)


class Matrix:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__content = [[0] * columns for _ in range(rows)]

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns


def newton_method(polynom, a, b, epsilon, max_iterations=1000):
    x = b
    derivative = polynom.get_derivative()
    val_x = polynom.eval(x)
    val_derivative_x = derivative.eval(x)
    iteration = 0

    while abs(val_x) > epsilon and iteration < max_iterations:
        x -= val_x / val_derivative_x
        val_x = polynom.eval(x)
        val_derivative_x = derivative.eval(x)
        iteration += 1

    if iteration == max_iterations:
        raise Exception("Newton's method did not converge")

    return x


def FFT(P):
    n = P.get_degree() + 1
    if n <= 1:
        return P
    if n & (n - 1) != 0:
        raise ValueError("The degree of the polynomial must be one less than a power of 2")

    omega = cmath.exp(2j * math.pi / n)
    omega_j = 1
    coefficients_pe = P.get_coefficients()[::2]
    coefficients_po = P.get_coefficients()[1::2]
    Pe = Polynom(len(coefficients_pe) - 1, coefficients_pe)
    Po = Polynom(len(coefficients_po) - 1, coefficients_po)
    ye = FFT(Pe).get_coefficients()
    yo = FFT(Po).get_coefficients()
    y = [0] * n
    for j in range(n // 2):
        y[j] = ye[j] + omega_j * yo[j]
        y[j + n // 2] = ye[j] - omega_j * yo[j]
        omega_j *= omega
    return Polynom(n - 1, y)


class Tests:
    def __run_polynom_test(self):
        print("Starting polynom test!")
        degree = 7
        coefficients = [-0.2, -3, 0, 17, -4, 0, 0, 5]
        polynom = Polynom(degree, coefficients)

        expected_degree = 6
        expected_coefficients = [-3, 0, 51, -16, 0, 0, 35]

        obtained_derivative = polynom.get_derivative()

        assert expected_degree == obtained_derivative.get_degree()
        assert expected_coefficients == obtained_derivative.get_coefficients()

        epsilon = 0.0001
        expected_zero = 0.4721155
        obtained_zero = newton_method(polynom, 0.4, 0.6, epsilon)
        assert abs(expected_zero - obtained_zero) < epsilon

        print("FFT of the polynomial:")
        fft_result = FFT(polynom)
        print(fft_result)

        print("Test polynom finished successfully!")

    def __run_matrix_test(self):
        print("Start matrix test")
        matrix = Matrix(3, 4)
        assert matrix.get_rows() == 3
        assert matrix.get_columns() == 4
        print("Matrix test finished successfully!")

    def run_all_tests(self):
        self.__run_polynom_test()
        self.__run_matrix_test()


if __name__ == "__main__":
    test = Tests()
    test.run_all_tests()
