import unittest

from AdjacenceMatrix import *
from Location import *


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
        self.assertEqual(am.get(Location(3, 1), Location(0, 1)), 5)

    def test_splitting(self):
        locations = [
            Location(0, 0),
            Location(0, 1),
            Location(3, 10),
            Location(8, 12),
            Location(10, 100),
            Location(100, 200),
        ]
        am = AdjacenceMatrix(locations, distance)
        spl = am.splitting(5)
        self.assertEqual(len(spl), 3)

if __name__ == '__main__':
    unittest.main()
