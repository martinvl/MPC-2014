from sys import stdin
from math import floor, log

def solve_const(N):
    p = int(floor(log(N, 2)))
    l = N % 2**p

    return 2*l+1

for line in stdin:
    print solve_const(int(line))

