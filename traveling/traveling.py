# @EXPECTED_RESULTS@: CORRECT

import numpy

n = int(raw_input())
m = int(raw_input())

edges = []
edges_reverse = []
for i in range(n):
	edges.append([])
	edges_reverse.append([])

	
for i in range(m):
	a,b = raw_input().split()
	a = int(a)
	b = int(b)
	edges[a].append(b)
	edges_reverse[b].append(a)

def bfs(start, e):
	vis = [False for i in range(n)]
	vis[start] = True
	q = [start]
	while len(q)>0:
		x = q[len(q)-1]
		q.pop()
		vis[x] = True
		for y in e[x]:
			if vis[y] == False:
				q.append(y)

	return vis.count(True)

vis1 = bfs(0, edges)
vis2 = bfs(0, edges_reverse)

if vis1 + vis2 == 2*n:
	print 'YES'
else:
	print 'NO'






