from ..common import *
import itertools

def main():
    data = readFasta(getProblemPath(__file__))
    assert(len(data) > 1)

    data = list(data.values())
    s = DNASeq(data.pop(0))
    introns = [ DNASeq(s) for s in data ]

    for intron in introns:
        s = s.removeIntron(intron)

    proteins = itertools.chain(*[findProteins(frame) for frame in genReadingFrames(s.translated())])
    result = ''
    for protein in proteins:
        if len(protein) > len(result):
            result = protein
    
    rprint(result)
    copyResult()
    

    