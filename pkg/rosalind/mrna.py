from ..common import *

def main():
    codonPerAA = {}
    for _, aa in rnaCodons.items():
        if aa in codonPerAA:
            codonPerAA[aa] += 1
        else:
            codonPerAA[aa] = 1
    
    seq = readFile(getDataPath(__file__))

    p = codonPerAA['_']
    for aa in seq:
        p *= codonPerAA[aa]
        if p > 1000000:
            p %= 1000000
    
    rprint(p)
    copyResult()
