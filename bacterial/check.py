from sys import stdin

m, n, t = map(int, stdin.readline().split())
lines = stdin.readlines()

for line in lines:
    assert(len(line[:-1]) == n)

    for c in line[:-1]:
        assert(c is 'X' or c is '.' or c is '#')

assert(len(lines) == m)
