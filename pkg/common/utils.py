import random
from pathlib import Path
from pyperclip import copy

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

def getDataPath(file: str) -> str:
    name = Path(file).stem
    return f"pkg/rosalind/problems/rosalind_{name}.txt" 

_result = ''

def rprint(msg):
    global _result
    _result += str(msg)
    _result += '\n'
    print(msg)

def copyResult():
    global _result
    copy(_result)
    _result = ''
