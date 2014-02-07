from random import randint
from math import log

k = 1000
c_min = 1
c_max = int(10e6)
r_min = 1
r_max = int(10)
n_min = 1
n_max = int(10e6)

eps = 10e-8
vals = []

def make_scheme():
    n = randint(n_min, n_max)
    r = randint(r_min, r_max)
    c = [randint(c_min, c_max) for j in xrange(r)]

    # unique # of combinations?
    val = sum(c)*log(n)

    for v in vals:
        if abs(v - val) < eps:
            return make_scheme()

    vals.append(val)

    return ' '.join([str(n)] + map(str, c))



for i in xrange(k):
    print make_scheme()
