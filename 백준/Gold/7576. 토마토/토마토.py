import sys
from collections import deque
sys.setrecursionlimit(10**5)

m,n=map(int,sys.stdin.readline().rstrip().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
visit=[[0]*m for i in range(n)]
d=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            d.append([i,j,0])
            visit[i][j]=1
            
max_num=0
while(len(d)!=0):
    x,y,a=d.popleft()
    pos=[[1,0],[0,-1],[-1,0],[0,1]]
    for px,py in pos:
        nx=x+px
        ny=y+py
        if nx>=n or nx<0 or ny>=m or ny<0 or visit[nx][ny]!=0 or arr[nx][ny]==-1:
            continue
        visit[nx][ny]=a+1
        d.append([nx,ny,a+1])
        max_num=max(max_num,a+1)
p=False
#print(visit)
for i in range(n):
    for j in range(m):
        if visit[i][j]==0 and arr[i][j]!=-1:
            p=True
            print(-1)
            break
    if p==True:
        break
        
if p==False:
    print(max_num)


        
    