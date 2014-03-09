from random import random

v_max = 100
t_max = 4 # technically 100, but that's not interesting
h_max = 1

v = v_max*random()
t = t_max*random()
p = 1 - h_max*random() # avoid 0, allow 1

print v, t, p
