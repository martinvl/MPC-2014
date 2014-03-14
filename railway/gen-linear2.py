"""
Generates test case that punished linear status checks
"""

n = int(1e5)
k = int(1e5)

print n

print '%d blocked' % (n/3)
print '%d blocked' % (2*n/3)

for i in xrange(k-2):
    print '%d status' % (n/2)
