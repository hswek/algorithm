import sys
from collections import deque
sys.setrecursionlimit(10**5)
T=int(input())
for _ in range(T):
    n=int(sys.stdin.readline().rstrip())
    x,y=map(int,sys.stdin.readline().rstrip().split())
    d_x,d_y=map(int,sys.stdin.readline().rstrip().split())
    visit=[[0]*n for i in range(n)]

    d=deque()
    d.append([x,y,0])
    while(len(d)!=0):
        x,y,a=d.popleft()
        if x== d_x and y==d_y:
            print(a)
            break
        pos=[[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
        for px,py in pos:
            nx=x+px
            ny=y+py
            if nx>=n or nx<0 or ny>=n or ny<0 or visit[nx][ny]==1:
                continue
            visit[nx][ny]=1
            d.append([nx,ny,a+1])
    