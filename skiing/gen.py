from random import randint

n_min = 1
n_max = int(10e4)
v_min = b_min = 1
v_max = b_max = 30
s_min = 1
s_max = int(10e2)

n = randint(n_min, n_max)
v = randint(v_min, v_max)
b = randint(b_min, b_max)

print n, v, b
print ' '.join(map(str, [randint(s_min, s_max) for i in xrange(n)]))
