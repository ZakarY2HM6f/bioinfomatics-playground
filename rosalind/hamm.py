with open('problems/rosalind_hamm.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

assert(len(data) == 2)
assert(len(data[0]) == len(data[1]))

distance = 0

for i in range(0, len(data[0])):
    if data[0][i] != data[1][i]:
        distance += 1

print(distance)
