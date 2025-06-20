import random
from pathlib import Path
from collections import OrderedDict
from pyperclip import copy

def randomSeq(length=50) -> str:
    return ''.join([random.choice("ACGT") for _ in range(0, length)])

def readFile(path: str) -> str:
    with open(path, 'r') as f:
        return f.read().strip().upper()

def readFasta(path: str) -> OrderedDict[str, str]:
    with open(path, 'r') as f:
        lines = f.readlines()

    result = OrderedDict()
    current = ''

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '>':
            current = line[1:]
            result[current] = ''
        else:
            result[current] += line

    return result

def getProblemPath(file: str) -> str:
    name = Path(file).stem
    return f"pkg/rosalind/problems/rosalind_{name}.txt" 

_result = ''

def rprint(*msg, end='\n'):
    global _result
    for m in msg:
        _result += str(m)
    _result += end if end else ''
    print(*msg, end=end)

def copyResult():
    global _result
    copy(_result)
    _result = ''
