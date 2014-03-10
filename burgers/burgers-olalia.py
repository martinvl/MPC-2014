# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

l =stdin.readline().split()

b=int(l[0])
s=int(l[1])
v=b*[0]

for i in range(s):
    l=stdin.readline()
    for j in range(b):
        v[j]*=2
        if (j<len(l) and l[j]=='#'):
            v[j]+=2
for j in range(b):
    v[j]+=1

a=0
for j in range(b):
    ma=a
    for i in range(a+1,b):
        if (v[i]>v[ma]):
            ma=i
    #print a, v[ma]
    if (v[ma]==1):
        print "Impossible"
        quit()
    if (v[ma]==0):
        break
    bytt=v[ma]
    v[ma]=v[a]
    v[a]=bytt
    a+=1
    for i in range(a,b):
        if ((v[i]^v[a-1])<v[i]):
            v[i]=v[i]^v[a-1]

a2=a
while (v[a-1]%2==0):
    a=a-1

for i in range(a-1):
    if ((v[i]%2)==1):
        v[i]=(v[i]^v[a-1])

for i in range(a2):
    if (a2-i==a):
        continue
    for  j in range(a2-i-1):
        if (v[j]^v[a2-1-i]<v[j]):
            v[j]^=v[a2-1-i]

        



ans=s
for i in range(s):
    if ((1<<(s-i))&v[a-1]!=0):
        cand=0
        for j in range(a2):
            if ((1<<(s-i))&v[j]!=0):
                cand=cand+1
        if (cand<ans):
            ans=cand

print ans
