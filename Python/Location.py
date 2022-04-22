from itertools import combinations
import random
import math
import copy
import sys

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

def cluster_distance(locations1, locations2):
    d = distance(locations1[0], locations2[0])
    for l in locations1:
        for g in locations2:
            d = min(d, distance(l, g))
    return d

def closest_elements(locations1, locations2):
    t = (locations1[0], locations2[0])
    d = distance(locations1[0], locations2[0])
    for l in locations1:
        for g in locations2:
            if d > distance(l, g):
                d = distance(l, g)
                t = (l, g)
    return t

def diameter(locations):
    if len(locations) == 1:
        return 0
    comb = list(combinations(locations, 2))
    ds = [distance(c[0], c[1]) for c in comb]
    return max(ds)

def clustering_distances(locations) -> list:
    loc = copy.copy(locations)
    clus = [loc[0]]
    loc.remove(loc[0])
    distances = []
    while loc:
        t = closest_elements(clus, loc)
        clus.append(t[1])
        loc.remove(t[1])
        distances.append(distance(t[0], t[1]))
    return distances


def splitting(coll, n) -> list:
        stair = sorted(clustering_distances(copy.copy(coll)))
        dis = stair[- n + 1]
        lsts = [[coll[0]]]
        for a in coll[1:]:
            appended = False
            for e in lsts:
                if cluster_distance([a], e) < dis:
                    e.append(a)
                    appended = True
            if not appended:
                lsts.append([a])
        if len(lsts) != n:
            raise ValueError(f"The splitting produced {len(lsts)} instead of {n}")
        return lsts
