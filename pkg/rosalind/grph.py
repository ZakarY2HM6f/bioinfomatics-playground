from ..common.utils import *

k = 3

def main():
    data = readFasta(getDataPath(__file__))
    graph = []

    for i1, s in data.items():
        for i2, t in data.items():
            if i2 == i1:
                continue
            if s[-3:] == t[0:3]:
                graph.append((i2, i1))

    for edge in graph:
        print(f"{edge[1]} {edge[0]}")
