import collections

NUCLEOTIDES = ['A', 'C', 'G', 'T']

def validateSeq(seq: str) -> bool:
    for b in seq:
        if b not in NUCLEOTIDES:
            return False
    return True

def readSeqFromFile(path: str) -> str:
    with open(path, 'r') as f:
        seq = f.read().strip().upper()
        assert(validateSeq(seq))
        return seq
