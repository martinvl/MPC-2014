# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from numpy import cumsum, max, arange

n, v, b = map(int, stdin.readline().split())
dist = cumsum([int(i) for i in stdin.readline().split()])

print(dist[0] + max(v*b*(arange(n) + 1) - dist))
