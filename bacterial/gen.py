from random import random, randint

cell_ratio = .02
v_to_c = {-1:'X', 0:'.', 1:'#'}

def in_circle(i, j, diam):
    rad = diam/2
    cx = cy = diam/2. - .5

    return (j - cx)**2 + (i - cy)**2 <= rad**2

def get_dishpoint(i, j, diam):
    return v_to_c[random() < cell_ratio if in_circle(i, j, diam) else -1]

def gen_dish(diam):
    for i in xrange(diam):
        print ''.join([get_dishpoint(i, j, diam) for j in xrange(diam)])

d_min = 1
d_max = 100
t_min = 1
t_max = 20

d = randint(d_min, d_max)
t = randint(t_min, t_max)

print d, d, t
gen_dish(d)
