import random
import __main__

def randomSeq(length=50) -> str:
    return ''.join([random.choice("ACGT") for _ in range(0, length)])

def readFile(path: str) -> str:
    with open(path, 'r') as f:
        return f.read().strip().upper()

def readFasta(path: str) -> dict[str, str]:
    with open(path, 'r') as f:
        lines = f.readlines()

    result = {}
    current = ''

    for line in lines:
        line = line.strip()
        if line[0] == '>':
            current = line[1:]
            result[current] = ''
        else:
            result[current] += line

    return result

def dataPath() -> str:
    name = __main__.__file__.split('.')[0]
    return f"problems/rosalind_{name}.txt" 
