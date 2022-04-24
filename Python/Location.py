from itertools import combinations
import random
import math
import copy
from AdjacenceMatrix import *

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

def cluster_distance(locations1: list, locations2: list) -> float:
    d = distance(locations1[0], locations2[0])
    for l in locations1:
        for g in locations2:
            d = min(d, distance(l, g))
    return d

def closest_elements(locations1: list, locations2: list) -> tuple:
    t = (locations1[0], locations2[0])
    d = distance(locations1[0], locations2[0])
    for l in locations1:
        for g in locations2:
            if d > distance(l, g):
                d = distance(l, g)
                t = (l, g)
    d = min(distance(l,g) for l in locations1 for g in locations2)
    return t

def diameter(locations: list) -> float:
    if len(locations) == 1:
        return 0
    comb = list(combinations(locations, 2))
    ds = [distance(c[0], c[1]) for c in comb]
    return max(ds)

def clustering_distances(locations: list) -> list:
    loc = copy.copy(locations)
    clus = [loc[0]]
    loc.remove(loc[0])
    distances = []
    while loc:
        t = closest_elements(clus, loc)
        clus.append(t[1])
        loc.remove(t[1])
        distances.append(distance(t[0], t[1]))
    distances.sort()
    return distances

def center(coll: list) -> Location:
    return Location(sum(x.latitude for x in coll)/len(coll), sum(x.longitude for x in coll)/len(coll))


def overlaps(coll) -> bool:
    a = [True for i in coll for j in coll if cluster_distance(i, j) == 0]
    return bool(a)

def merge_overlapping_sets(lsts):
    repeat = True
    while repeat:
        repeat = False
        for c in lsts:
            for e in c:
                r = [l for l in lsts if e in l]
                if len(r) > 1:
                    for m in r:
                        lsts.remove(m)
                    tt = [el for sublist in r for el in sublist]
                    lsts.append(tt)
                    repeat = True
                    break
            if repeat:
                break


def splitting(coll, n) -> list:
        stair = clustering_distances(copy.copy(coll))
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
        merge_overlapping_sets(lsts)
        if len(lsts) != n:
            raise ValueError(f"The splitting produced {len(lsts)} instead of {n}\nThe collections are\n{lsts}")
        return lsts

def clustering(coll, n) -> list:
    strt = random.choices(coll, k= n)
    clusters = []
    for i in range(4):
        clusters = [[e] for e in strt]
        for e in coll:
            min(clusters, key=lambda x: cluster_distance([e], x)).append(e)
        if i > 0:
            for index, c in enumerate(strt):
                clusters[index].remove(c)
                if len(clusters[index]) == 0:
                    raise ValueError(f"removed last element {c} from one collection {clusters}")
        strt = [center(cluster) for cluster in clusters]
    return clusters
