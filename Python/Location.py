import random
import math


class Location:
    def __init__(self, lati, longi):
        self.latitude = lati
        self.longitude = longi

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"[{self.latitude} : {self.longitude}]"

    def __eq__(self, obj):
        return isinstance(obj, Location) and obj.latitude == self.latitude and obj.longitude == self.longitude 

    def __hash__(self) -> int:
        return self.latitude + self.longitude * 10000000

def generate(n):
    locs = []
    for _ in range(n):
        longi = random.randint(0, 1000)
        lati = random.randint(0, 1000)
        locs.append(Location(lati, longi))
    return locs


def distance(location1, location2):
    longi = location1.longitude - location2.longitude
    lati = location1.latitude - location2.latitude
    return math.sqrt(lati**2 + longi**2)


def test():
    print(generate(5))
