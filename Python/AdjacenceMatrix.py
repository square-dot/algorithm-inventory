from Location import *


class AdjacenceMatrix:
    def __init__(self, collection, mapping):
        self.c = {}
        for e in collection:
            for d in collection:
                self.c[(e, d)] = mapping(e, d)
        self.elements = collection
        print(f"Created adjacence matrix from {self.nrelements()} elements")
        print(self.__str__())

    def __str__(self) -> str:
        s = "\t"
        for el in self.elements:
            s += f"{el}" + "\t"
        s += "\n"
        for el in self.elements:
            s += f"{el}" + "\t"
            for le in self.elements:
                s += "{:.1f}".format(self.get(el, le)) + "\t"
            s += "\n"
        return s

    def get(self, a, b):
        if (a, b) not in self.c.keys():
            print(f'{(a, b).__str__()} not found')
        return self.c[(a, b)]
    
    def nrelements(self):
        return len(self.elements)



