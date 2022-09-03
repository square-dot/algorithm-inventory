from cmath import cos, pi, sin

from Polynomial import *


def uroot(n, k) -> complex:
    theta = 2*pi/n
    return complex(cos(theta*k), sin(theta*k))


def squarerootpoints(polynomial: Polynomial, n):
    sqroots = [polynomial.evaluate(uroot(n, k)) for k in range(n)]
    return sqroots

def degree2n(polynomial: Polynomial):
    v = [2**n for n in range(0, 16)]
    m = min([l for l in v if l >= len(polynomial.coefficients)])
    return m

def fft(polynomial: Polynomial, is_for_inverse = False) -> list[complex]:
    n = len(polynomial.coefficients)
    assert n in [2**n for n in range(20)]
    if n == 1:
        return [polynomial.coefficients[0]]
    evaluations = [complex(0,0)] * n
    odd = Polynomial(coefficients= [c for i,c in enumerate(polynomial.coefficients) if i%2 == 1])
    even = Polynomial(coefficients= [c for i,c in enumerate(polynomial.coefficients) if i%2 == 0])
    assert len(odd.coefficients) == n // 2 & len(even.coefficients) == n // 2
    evaluation_odd = fft(odd, is_for_inverse)
    evaluation_even = fft(even, is_for_inverse)
    for k in range(n // 2):
        assert len(evaluation_even) == n // 2, f"Error claiming {len(evaluation_even)} is equal to {n // 2}"
        assert len(evaluation_odd) == n // 2, f"Error claiming {len(evaluation_odd)} is equal to {n // 2}"
        a = -1 if is_for_inverse else 1
        evaluations[k] = evaluation_even[k] + uroot(n, a * k) * evaluation_odd[k]
        evaluations[k + n // 2] = evaluation_even[k] - uroot(n, a * k) * evaluation_odd[k]
    return evaluations

def inversefft(polynomial: Polynomial) -> list[complex]:
    deg = len(polynomial.coefficients)
    res = fft(polynomial, is_for_inverse=True)
    return [c / deg for c in res]


def multiplywithfft(poly1: Polynomial, poly2: Polynomial):
    deg = max(degree2n(poly1), degree2n(poly2)) * 2
    c1 = [poly1.coefficients[i] if i < len(poly1.coefficients) else 0 for i in range(deg)]
    c2 = [poly2.coefficients[i] if i < len(poly2.coefficients) else 0 for i in range(deg)]
    values1 = fft(Polynomial(c1))
    values2 = fft(Polynomial(c2))
    endvalues = [a[0] * a[1] for a in zip(values1, values2)]
    coefficients = inversefft(Polynomial(endvalues))
    return Polynomial(coefficients)


