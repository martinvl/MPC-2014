from sys import stdin, maxint

n, v, b = map(int, stdin.readline().split())
s = map(int, stdin.readline().split())

d = -maxint - 1
dist = 0

for i, si in zip(xrange(n), s):
    dist += si

    h = v*b*(i + 1) - dist
    d = h if h > d else d

print s[0] + d
