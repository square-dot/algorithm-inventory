from cmath import exp, pi



class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        return self.coefficients.__str__()
    
    def multiply(self, polynomial):  # sourcery skip: use-itertools-product
        total_coefficients = [0 for _ in range(len(self.coefficients) + len(polynomial.coefficients) - 1)]
        for idx, val in enumerate(self.coefficients):
            for i, v in enumerate(polynomial.coefficients):
                total_coefficients[idx + i] += val * v
        return Polynomial(total_coefficients)

    def evaluate(self, x):
        return sum(self.coefficients[l] * x**l for l in range(len(self.coefficients)))

    def squarerootpoints(self, n):
        sqroots = [self.evaluate(exp(2*pi*complex(0, 1)/n)) for _ in range(n)]


def test(n, m):
    poly1 = Polynomial(range(1, n))
    poly2 = Polynomial(range(1, m))
    res = poly1.multiply(poly2)
    print(res.evaluate(1))

test(6000, 4000)


