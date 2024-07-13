import sys
from collections import deque
import heapq
import math
#sys.setrecursionlimit(10**5)
n,m,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
visit=[[[999999999] *m for _ in range(n) ] for __ in range(k+10)]
#visit={}
dx=[1,0,-1,0]
dy=[0,-1,0,1]
a=1
q=deque([[0,0,0]])
def to_str(x,y,crash):
    x,y,crash=map(str,[x,y,crash])
    return "_".join([x,y,crash])
#visit[to_str(0,0,0)]=1
visit[0][0][0]=1
result=9999999999999
while q:
    x,y,crash=q.popleft()
    
    dis=visit[crash][x][y]
    if dis%2==1:
        day=1
    else:
        day=0
    #print(x,y,crash,dis,day)
    if x==n-1 and y==m-1:
        result=min(result,visit[crash][x][y])
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if arr[nx][ny]=="1":
            if crash==k:
                continue
            if day==1:
                if visit[crash+1][nx][ny]<=dis+1:
                    continue
                q.append((nx,ny,crash+1))
                visit[crash+1][nx][ny]=dis+1
            if day==0:
                if visit[crash+1][nx][ny]<=dis+2:
                    continue
                q.append((nx,ny,crash+1))
                visit[crash+1][nx][ny]=dis+2
        else:
            if visit[crash][nx][ny]<=dis+1:
                continue
            q.append((nx,ny,crash))
            visit[crash][nx][ny]=dis+1
if 9999999999999==result:
    print(-1)
else:
    print(result)