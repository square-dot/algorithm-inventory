from typing import Tuple
import math


class AdjacenceMatrix:
    def __init__(self, collection, mapping):
        self.c = {}
        for e in collection:
            for d in collection:
                self.c[e, d] = mapping(e, d)
        self.elements = collection
        print(f"Created adjacence matrix from {len(self.elements)} elements")

    def get(self, a, b):
        if [a, b] not in self.c.keys():
            print(f'{[a, b].__str__()} not found')
        return self.c[a, b]
    
    def splitting(self, n):
        stair = sorted(self.c.values())
        dis = stair[len(self.elements) * (len(self.elements) - 1) - n + 1]
        lsts = []
        considered = []
        for a in self.elements:
            if a in considered:
                continue
            this_list = [a]
            considered.append(a)
            for b in self.elements:
                if b in considered:
                    continue
                if self.get(a, b) <= dis:
                    this_list.append(b)
                    considered.append(b)
            lsts.append(this_list)
        print(lsts)
        return lsts



