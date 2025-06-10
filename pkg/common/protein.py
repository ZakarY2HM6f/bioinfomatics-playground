from .sequence import *

def genReadingFrames(seq: DNASeq | RNASeq) -> list[AASeq]:
    Seq = type(seq)
    f1 = seq.translated()
    f2 = Seq(seq[1:], True).translated()
    f3 = Seq(seq[2:], True).translated()
    r1 = seq.complemented().translated()
    r2 = Seq(r1[1:], True).translated()
    r3 = Seq(r1[2:], True).translated()
    return [f1, f2, f3, r1, r2, r3]

def findProtein(seq: AASeq) -> list[AASeq]:
    currents = []
    proteins = []
    for aa in seq:
        match aa:
            case 'M':
                currents.append('M')
            case '_':
                if currents:
                    proteins.extend([AASeq(c, True, True) for c in currents])
                    currents.clear()
            case _:
                if currents:
                    for i in range(len(currents)):
                        currents[i] += aa
    return proteins
