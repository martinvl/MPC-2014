from random import random, randint

cities = ('Kristiansand', 'Bergen', 'Trondheim')

n_min = 1
n_max = int(100)

incompatible_rate = .05
n = randint(n_min, n_max)

packages = [cities[randint(0, len(cities)-1)] for i in xrange(n)]
compatible = [n*[True] for i in xrange(n)]

for i in xrange(n):
    for j in xrange(n):
        if i == j:
            continue

        if random() < incompatible_rate/2:
            compatible[i][j] = False
            compatible[j][i] = False

print n

for i in xrange(n):
    print ' '.join(map(str, [packages[i]] + [j for j in xrange(n) if not compatible[i][j]]))
