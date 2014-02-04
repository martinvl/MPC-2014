from sys import stdin

lines = stdin.readlines()
m, n = map(int, lines[0].split())
bi, bj, ri, rj = map(int, lines[1].split())
ps = [map(int, line.split()) for line in lines[2:]]

prev = False
visited = [n*[False] for i in xrange(m)]

def valid_pos(p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < m and p[1] < n

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for p in ps:
    if not valid_pos(p):
        print 'Invalid coordinate', p

    if visited[p[0]][p[1]]:
        print 'Double coordinate', p

    visited[p[0]][p[1]] = True

    if prev and manhattan_dist(p, prev) != 1:
        print 'Invalid distance', p, prev

    prev = p
