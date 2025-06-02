from typing import Self
from enum import Enum

allowedDnaNeucleotides = "ATCG"
allowedRnaNeucleotides = "AUCG"

complementTable = str.maketrans("ACGT", "TGCA")

class SeqType(Enum):
    DNA = 'd'
    RNA = 'r'

class Sequence(str):
    def __init__(self, type=SeqType.DNA):
        self.type = type
        match type:
            case SeqType.DNA:
                allowed = allowedDnaNeucleotides
                
            case SeqType.RNA:
                allowed = allowedRnaNeucleotides
            case _:
                raise Exception()

        for base in self:
            if base not in allowed:
                raise Exception()

    def complemented(self) -> Self:
        return self.translate(complementTable)[::-1]

    def transcribed(self) -> Self:
        assert(self.type == SeqType.DNA)
        self.type = SeqType.RNA
        return self.replace('T', 'U')
