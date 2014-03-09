from sys import stdin
from time import sleep
from scitools.std import *

def plot_grid(m, n):
    # horizontal lines
    for i in xrange(m):
        plot([0, n-1], [i, i], 'k', hidden='on', daspect=[1,1,1])

    # vertical lines
    for j in xrange(n):
        plot([j, j], [0, m-1], 'k', hidden='on', daspect=[1,1,1])

m, n = map(int, stdin.readline().split())
bi, bj, ri, rj = map(int, stdin.readline().split())
p = [map(int, line.split()) for line in stdin]
pi, pj = zip(*p)

# safe route
si, sj = zip(*((5, 4), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (4, 1), (4, 0),
    (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2)))

# unsafe route
ui, uj = zip(*((5, 4), (4, 4), (3, 4), (3, 3), (2, 3), (2, 2), (1, 2)))

figure()
hold('on')
axis([-1, n, -1, m])
plot_grid(m, n)
plot(pj, m - 1 - array(pi), 'b-3', legend='Police route')
plot(sj, si, 'g-3', legend='Safe route')
plot(uj, ui, 'r--3', legend='Unsafe route')
plot([bj], [m - 1 - bi], 'rs', legend='Bank')
plot([rj], [m - 1 - ri], 'gs', legend='Rendezvous point')
hardcopy('getaway.png')
