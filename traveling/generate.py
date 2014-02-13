from networkx import *
import sys

n =  eval(sys.argv[1])
p = eval(sys.argv[2])
g = erdos_renyi_graph(n, p, directed=True)

print n
print len(g.edges())
for a,b in g.edges():
	print a,b



