from .sequence import *

def genReadingFrames(seq: DNASeq | RNASeq) -> list[AASeq]:
    Seq = type(seq)
    f1 = seq.translated()
    f2 = Seq(seq[1:], True).translated()
    f3 = Seq(seq[2:], True).translated()
    qes = seq.complemented()
    r1 = qes.translated()
    r2 = Seq(qes[1:], True).translated()
    r3 = Seq(qes[2:], True).translated()
    return [f1, f2, f3, r1, r2, r3]

def findProtein(seq: AASeq) -> list[AASeq]:
    currents = []
    proteins = []
    for aa in seq:
        if aa == '_'and currents:
            proteins.extend([AASeq(c, True, True) for c in currents])
            currents.clear()
        else:
            if aa == 'M':
                currents.append('')
            if currents:
                for i in range(len(currents)):
                    currents[i] += aa
                
    return proteins
