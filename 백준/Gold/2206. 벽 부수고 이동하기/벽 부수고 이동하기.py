import sys
from collections import deque
sys.setrecursionlimit(10**5)

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[1,0,-1,0]
dy=[0,-1,0,1]

result=9876542
visit=[[0]*m for i in range(n)]
d=deque()
d.append([0,0,1])
visit[0][0]=1
while(len(d)!=0):
    x,y,a=d.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=m or visit[nx][ny]!=0 or arr[nx][ny]==1:
            continue
        d.append([nx,ny,a+1])
        visit[nx][ny]=a+1
    
visit2=[[0]*m for i in range(n)]
d=deque()
d.append([n-1,m-1,1])
visit2[n-1][m-1]=1
while(len(d)!=0):
    x,y,a=d.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=m or visit2[nx][ny]!=0 or arr[nx][ny]==1:
            continue
        d.append([nx,ny,a+1])
        visit2[nx][ny]=a+1
    
if visit[n-1][m-1]!=0:
    result=min(result,visit[n-1][m-1])
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            continue
        v=[]
        v2=[]
        for z in range(4):
            nx=i+dx[z]
            ny=j+dy[z]
            if nx<0 or ny<0 or nx>=n or ny>=m or arr[nx][ny]==1:
                continue
            #print(visit[nx][ny],visit2[nx][ny])
            if visit[nx][ny]!=0:
                v.append(visit[nx][ny])
            if visit2[nx][ny]!=0:
                v2.append(visit2[nx][ny])
        #print(v)
        if len(v)==0:
            continue
        if len(v2)==0:
            continue
        result=min(result,min(v)+min(v2)+1)
if result==9876542:
    print(-1)
else:
    print(result)
        