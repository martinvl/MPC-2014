from sys import stdin
from numpy import array, sum
from scipy.ndimage import binary_dilation

c_to_v = {'#':1, '.':0, 'X':-1}

m, n, g = map(int, stdin.readline().split())
dish = array([[c_to_v[c] for c in l.replace('\n', '')] for l in stdin])
mask = 1 - (dish == -1)
result = binary_dilation(dish == 1, [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 2, mask)

v_to_c = {-1:'X', 0:'.', 1:'#'}

def print_dish(dish):
    for i in xrange(len(dish)):
        print ''.join([v_to_c[a] for a in dish[i,:]])

print_dish(result - 1 + mask)
