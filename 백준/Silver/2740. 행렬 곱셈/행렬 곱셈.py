import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
a=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().rstrip().split())))
m,k=map(int,sys.stdin.readline().rstrip().split())
b=[]
for i in range(m):
    b.append(list(map(int,sys.stdin.readline().rstrip().split())))
arr=[[0]*k for i in range(n)]
for i in range(n):
    for j in range(k):
        s=0
        for z in range(m):
            s+=a[i][z]*b[z][j]
        print(s,end=' ')
    print()