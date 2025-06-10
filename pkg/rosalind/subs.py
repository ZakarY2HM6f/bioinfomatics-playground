from __init__ import *

data = readFile().split('\n')
assert(len(data) == 2)

s = data[0]
t = data[1]

locations = []

i = 0
while True:
    i = s.find(t, i + 1)
    if i < 0:
        break
    locations.append(i)

print(' '.join([ str(l + 1) for l in locations ]))
