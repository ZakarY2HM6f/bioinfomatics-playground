from ..common import *

def main():
    data = readFile(getProblemPath(__file__))
    seq = RNASeq(data)
    seq = seq.translated()

    print(seq[:-1])
