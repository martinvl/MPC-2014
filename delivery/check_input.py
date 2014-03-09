from sys import stdin
from numpy import zeros, diag, nonzero

n = int(stdin.readline())
cities = stdin.readline().split()

assert(len(cities) == n) # check num cities = n

incomps = zeros((n, n))

i = 0
for line in stdin:
    incomps[i, map(int, line.split())] = 1
    i += 1

assert(i == n) # check num incomps = n
assert((incomps == incomps.T).all()) # check incomps is two-way
assert((diag(incomps) == 0).all()) # check no self-incomp

print 'input OK'
