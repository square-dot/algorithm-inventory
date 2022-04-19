import itertools

from Location import *


def distances(locations):
    return sum(distance(locations[i], locations[i + 1]) for i in range(len(locations) - 1))


def brute_force(locations):
    permutations = itertools.permutations(locations)
    return min(distances(it) for it in permutations)


def test(n):
    locations = generate(n)
    print(locations)
    return brute_force(locations)

print(test(9))
