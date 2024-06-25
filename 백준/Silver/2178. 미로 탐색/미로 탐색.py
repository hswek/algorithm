import sys
from collections import deque
sys.setrecursionlimit(10**5)
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[1,0,-1,0]
dy=[0,-1,0,1]
visit=[[0]*(m) for i in range(n)]

def bfs(x,y):
    d=deque()
    d.append([x,y,1])
    visit[x][y]=1
    while(len(d)!=0):
        x,y,a=d.popleft()
        if x==n-1 and y==m-1:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visit[nx][ny]!=0 or arr[nx][ny]==0:
                continue
            visit[nx][ny]=a
            d.append([nx,ny,a+1])
bfs(0,0)
print(visit[n-1][m-1]+1)
    

