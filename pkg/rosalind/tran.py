from ..common import *

transitions = {
    'A': 'G',
    'C': 'T',
    'T': 'C',
    'G': 'A',
}

transversions = {
    'A': ['C', 'T'],
    'C': ['A', 'G'],
    'T': ['A', 'G'],
    'G': ['C', 'T'],
}

def main():
    data = readFasta(getProblemPath(__file__))

    transition = 0
    transversion = 0
    for a, b in zip(*data.values()):
        if a == b:
            continue
        if transitions[a] == b:
            transition += 1
        if a in transversions[b]:
            transversion += 1

    ratio = transition / transversion
    rprint(ratio)
    copyResult()
