n = 90

packages = ['Kristiansand']*(n/3) + ['Bergen']*(n/3) + ['Trondheim']*(n/3)
incompatible = [[False]*n for i in xrange(n)]

for i in xrange(0, 15):
    for j in xrange(15, 30):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(30, 45):
    for j in xrange(45, 60):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(60, 75):
    for j in xrange(75, 90):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(0, 15): # must go directly to Kristiansand (not via Trondheim)
    for j in xrange(60, 90):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(30, 45): # must go directly to Bergen (not via Kristiansand)
    for j in xrange(0, 30):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(60, 75): # must go directly to Trondheim (not via Bergen)
    for j in xrange(30, 60):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(15, 30): # must go indirectly to Kristiansand
    for j in xrange(30, 60):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(45, 60): # must go indirectly to Bergen
    for j in xrange(60, 90):
        incompatible[i][j] = incompatible[j][i] = True

for i in xrange(75, 90): # must go indirectly to Trondheim
    for j in xrange(0, 30):
        incompatible[i][j] = incompatible[j][i] = True

print n
for i in xrange(n):
    print ' '.join(map(str, [packages[i]] + [j for j in xrange(n) if incompatible[i][j]]))
