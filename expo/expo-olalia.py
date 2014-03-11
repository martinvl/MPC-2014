# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

v=stdin.readline().split()
a=int(v[0])
b=int(v[1])
n=int(v[2])
c=1
while(b>0):
    if (b%2):
        c*=a
        c%=n
    b/=2
    a*=a
    a%=n
print c
