# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
s=stdin.readline().split()
n=int(s[0])
v=int(s[1])
b=int(s[2])

s=stdin.readline().split()
for i in range(n):
    s[i]=int(s[i])
d=-s[0]
ans=0
for i in range(0,n):
    d+=s[i]
    if (v*b*(i+1)-d>ans):
        ans=b*v*(i+1)-d

print ans
