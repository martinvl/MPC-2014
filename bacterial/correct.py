from sys import stdin
from numpy import array, sum
from scipy.ndimage import binary_dilation

c_to_v = {'#':1, '.':0, ' ':-1}

d, t = map(int, stdin.readline().split())
dish = array([[c_to_v[c] for c in l.replace('\n', '')] for l in stdin])
mask = 1 - (dish == -1)
result = binary_dilation(dish == 1, [[0, 1, 0], [1, 1, 1], [0, 1, 0]], t, mask)

print sum(result)
