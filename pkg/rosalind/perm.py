import math
from ..common import *


def main():
    with open(getProblemPath(__file__), "r") as f:
        n = int(f.read().strip())

    t = math.perm(n, n)
    rprint(t)

    results = [[i] for i in range(1, n + 1)]

    def walk_mut(tree, unused=None):
        if unused == None:
            unused = [i for i in range(1, n + 1)]
        if len(unused) == 0:
            return

        if isinstance(tree[0], int):
            unused.remove(tree[0])
            if len(unused) == 0:
                return

            tree.append([[u] for u in unused])
            walk_mut(tree[1], unused.copy())
        else:
            for node in tree:
                walk_mut(node, unused.copy())

    walk_mut(results)
    print(results)

    def walk_print(tree, p=""):
        if isinstance(tree[0], int):
            p += str(tree[0]) + " "

            if len(tree) == 2:
                walk_print(tree[1], str(p))
            else:
                rprint(p)
        else:
            for node in tree:
                walk_print(node, str(p))

    walk_print(results)
    copyResult()
