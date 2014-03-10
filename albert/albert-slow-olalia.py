# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
s=stdin.readline().split()
while(len(s)>0):
    l=int(s[0])
    n=int(stdin.readline())
    d=[]
    p=[]
    for i in range(n):
        s=stdin.readline().split()
        d.append(int(s[0]))
        p.append((int(s[1]), i))
        
    p.sort()
    w=[]
    for i in range(d[n-1]):
        w.append(0)
    ans=0
    c=0
    for i in range(n):
        j=d[p[i][1]]
        while(j<d[n-1] and j<d[p[i][1]]+l):
            if (w[j]==0):
                ans+=p[i][0]
                w[j]=1
                c+=1
            j+=1
            
    if (c<d[n-1]):
        print "Stay home"
    else:
        print ans
    s=stdin.readline().split()
