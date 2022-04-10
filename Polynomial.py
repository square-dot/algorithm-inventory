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


def test():
    poly1 = Polynomial([1, 2])
    poly2 = Polynomial([1, 2])
    print(poly1.multiply(poly2))

test()