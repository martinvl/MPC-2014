from random import randint

n = 99 # must be divisible by 3
possible = False

packages = ['Kristiansand']*(n/3) + ['Bergen']*(n/3) + ['Trondheim']*(n/3)
incompatible = [[False]*n for i in xrange(n)]

for i in xrange(0*n/6, 1*n/6):
    for j in xrange(1*n/6, 2*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(2*n/6, 3*n/6):
    for j in xrange(3*n/6, 4*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(4*n/6, 5*n/6):
    for j in xrange(5*n/6, 6*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(0*n/6, 1*n/6): # must go directly to Kristiansand (not via Trondheim)
    for j in xrange(4*n/6, 6*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(2*n/6, 3*n/6): # must go directly to Bergen (not via Kristiansand)
    for j in xrange(0*n/6, 2*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(4*n/6, 5*n/6): # must go directly to Trondheim (not via Bergen)
    for j in xrange(2*n/6, 4*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(1*n/6, 2*n/6): # must go indirectly to Kristiansand
    for j in xrange(2*n/6, 4*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(3*n/6, 4*n/6): # must go indirectly to Bergen
    for j in xrange(4*n/6, 6*n/6):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(5*n/6, 6*n/6): # must go indirectly to Trondheim
    for j in xrange(0*n/6, 2*n/6):
        incompatible[i][j] = incompatible[j][i] = True

if not possible:
    while True:
        a = randint(0, n-1)
        b = randint(0, n-1)

        if a == b or incompatible[a][b]:
            continue
        else:
            incompatible[a][b] = True
            incompatible[b][a] = True
            break

print n
print ' '.join(packages)

for i in xrange(n):
    print ' '.join(map(str, [j for j in xrange(n) if incompatible[i][j]]))
