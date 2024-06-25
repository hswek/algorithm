import sys
from collections import deque
sys.setrecursionlimit(10**5)

m,n,h=map(int,sys.stdin.readline().rstrip().split())

arr=[]
for j in range(h):
    tmp=[]
    for i in range(n):
        tmp.append(list(map(int,sys.stdin.readline().rstrip().split())))
    arr.append(tmp)
visit=[[[0]*m for i in range(n)] for j in range(h)]

d=deque()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if arr[z][i][j]==1:
                d.append([z,i,j,0])
                visit[z][i][j]=1
            
max_num=0
while(len(d)!=0):
    z,x,y,a=d.popleft()
    pos=[[0,1,0],[0,0,-1],[0,-1,0],[0,0,1],[1,0,0],[-1,0,0]]
    for pz,px,py in pos:
        nx=x+px
        ny=y+py
        nz=z+pz
        if nx>=n or nx<0 or ny>=m or ny<0 or nz>=h or nz<0 or visit[nz][nx][ny]!=0 or arr[nz][nx][ny]==-1:
            continue
        visit[nz][nx][ny]=a+1
        d.append([nz,nx,ny,a+1])
        max_num=max(max_num,a+1)
p=False
#print(visit)
for z in range(h):
    for i in range(n):
        for j in range(m):
            if visit[z][i][j]==0 and arr[z][i][j]!=-1:
                p=True
                print(-1)
                break
        if p==True:
            break
        
if p==False:
    print(max_num)


        
    