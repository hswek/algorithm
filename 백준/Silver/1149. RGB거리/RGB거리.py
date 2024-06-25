import sys
n=int(input())
r=[-1]*1001
g=[-1]*1001
b=[-1]*1001
for _ in range(n):
    x,y,z=map(int,input().split())
    r[_+1]=x
    g[_+1]=y
    b[_+1]=z
min_r=[-1]*1001
min_g=[-1]*1001
min_b=[-1]*1001
min_r[1]=r[1]
min_g[1]=g[1]
min_b[1]=b[1]
def a(n,color):
    if color==r:
        if min_r[n]!=-1:
            return min_r[n]
        min_r[n]=min([a(n-1,b)+r[n],a(n-1,g)+r[n]])
        return min_r[n]
    if color==b:
        if min_b[n]!=-1:
            return min_b[n]
        min_b[n]=min([a(n-1,g)+b[n],a(n-1,r)+b[n]])
        return min_b[n]
    if color==g:
        if min_g[n]!=-1:
            return min_g[n]
        min_g[n]=min([a(n-1,b)+g[n],a(n-1,r)+g[n]])
        return min_g[n]
x1=a(n,r)
x2=a(n,b)
x3=a(n,g)
print(min([x1,x2,x3]))