from typing import Self
from enum import Enum

allowedDnaNeucleotides = "ATCG"
allowedRnaNeucleotides = "AUCG"

dnaComplementTable = str.maketrans("ACGT", "TGCA")
rnaComplementTable = str.maketrans("ACGU", "UGCA")

dnaCondons = {
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

class SeqType(Enum):
    DNA = 'd'
    RNA = 'r'

class Sequence(str):
    def __init__(self, seq, type=SeqType.DNA):
        match type:
            case SeqType.DNA:
                allowed = allowedDnaNeucleotides
            case SeqType.RNA:
                allowed = allowedRnaNeucleotides
            case _:
                raise Exception()

        self.type = type

        for base in self:
            if base not in allowed:
                raise Exception("Invalid character in sequence")

        self = seq

    def complemented(self) -> Self:
        match self.type:
            case SeqType.DNA:
                return self.translate(dnaComplementTable)[::-1]
            case SeqType.RNA:
                return self.translate(rnaComplementTable)[::-1]
            case _:
                raise Exception("Invalid Sequence type")

    def transcribed(self) -> Self:
        assert(self.type == SeqType.DNA)
        new = Sequence(self.replace('T', 'U'))
        new.type = SeqType.RNA
        return new
