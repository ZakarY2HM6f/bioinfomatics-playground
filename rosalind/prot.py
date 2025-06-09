from __init__ import *

data = readFile()
seq = RNASeq(data)
seq = seq.translated()

print(seq[:-1])
