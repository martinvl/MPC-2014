from random import randint

config = ['#', ' ']
b_min = s_min = 1
b_max = s_max = 16

b = randint(b_min, b_max)
s = randint(s_min, s_max)

print b, s

for i in xrange(s):
    print ''.join([config[randint(0, 1)] for j in xrange(b)])
