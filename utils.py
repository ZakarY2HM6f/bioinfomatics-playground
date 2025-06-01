import collections

NUCLEOTIDES = ['A', 'C', 'G', 'T']

def validateSeq(seq: str):
    seq = seq.upper()
    for b in seq:
        if b not in NUCLEOTIDES:
            return False
    return True
