# @EXPECTED_RESULTS@: WRONG-ANSWER

from sys import stdin
n=stdin.readline().split()[0]
ans=0
for i in range(len(n)):
    ans+=int(n[i])
if (((ans%3)!=0) or (int(n[-1])%2)!=0):
    print "FIGHT!"
else:
    print "BEER!"
