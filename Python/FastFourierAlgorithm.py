from Polynomial import *

def FFT(poly1: Polynomial, poly2: Polynomial):
    deg1 = poly1.degree2n() * 2
    deg2 = poly2.degree2n()*2
    finaldeg = min(deg1, deg2)
    evaluation1 = poly1.squarerootpoints(finaldeg)
    evaluation2 = poly2.squarerootpoints(finaldeg)
    multiplication = list(a[0] * a[1] for a in zip(evaluation1, evaluation2))
