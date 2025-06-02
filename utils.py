def readFromFile(path: str) -> str:
    with open(path, 'r') as f:
        return f.read().strip().upper()
