import math
import unittest
import random
import time

from AdjacenceMatrix import *
from Location import *
from TravelingSalesman import *

from Polynomial import *
from FastFourierAlgorithm import *


class LocationsLists:
    @staticmethod
    def list(n) -> list:
        match n:
            case 1:
                return [
                    Location(3, 1),
                    Location(0, 1),
                    Location(3, 10),
                ]
            case 2:
                return [
                    Location(30, 1),
                    Location(110, 1),
                    Location(130, 10),
                ]
            case 3:
                return [
                    Location(0, 0),
                    Location(0, 1),
                    Location(3, 10),
                    Location(8, 12),
                    Location(10, 100),
                    Location(11, 100),
                    Location(100, 200),
                    Location(100, 205),
                    Location(120, 207),
                    Location(130, 209),
                    Location(150, 210),
                    Location(300, 220),
                    Location(300, 250),
                ]
            case 4:
                return [
                    Location(0, 0),
                    Location(0, 1),
                    Location(0, 10),
                    Location(0, 83),
                    Location(1, 12),
                    Location(1, 98),
                    Location(2, 45),
                    Location(5, 17),
                    Location(10, 64),
                    Location(12, 40),
                    Location(13, 2),
                    Location(25, 99),
                    Location(28, 32),
                    Location(30, 5),
                    Location(30, 78),
                    Location(45, 12),
                    Location(48, 57),
                    Location(50, 34),
                    Location(53, 111),
                    Location(52, 32),
                    Location(60, 0),
                    Location(72, 32),
                    Location(100, 10),
                    Location(110, 39),
                    Location(112, 80),
                    Location(120, 1),
                    Location(142, 95),
                ]
            case _:
                return []



class TestLocation(unittest.TestCase):
    def test_instantiate_location(self):
        location = Location(3, 1)
        self.assertEqual(location.latitude, 3)
        self.assertEqual(location.longitude, 1)

    def test_equality(self):
        location1 = Location(3, 1)
        location2 = Location(3, 1)
        self.assertEqual(location1, location2)

    def test_distance(self):
        location1 = Location(3, 1)
        location2 = Location(0, 1)
        dist = distance(location1, location2)
        self.assertEqual(dist, 3)

    def test_cluster_distance(self):
        locations1 = LocationsLists.list(1)
        locations2 = LocationsLists.list(2)
        dist = cluster_distance(locations1, locations2)
        self.assertEqual(dist, 27)

    def test_clustering_distances_1(self):
        locations = LocationsLists.list(1)
        c = clustering_distances(locations)
        self.assertEqual(c, [3.0, 9.0])

    def test_clustering_distances_2(self):
        locations = LocationsLists.list(4)
        c = clustering_distances(locations)
        c.sort()
        print(f"clustering distances\n{c}")
        self.assertEqual(c[0], 1)

    def test_splitting_2(self):
        locations = LocationsLists.list(4)
        sn = 2
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_splitting_3(self):
        locations = LocationsLists.list(4)
        sn = 3
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_splitting_4(self):
        locations = LocationsLists.list(4)
        sn = 4
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_splitting_5(self):
        locations = LocationsLists.list(4)
        sn = 5
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_splitting_6(self):
        locations = LocationsLists.list(4)
        sn = 6
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_splitting_7(self):
        locations = LocationsLists.list(4)
        sn = 7
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)
    
    def test_splitting_8(self):
        locations = LocationsLists.list(4)
        sn = 8
        spl = splitting(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_clustering_1(self):
        locations = LocationsLists.list(4)
        sn = 1
        spl = clustering(locations, sn)
        self.assertEqual(len(spl), sn)
    
    def test_clustering_2(self):
        locations = LocationsLists.list(4)
        sn = 2
        spl = clustering(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_clustering_3(self):
        locations = LocationsLists.list(4)
        sn = 3
        spl = clustering(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_clustering_5(self):
        locations = LocationsLists.list(4)
        sn = 5
        spl = clustering(locations, sn)
        self.assertEqual(len(spl), sn)

    def test_clustering_8(self):
        locations = LocationsLists.list(4)
        sn = 8
        spl = clustering(locations, sn)
        self.assertEqual(len(spl), sn)

class TestAdjacenceMatrix(unittest.TestCase):
    def test_instantiate(self):
        locations = [
            Location(3, 1),
            Location(0, 1),
            Location(3, 10),
        ]
        am = AdjacenceMatrix(locations, distance)
        self.assertEqual(am.elements, locations)

    def test_value(self):
        locations = [
            Location(3, 1),
            Location(0, 1),
            Location(3, 10),
            Location(3, 12),
        ]
        am = AdjacenceMatrix(locations, distance)
        self.assertEqual(am.get(Location(3, 1), Location(0, 1)), 3)
        self.assertEqual(am.get(Location(3, 1), Location(3, 10)), 9)
        self.assertEqual(am.get(Location(0, 1), Location(3, 10)), math.sqrt(90))


class TestTravelingSalesman(unittest.TestCase):

    def test_brute_force(self):
        locations = LocationsLists.list(4)[:7]
        random.shuffle(locations)
        res = brute_force(locations)
        print(f"\nResult brute force:\n{res}")
        print(f"Total lenght {pathlength(res)}")

    def test_divide_et_impera(self):
        locations = LocationsLists.list(4)[:8]
        random.shuffle(locations)
        res = divide_et_impera(locations)
        print(f"\nResult divide et impera:\n{res}")
        print(f"Total lenght {pathlength(res)}")


if __name__ == "__main__":
    unittest.main()


class PolynomialTests(unittest.TestCase):
    def test_equality1(self):
        poly1 = Polynomial([1, 2])
        poly2 = Polynomial([1, 2])
        self.assertTrue(poly1 == poly2)
    
    def test_equality2(self):
        poly1 = Polynomial([1, 2, 0])
        poly2 = Polynomial([1, 2])
        self.assertTrue(poly1 == poly2)

    def test_equality3(self):
        poly1 = Polynomial([2, 5, 7, 8])
        poly2 = Polynomial([4, 6, 7, 8])
        self.assertFalse(poly1 == poly2)

    def test_equality4(self):
        poly1 = Polynomial([1, 5])
        poly2 = Polynomial([1, 5, 7, 8])
        self.assertFalse(poly1 == poly2)

    def test_evaluate(self):
        poly = Polynomial([1, 5, 7, 8])
        self.assertTrue(poly.evaluate(2) == 103)

class FastFourierTransform(unittest.TestCase):
    def test_fft(self):
        poly = Polynomial(list(range(1, 9)))
        n = degree2n(poly)
        x_values = [uroot(n, k) for k in range(n)]
        expected = [poly.evaluate(x) for x in x_values]
        obtained = fft(poly)
        for a in zip(expected, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_fft_with_inverse_1(self):
        coefficients = list(range(1, 9))
        poly = Polynomial(coefficients)
        obtained = inversefft(Polynomial(fft(poly)))
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_fft_with_inverse_2(self):
        coefficients = [12.1, 0, -4, 6, 3.67, 9, 0, 3.6]
        poly = Polynomial(coefficients)
        n = degree2n(poly)
        obtained = inversefft(Polynomial(fft(poly)))
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_fft_with_inverse_3(self):
        coefficients = [12.1, 0, 6, 6]
        poly = Polynomial(coefficients)
        obtained = inversefft(Polynomial(fft(poly)))
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

class PolynomialMultiplicaiton(unittest.TestCase):
    def test_correctness_0(self):
        poly1 = Polynomial([1])
        poly2 = Polynomial([1])
        res_fft = multiplywithfft(poly1, poly2)
        coefficients = [1]
        obtained  = res_fft.coefficients      
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])


    def test_correctness_1(self):
        poly1 = Polynomial([1, 2])
        poly2 = Polynomial([1])
        res_fft = multiplywithfft(poly1, poly2)
        coefficients = [1, 2]
        obtained  = res_fft.coefficients      
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_correctness_2(self):
        poly1 = Polynomial([1, 2])
        poly2 = Polynomial([1, 2])
        res_fft = multiplywithfft(poly1, poly2)
        coefficients = [1, 4, 4]
        obtained  = res_fft.coefficients      
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_correctness_3(self):
        poly1 = Polynomial([1, 3, 4])
        poly2 = Polynomial([1, 2])
        res_fft = multiplywithfft(poly1, poly2)
        coefficients = [1, 5, 10, 8]
        obtained  = res_fft.coefficients      
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_correctness_4(self):
        poly1 = Polynomial([2, 5, 7, 8])
        poly2 = Polynomial([4, 6, 7, 8])
        res_bf = poly1.multiply(poly2)
        res_fft = multiplywithfft(poly1, poly2)
        coefficients = res_bf.coefficients 
        obtained  = res_fft.coefficients      
        for a in zip(coefficients, obtained):
            self.assertAlmostEqual(a[0], a[1])

    def test_brute_force(self):
        start_time = time.time()
        poly1 = Polynomial(list(range(1, 1_000)))
        poly2 = Polynomial(list(range(1, 1_000)))
        res = poly1.multiply(poly2)
        print("--- %s seconds for brute force ---" % (time.time() - start_time))
        print(res.evaluate(1))

    def test_fft(self):
        start_time = time.time()
        poly1 = Polynomial(list(range(1, 1_000)))
        poly2 = Polynomial(list(range(1, 1_000)))
        res = multiplywithfft(poly1, poly2)
        print("--- %s seconds for fft ---" % (time.time() - start_time))
        print(res.evaluate(1))
