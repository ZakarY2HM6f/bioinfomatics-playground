from typing import Self
from enum import Enum

allowedDnaNeucleotides = "ATCG"
allowedRnaNeucleotides = "AUCG"

complementTable = str.maketrans("ACGT", "TGCA")

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
                raise Exception()

        self = seq

    def complemented(self) -> Self:
        return self.translate(complementTable)[::-1]

    def transcribed(self) -> Self:
        assert(self.type == SeqType.DNA)
        new = self.replace('T', 'U')
        new.type = SeqType.RNA
        return new
