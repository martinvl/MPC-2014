# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

s=stdin.readline().split()
n=int(s[0])
neh=-1
ans=0
pri=""


for i in range(n):
    s=stdin.readline().split()
    k=int(s[0])
    c=0
    for j in range(k):
        s=stdin.readline().split()
        c=c+int(s[1])*(int(s[0])+1)
    if (c==neh):
        pri="*"
    if (c>neh):
        ans=i+1
        neh=c

    
print str(ans)+pri,
