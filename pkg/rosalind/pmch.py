import math
from collections import Counter
from ..common import *

def main():
    _, seq = readFasta(getProblemPath(__file__)).popitem()

    counts = Counter(seq)
    assert(counts['A'] == counts['U'])
    assert(counts['C'] == counts['G'])

    auPairs = math.factorial(counts['A'])
    cgPairs = math.factorial(counts['C'])

    p = auPairs * cgPairs

    print(p)
