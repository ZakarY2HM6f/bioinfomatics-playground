with open("problems/rosalind_fib.txt", 'r') as f:
    data = f.read().strip().split(' ')

assert(len(data) == 2)
n = int(data[0])
k = int(data[1])

initPair = 1

lastPair = initPair
currPair = initPair
for _ in range(0, n - 2):
    tmp = lastPair * k + currPair
    lastPair = currPair
    currPair = tmp

print(currPair)
