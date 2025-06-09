import math

with open('problems/rosalind_iprb.txt', 'r') as f:
    data = f.read().strip().split(' ')

assert(len(data) == 3)

k = int(data[0])
m = int(data[1])
n = int(data[2])

total = k + m + n

t = math.comb(total, 2)
kx = (math.comb(k + m, 2) + math.comb(k + n, 2) - math.comb(k, 2) - math.comb(m, 2) - math.comb(n, 2)) / t
mm = math.comb(m, 2) / t
mn = (math.comb(m + n, 2) - math.comb(m, 2) - math.comb(n, 2)) / t

p = kx + mm * 0.75 + mn * 0.5

print(round(p, 6))
