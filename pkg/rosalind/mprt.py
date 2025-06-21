from ..common import *
import requests
import re


finder = re.compile(r"\{([^\}]+)\}")


def motifToRegex(m: str) -> str:
    n = re.search(finder, m)
    while n:
        m = m.replace(n.group(0), f"[^{n.group(1)}]")
        n = re.search(finder, m)
    return f"({m})"


def main():
    with open(getProblemPath(__file__), "r") as f:
        ids = [l for l in f.read().splitlines() if len(l) > 0]

    mr = motifToRegex("N{P}[ST]{P}")

    results = {}
    for id in ids:
        nid = id.split("_")[0]

        url = f"http://www.uniprot.org/uniprot/{nid}.fasta"
        r = requests.get(url)
        if r.status_code != 200:
            print(url)
            continue

        s = r.content.decode()
        try:
            s = parseFasta(s)
            s = AASeq(s.values().__iter__().__next__())
        except:
            print(id)
            print(r.content)
            continue
        
        m = re.search(mr, s)
        i = 0
        while m:
            if id not in results:
                results[id] = []
            results[id].append(i + m.start() + 1)
            s = s[m.start() + 1:]
            i += m.start() + 1
            m = re.search(mr, s)

    for id, motifs in results.items():
        rprint(id)
        rprint(*motifs)

    copyResult()

# USED: 01:27