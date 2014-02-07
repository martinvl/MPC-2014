from sys import stdin
from numpy import cumsum, arange, max

n, v, b = map(int, stdin.readline().split())
dist = cumsum(map(int, stdin.readline().split()))

print dist[0] + max(v*b*(arange(n) + 1) - dist)
