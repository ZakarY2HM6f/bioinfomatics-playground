from ..common import *
import itertools

def main():
    data = readFasta(getProblemPath(__file__))
    s = data.values().__iter__().__next__()
    s = DNASeq(s)

    proteins = itertools.chain(*(findProteins(frame) for frame in genReadingFrames(s)))
    for p in proteins:
        rprint(p)

    copyResult()
