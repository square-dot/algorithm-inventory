import math
import unittest
import random

from AdjacenceMatrix import *
from Location import *
from TravelingSalesman import *


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
        locations = LocationsLists.list(4)[:15]
        random.shuffle(locations)
        res = divide_et_impera(locations)
        print(f"\nResult divide et impera:\n{res}")
        print(f"Total lenght {pathlength(res)}")


if __name__ == "__main__":
    unittest.main()
