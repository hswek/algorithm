import sys
from collections import deque
sys.setrecursionlimit(10**4)

#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
    
cache=[[-1]* (m+1) for i in range(n+1)]
arr2=[[0]* (m+1) for i in range(n+1)]
def recursive(x,y,p):
    global n,m
    #print(x,y)
    if arr2[x][y]==1:
        return 99999999999
    if cache[x][y]!=-1:
        return cache[x][y]
    how=arr[x][y]
    if how=='H':
        return 0
    how=int(how)
    dx=[how,0,-how,0]
    dy=[0,-how,0,how]
    result=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if arr[nx][ny]=='H':
            continue
        arr2[x][y]=1
        result=max(result,recursive(nx,ny,p+[x,y])+1)
        arr2[x][y]=0
    cache[x][y]=result
    return result

r=recursive(0,0,[])
if r>=99999999:
    print(-1)
else:
    print(r+1)