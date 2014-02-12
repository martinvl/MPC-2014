from sys import stdin

def parse_spatula(line):
    line = line.replace('#', '1')
    line = line.replace(' ', '0')

    return int(line, 2)

b, s = map(int, stdin.readline().split())
spatulas = map(parse_spatula, stdin)

N = s+1

for i in xrange(2**s):
    spatula = 0
    n = 0

    for j in xrange(s):
        if i & (1 << j):
            spatula ^= spatulas[j]
            n += 1

    if spatula == 2**b-1 and n < N:
        N = n

if N == s+1:
    print 'Impossible'
else:
    print N
