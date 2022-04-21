import itertools
from AdjacenceMatrix import *
from Location import *


def pathlength(locations):
    return sum(distance(locations[i], locations[i + 1]) for i in range(len(locations) - 1))


def brute_force(locations):
    permutations = itertools.permutations(locations)
    return min(pathlength(it) for it in permutations)


def divide_et_impera(locations):
    lsts = splitting(locations, 3)
    tot = sum(pathlength(l) for l in lsts)
    permutations = list(itertools.permutations(lsts))
    minimalconnections = sum(distance(l, Location(0,0)) for l in locations)
    for permu in permutations:
        tot = 0
        for i in range(len(permu) - 1):
            tot += cluster_distance(permu[i], permu[i+1])
            tot += diameter(permu[i])
        minimalconnections = min(tot, minimalconnections)
    return tot

