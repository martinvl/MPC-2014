from random import randint
from math import floor, ceil

c_min = -int(1e4)
c_max = int(1e4)
n = int(1e4)
broken = False

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p = (x1, y1) # origin
        self.d = (x2 - x1, y2 - y1) # direction

    def __eq__(self, l):
        return self.par(l) and self.has(*l.p)

    def has(self, x, y): # has point
        dx, dy = self.d
        sx = x - self.p[0]
        sy = y - self.p[1]

        return  sx*dy == sy*dx

    def par(self, l): # is parallell
        x, y = self.d
        lx, ly = l.d

        return x*ly == y*lx


print n
wires = []

def make_hor_wire():
    x1, x2, y = [randint(c_min, c_max) for i in xrange(3)]
    points = (x1, y, x2, y)
    wire = Line(*points)

    if x1 == x2 or wire in wires:
        return make_hor_wire()

    wires.append(wire)
    return points

def make_ver_wire():
    x, y1, y2 = [randint(c_min, c_max) for i in xrange(3)]
    points = (x, y1, x, y2)
    wire = Line(*points)

    if y1 == y2 or wire in wires:
        return make_ver_wire()

    wires.append(wire)
    return points

for i in xrange(n - 1):
    print ' '.join(map(str, make_hor_wire() if i % 2 else make_ver_wire()))

print ' '.join(map(str, (0, 0, 1, 1) if broken else make_hor_wire()))

