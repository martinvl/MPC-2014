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

figure()
hold('on')
axis([-1, n, -1, m])
plot_grid(m, n)
plot(pj, m - 1 - array(pi), 'b-3', legend='Police route')
plot([bj], [m - 1 - bi], 'rs', legend='Bank')
plot([rj], [m - 1 - ri], 'gs', legend='Rendezvous point')
hardcopy('getaway.png')
