import math
from ..common import *


def modInverse(a, m):
    hcf = math.gcd(a, m)
    if hcf != 1:
        raise Exception("No modulular multiplicative inverse for ", a, m)
    else:
        return (a % m + m) % m


def modFactorial(x, m):
    r = 1
    for i in range(1, x + 1):
        r *= i
        while r >= m:
            r %= m
    return r


def modPermutation(n, k, m):
    b = modFactorial(n - k, m)
    try:
        b_inv = modInverse(b, m)
        a = modFactorial(n, m)
        print('perm route 1')
        return (a * b_inv) % m
    except:
        p = math.perm(n, k)
        while p >= m:
            p %= m
        print('perm route 2')
        return p

def main():
    with open(getProblemPath(__file__), "r") as f:
        [n, k] = [int(s) for s in f.read().strip().split(" ") if s]

    p = modPermutation(n, k, 1000000)
    rprint(p)
