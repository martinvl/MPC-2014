from random import randint

m = 9

print ''.join(map(str, (randint(0, 9) for j in xrange(m))))
