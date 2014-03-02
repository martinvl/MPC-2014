from sys import stdin


l = stdin.readline().split()
n = int(l[0])
v = int(l[1])
b = int(l[2])

l = stdin.readline().split()
dist_to_first = int(l[0])
acc_dist = 0
result = 0
for i in range(n):
    acc_dist += int(l[i])
    if v*b*(i+1) - acc_dist + dist_to_first > result:
        result = v*b*(i+1) - acc_dist + dist_to_first

print result
