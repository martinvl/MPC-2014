"""
Generates test case that punishes linear search over array containing all
closed or open segments
"""
from random import randint

n = int(1e5)
k = int(1e5)

o = range(n)
c = []

print n

for i in xrange(k/2):
    s = o.pop(randint(0, len(o)-1))
    c.append(s)

    print s, 'blocked'

print n/2, 'status'

for i in xrange(k/2 - 2):
    s = c.pop(randint(0, len(c)-1))
    o.append(s)

    print s, 'opened'

print n/2, 'status'
