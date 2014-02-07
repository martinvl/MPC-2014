from sys import stdin, maxint
from numpy import cumsum, array, max

n, v, b = map(int, stdin.readline().split())
dist = cumsum(map(int, stdin.readline().split()))

print dist[0] + max(v*b*(array(xrange(n)) + 1) - dist)
