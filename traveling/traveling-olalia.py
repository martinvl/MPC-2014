# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

N=int(stdin.readline())
M=int(stdin.readline())
e=N*[[]]
f=N*[[]]

for i in range(M):
    s=stdin.readline().split()
    a=int(s[0])
    b=int(s[1])
    e[a].append(b)
    f[b].append(a)
done=N*[0]
done[0]=1
v=[0]
i=0
while(i<len(v)):
    for j in e[v[i]]:
        if (done[j]==0):
            done[j]=1
            v.append(j)
    i=i+1
if (len(v)<N):
    print "NO"
    quit()
done=N*[0]
done[0]=1
v=[0]
i=0
while(i<len(v)):
    for j in f[v[i]]:
        if (done[j]==0):
            done[j]=1
            v.append(j)
    i=i+1
if (len(v)<N):
    print "NO"
    quit()
print "YES"
