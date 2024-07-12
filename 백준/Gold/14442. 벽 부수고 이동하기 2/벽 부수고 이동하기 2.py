import sys
from collections import deque
import heapq
import math
#sys.setrecursionlimit(10**5)
n,m,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
visit=[[[-1] *m for _ in range(n) ] for __ in range(k+1)]
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
while q:
    x,y,crash=q.popleft()
    dis=visit[crash][x][y]
    if x==n-1 and y==m-1:
        print(visit[crash][x][y])
        a=2
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if arr[nx][ny]=="1":
            #print("its wall",nx,ny)
            if crash==k or visit[crash+1][nx][ny]!=-1:
                continue
            #for j in range(crash+2):
            ##    if to_str(nx,ny,j) in visit:
            #        continue
            #if to_str(nx,ny,crash+1) in visit:
            #    continue
            q.append((nx,ny,crash+1))
            #visit[crash+1][nx][ny]=True
            visit[crash+1][nx][ny]=dis+1
            #visit[to_str(nx,ny,crash+1)]=dis+1
        else:
            #print("its not wall",nx,ny)
            #for j in range(crash+1):
            #    if to_str(nx,ny,j) in visit:
            #        continue
            #if to_str(nx,ny,crash) in visit:
            #    continue
            if visit[crash][nx][ny]!=-1:
                continue
            q.append((nx,ny,crash))
            visit[crash][nx][ny]=dis+1
            #visit[to_str(nx,ny,crash)]=1
            #visit[to_str(nx,ny,crash)]=dis+1
if a==1:
    print(-1)