from typing import Self, NewType, Iterable
from enum import Enum

allowedDnaNeucleotides = "ATCG"
allowedRnaNeucleotides = "AUCG"
allowedProteins = "ACDEFGHIKLMNPQRSTVWY_"

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

rnaCodons = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_",
    "UGU": "C", "UGC": "C",
    "UGG": "w",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "AUG": "M",
    "AAU": "N", "AAC": "N"
}

RNASeq = NewType("RNASeq", None)
ProSeq = NewType("ProSeq", None)

class BaseSeq(str):
    pass

class DNASeq(BaseSeq):
    def __new__(cls, seq: str | Iterable[str], safe=False):
        if isinstance(str, Iterable):
            seq = ''.join(seq)
            
        if not safe:
            for base in seq:
                if base not in allowedDnaNeucleotides:
                    raise Exception(f"Invalid character '{base}' in sequence")

        instance = super().__new__(cls, seq)
        return instance

    def complemented(self) -> Self:
        return DNASeq(self.translate(dnaComplementTable)[::-1], True)

    def transcribed(self) -> RNASeq:
        return RNASeq(self.replace('T', 'U'), True)
    
    def translated(self) -> ProSeq:
        return ProSeq([dnaCondons[self[i*3:i*3+3]] for i in range(0, len(self) // 3)], True)

    
class RNASeq(BaseSeq):
    def __new__(cls, seq: str | Iterable[str], safe=False):
        if isinstance(str, Iterable):
            seq = ''.join(seq)

        if not safe:
            for base in seq:
                if base not in allowedRnaNeucleotides:
                    raise Exception(f"Invalid character '{base}' in sequence")

        instance = super().__new__(cls, seq)
        return instance

    def complemented(self) -> Self:
        return RNASeq(self.translate(rnaComplementTable)[::-1], True)

class ProSeq(BaseSeq):
    def __new__(cls, seq: str | Iterable[str], safe=False):
        if isinstance(str, Iterable):
            seq = ''.join(seq)

        if not safe:
            for ch in seq:
                if ch not in allowedProteins:
                    raise Exception(f"Invalid character '{ch}' in sequence")

        instance = super().__new__(cls, seq)
        return instance
