import random
from pathlib import Path
import __main__

def randomSeq(length=50) -> str:
    return ''.join([random.choice("ACGT") for _ in range(0, length)])

def readFile(path: str | None = None) -> str:
    if not path:
        path = getDataPath()

    with open(path, 'r') as f:
        return f.read().strip().upper()

def readFasta(path: str | None = None) -> dict[str, str]:
    if not path:
        path = getDataPath()

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

def getDataPath() -> str:
    name = Path(__main__.__file__).stem
    return f"problems/rosalind_{name}.txt" 
