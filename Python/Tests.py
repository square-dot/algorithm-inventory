import math
import unittest

from AdjacenceMatrix import *
from Location import *
from TravelingSalesman import *


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

    def test_clustering_distances(self):
        locations = [
            Location(3, 1),
            Location(0, 1),
            Location(3, 10),
        ]
        c = clustering_distances(locations)
        print(f"Clustering distances are {c}")

    def test_splitting(self):
        locations = [
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
        sn = 7
        spl = splitting(locations, sn)
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
        locations = generate(9)
        return brute_force(locations)

    def test2(self):
        print("\nRunning test 2\n")
        locations = generate(9)
        print("The locations are")
        print(locations)
        return divide_et_impera(locations)


if __name__ == '__main__':
    unittest.main()
