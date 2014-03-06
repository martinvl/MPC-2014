from sys import stdin
T=int(stdin.readline())
for tc in range(T):
    s=stdin.readline().split()
    X=int(s[0])
    Y=int(s[1])
    M=int(s[2])
    x=[]
    for i in range(X):
        x.append([])
        s=stdin.readline().split()
        for j in s:
            x[i].append(int(j))
    y=[]
    for i in range(X-1):
        y.append([])
        s=stdin.readline().split()
        for j in s:
            y[i].append(int(j))
    v=[]
    for i in range(X):
        v.append([])
        for j in range(Y):
            v[i].append(0)
    v[0][0]=M
    for i in range(X):
        for j in range(Y):
            i2=i-1
            j2=j-1
            if (j2>=0 and v[i][j2]-x[i][j2]>v[i][j]):
                v[i][j]=v[i][j2]-x[i][j2]
            if (i2>=0 and v[i2][j]-y[i2][j]>v[i][j]):
                v[i][j]=v[i2][j]-y[i2][j]
    
    print v[X-1][Y-1]
