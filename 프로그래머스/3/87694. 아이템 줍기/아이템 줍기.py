def fill(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            arr[i][j]=1
def unfill(arr):
    arr2=[[0] * 103 for i in range(103)]
    d=[[1,0],[0,-1],[-1,0],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for i in range(102):
        for j in range(102):
            if arr[i][j]==1:
                is_true=False
                for dx,dy in d:
                    nx=i+dx
                    ny=j+dy
                    if nx<0 or ny<0:
                        continue
                    if arr[nx][ny]==0:
                        is_true=True
                arr2[i][j]=0
                if is_true==True:
                    arr2[i][j]=1
    return arr2
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    global arr
    answer = 0
    arr=[[0] * 103 for i in range(103)]
    visit=[[0] * 103 for i in range(103)]
    for x1,y1,x2,y2 in rectangle:
        x1*=2
        x2*=2
        y1*=2
        y2*=2
        fill(x1,y1,x2,y2)
    arr=unfill(arr)
    dxy=[[1,0],[0,-1],[-1,0],[0,1]]
    d=deque([[characterX*2,characterY*2,0]])
    while len(d):
        x,y,cost=d.popleft()
        #print(x,y)
        if x==itemX*2 and y==itemY*2:
            return cost//2
        for dx,dy in dxy:
            nx=x+dx
            ny=y+dy
            if nx<0 or ny<0 or arr[nx][ny]==0 or visit[nx][ny]==1:
                continue
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
            
    return answer