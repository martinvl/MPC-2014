# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
s = stdin.readline().split()
d=int(s[0])
s = stdin.readline().split()
n=int(s[0])

print d*n-1
