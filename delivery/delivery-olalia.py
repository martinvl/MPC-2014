# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

n=int(stdin.readline())
N=2*n
s=stdin.readline().split()
city=[]
cities=["Kristiansand", "Bergen", "Trondheim"]
for w in s:
    for i in range(3):
        if (w==cities[i]):
            city.append(i)

inco=[]
for i in range(n):
    inco.append([])
    s=stdin.readline().split()
    for j in range(len(s)):
        inco[i].append(int(s[j]))
global inco2
inco2=[]
for i in range(2*n):
    inco2.append([])
for i in range(n):
    for j in inco[i]:
        for k in range(2):
            for h in range(2):
                if (((city[i]+k)%3)==((city[j]+h)%3)):
                    inco2[(i+k*n)%N].append((j+(h+1)*n)%N)
global index, compnum
global vindex, lowlink, comps
global S
vindex=[]
lowlink=[]
comps=[]
compnum=0
index=0
for i in range(N):
    vindex.append(-1)
    comps.append(-1)
    lowlink.append(-1)
S=[]
def sc(i):
    global inco2
    global index, compnum
    global vindex, lowlink, comps
    global S
    vindex[i]=index
    lowlink[i]=index
    index+=1
    S.append(i)
    for w in inco2[i]:
        if (vindex[w]==-1):
            sc(w)
            if (lowlink[w]<lowlink[i]):
                lowlink[i]=lowlink[w]
        else:
            if (comps[w]==-1):
                if (vindex[w]<lowlink[i]):
                    lowlink[i]=vindex[w]
    if (lowlink[i]==vindex[i]):
        while(1):
            w=S.pop()
            comps[w]=compnum
            if (w==i):
                compnum+=1
                break
    return
        

for i in range(N):
    if (vindex[i]==-1):
        sc(i)
for i in range(n):
    if (comps[i]==comps[i+n]):
        print "Impossible"
        quit()
print "Possible"
