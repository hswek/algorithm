import sys
from collections import deque
sys.setrecursionlimit(10**5)
T=int(input())
for _ in range(T):
    m,n,k=map(int,sys.stdin.readline().rstrip().split())
    arr=[[0]*m for i in range(n)]
    for i in range(k):
        j,i=map(int,sys.stdin.readline().rstrip().split())
        arr[i][j]=1
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    visit=[[0]*(m) for i in range(n)]
    def dfs(x,y,a):
        visit[x][y]=a
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #print(nx,ny)
            #print(arr)
            #print(arr[nx][ny])
            if visit[nx][ny]!=0 or arr[nx][ny]==0:
                continue
            visit[nx][ny]=a
            dfs(nx,ny,a)

    a=1

    for i in range(0,n):
        for j in range(0,m):
            if visit[i][j]==0 and arr[i][j]!=0:
                dfs(i,j,a)
                a+=1
    print(a-1)
    
    

