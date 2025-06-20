from ..common import *


def main():
    with open(getProblemPath(__file__), "r") as f:
        data = f.read().strip().split(" ")
    assert len(data) == 2
    [n, m] = [int(s) for s in data]

    # (old, new)
    population = [(0, 0) for _ in range(m)] + [(0, 1)]
    for _ in range(n - 1):
        old = sum(population[-1]) - population[-m][1]
        new = population[-1][0]
        population.append((old, new))
        population.pop(0)

    print(population)
    rprint(sum(population[-1]))
    copyResult()
