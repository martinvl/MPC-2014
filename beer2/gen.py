from random import randint

m = int(1e6)

print ''.join(map(str, (randint(0, 9) for j in xrange(m))))
