import itertools
from AdjacenceMatrix import *
from Location import *


def pathlength(locations):
    return sum(distance(locations[i], locations[i + 1]) for i in range(len(locations) - 1))


def brute_force(locations):
    permutations = itertools.permutations(locations)
    return min(permutations, key=pathlength)


def divide_et_impera(locations):
    lsts = splitting(locations, 3)
    tot0 = sum(pathlength(l) for l in lsts)
    permutations = list(itertools.permutations(lsts))
    minimalconnections = sum(distance(l, Location(0,0)) for l in locations)
    for permu in permutations:
        tot1 = 0
        for i in range(len(permu) - 1):
            tot1 += cluster_distance(permu[i], permu[i+1])
            tot1 += diameter(permu[i])
        minimalconnections = min(tot1, minimalconnections)
    tot0 += minimalconnections
    return tot0

def divide_et_impera2(locations):
    setsnr = 3
    lsts = splitting(locations, setsnr)
    paths = [brute_force(l) for l in lsts]
    permutations = list(itertools.permutations(paths))
    permutation = min(permutations, key=lambda x: sum(distance(x[i][-1],x[i+1][0]) for i in range(setsnr - 1)))
    path = []
    for p in permutation:
        path += p
    return path
