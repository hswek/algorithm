import sys
from collections import deque
sys.setrecursionlimit(10**5)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[1,0,-1,0]
dy=[0,-1,0,1]
visit=[[0]*(n+1) for i in range(n+1)]
def dfs(x,y,a):
    visit[x][y]=a
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
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
    for j in range(0,n):
        if visit[i][j]==0 and arr[i][j]!=0:
            dfs(i,j,a)
            a+=1
d={}
#print(visit)
for i in range(0,n):
    for j in range(0,n):
        if visit[i][j] in d:
            d[visit[i][j]]+=1
        else:
            d[visit[i][j]]=1
ab=[]
for i,j in d.items():
    ab.append([j,i])
ab.sort()
#print(ab)

if 0 in d:
    print(len(ab)-1)
else:
    print(len(ab))
for i in ab:
    if i[1]==0:
        continue
    print(i[0])
    
    

