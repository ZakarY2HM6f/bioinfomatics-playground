from __init__ import *

data = list(readFasta().values())

l = len(data[0])
for i in range(0, len(data)):
    assert(len(data[i]) == l)

profile = {
    'A': [ 0 for _ in range(0, l) ],
    'T': [ 0 for _ in range(0, l) ],
    'C': [ 0 for _ in range(0, l) ],
    'G': [ 0 for _ in range(0, l) ]
}

for seq in data:
    for i, b in enumerate(seq):
        profile[b][i] += 1

consensus = ''

for i in range(0, l):
    cons = max(profile, key=lambda k: profile[k][i])
    consensus += cons

print(consensus)
for k, v in profile.items():
    print(f"{k}: " + ' '.join([ str(x) for x in v]))
