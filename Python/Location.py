import random
import math

class Location:
    def __init__(self, longi, lati):
        self.longitude = longi
        self.latitude = lati

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"[{self.longitude} : {self.latitude}]"

def generate(n):
    locs = []
    for _ in range(n):
        longi = random.randint(0, 1000)
        lati = random.randint(0, 1000)
        locs.append(Location(longi, lati))
    return locs

def distance(location1, location2):
    longi = location1.longitude - location2.longitude
    lati = location1.latitude - location2.latitude
    return math.sqrt(longi ** 2 + lati ** 2)


def test():
    print(generate(5))


