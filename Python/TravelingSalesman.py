import itertools
from AdjacenceMatrix import *
from Location import *


max_brute_force = 8

def pathlength(locations):
    return sum(distance(locations[i], locations[i + 1]) for i in range(len(locations) - 1))


def brute_force(locations):
    permutations = itertools.permutations(locations)
    return min(permutations, key=pathlength)


def divide_et_impera(locations):
    return []
    still_to_improve = True
    trials= []
    setsnr = math.floor(len(locations) / max_brute_force)
    while still_to_improve & len(trials) < 5:
        lsts = clustering(locations, setsnr)
        if max(len(c) for c in lsts) <= max_brute_force:
            still_to_improve = False
        else:
            setsnr += 1
        trials.append(lsts)
    selected_clustering = min([t for t in trials if max(len(c) for c in t) <= max_brute_force], key=lambda x: pathlength(brute_force(x)))
    paths = [brute_force(l) for l in selected_clustering]
    permutations = list(itertools.permutations(paths))
    permutation = min(permutations, key=lambda x: sum(distance(x[i][-1],x[i+1][0]) for i in range(setsnr - 1)))
    path = []
    for p in permutation:
        path += p
    return path
