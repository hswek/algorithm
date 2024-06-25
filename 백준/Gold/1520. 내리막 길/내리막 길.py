import sys
import heapq
from collections import deque
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
#arr=[]
#for i in range(500):
#    arr.append(range(1000-i,500-i,-1))
cache=[[-1]*501 for i in range(501)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def recursive(x,y):
    if x==n-1 and y==m-1:
        return 1
    if cache[x][y]!=-1:
        return cache[x][y]
    result=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if arr[nx][ny]>=arr[x][y]:
            continue
        result+=recursive(nx,ny)
    cache[x][y]=result
    return result
print(recursive(0,0))