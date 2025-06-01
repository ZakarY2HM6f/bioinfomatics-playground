import collections
import string

import utils

## Task 1 - Counting DNA bases

with open("problems/rosalind_dna.txt", 'r') as f:
    seq = f.read().strip()
    assert(utils.validateSeq(seq))
    counts = collections.Counter(seq)

print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}\n")

## Task 2 - Transcribe into RNA

with open("problems/rosalind_rna.txt", 'r') as f:
    seq = f.read().strip()
    assert(utils.validateSeq(seq))
    seq = seq.replace('T', 'U')

print(f"{seq}\n")

## Task 3 - Reverse complementing DNA
"""
DNA sequences have directions which run from 5' to 3' with 5' being the 
phosphate end and 3' being the hydroxy end. String representions are also 
ordered as such. So to form a sequence complementary to another, not only 
should the bases be flipped to their complements, the order of the sequence is 
also reversed.

5' ---> 3'
ATCGTAGCAG <- input sequence
TAGCATCGTC <- output sequence
3' ---> 5'

output sequence (5'-3'): CTGCTACGAT
"""

COMPLEMENT = str.maketrans("ACGT", "TGCA")

with open("problems/rosalind_revc.txt", 'r') as f:
    seq = f.read().strip()
    assert(utils.validateSeq(seq))
    seq = seq.translate(COMPLEMENT)[::-1]

print(seq)

