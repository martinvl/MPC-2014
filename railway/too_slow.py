from sys import stdin
from numpy import zeros

n = int(stdin.readline())
segments = zeros(n)

for line in stdin:
    i, w = line.split()
    i = int(i)

    if w == 'blocked':
        segments[i] = 1
    elif w == 'opened':
        segments[i] = 0
    else:
        if segments[:i+1].any() and segments[i:].any():
            print 'no service'
        else:
            print 'good service'
