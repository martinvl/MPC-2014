from random import randint

c_min = -int(1e4)
c_max = int(1e4)
n_min = 1
n_max = int(1e4)

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

n = randint(n_min, n_max)
print n

wires = []

def make_wire():
    points = [randint(c_min, c_max) for i in xrange(4)]
    wire = Line(*points)
    x1, y1, x2, y2 = points

    if (x1 == x2 and y1 == y2) or wire in wires:
        return make_wire()

    wires.append(wire)
    return points

for i in xrange(n):
    print ' '.join(map(str, make_wire()))
