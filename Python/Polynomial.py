
class Polynomial:
    def __init__(self, coefficients: list):
        self.coefficients = coefficients

    def __str__(self):
        return self.coefficients.__str__()

    def __repr__(self):
        return f"Coefficients {self.coefficients}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Polynomial):
            if len(self.coefficients) >= len(other.coefficients):
                a = self
                b = other
            else:
                a = other
                b = self
            for i,c in enumerate(a.coefficients):
                if i < len(b.coefficients):
                    if c != b.coefficients[i]:
                        return False
                else:
                    if c != 0:
                        return False
            return True
            
        return False
    
    def multiply(self, polynomial):  # sourcery skip: use-itertools-product
        total_coefficients = [0 for _ in range(len(self.coefficients) + len(polynomial.coefficients) - 1)]
        for idx, val in enumerate(self.coefficients):
            for i, v in enumerate(polynomial.coefficients):
                total_coefficients[idx + i] += val * v
        return Polynomial(total_coefficients)

    def evaluate(self, x):
        return sum(self.coefficients[l] * x**l for l in range(len(self.coefficients)))
        