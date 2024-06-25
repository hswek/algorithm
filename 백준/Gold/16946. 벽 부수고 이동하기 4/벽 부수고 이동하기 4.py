import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5*5)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
x,y=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(x):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))
m=[[0]*(y) for i in range(x)]

visit=[[0]*(y) for i in range(x)]

def dfs(a,b):
    global x,y,q
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    visit[a][b]=visit_counter
    q.append([a,b])
    for i in range(4):
        nx=a+dx[i]
        ny=b+dy[i]
        if nx>=x or nx<0 or ny>=y or ny<0:
            continue
        if visit[nx][ny]==0 and arr[nx][ny]==0:
            dfs(nx,ny)
visit_counter=1
for i in range(x):
    for j in range(y):
        if visit[i][j]==0 and arr[i][j]==0:
            q=deque()
            dfs(i,j)
            visit_counter+=1
            l=len(q)
            while len(q):
                a,b=q.pop()
                m[a][b]=l

for i in range(x):
    for j in range(y):
        if arr[i][j]==0:
            print(0,end='')
        else:
            dx=[1,0,-1,0]
            dy=[0,-1,0,1]
            r=1
            a2=[]
            for z in range(4):
                nx=i+dx[z]
                ny=j+dy[z]
                if nx>=x or nx<0 or ny>=y or ny<0:
                    continue
                if visit[nx][ny] not in a2:
                    r+=m[nx][ny]
                    #print(i,j,nx,ny,m[nx][ny])
                    a2.append(visit[nx][ny])
            print(r%10,end='')
    print()









        