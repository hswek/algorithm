from collections import deque
def solution(maps):
    direction=[[1,0],[0,-1],[-1,0],[0,1]]
    d=deque()
    d.append([0,0,0])
    visit=[[-1]*len(maps[0]) for i in range(len(maps))]
    while len(d):
        x,y,distance=d[0]
        d.popleft()
        #print(x,y)
        if x==len(maps)-1 and y==len(maps[0])-1:
            return distance+1
        for i in range(4):
            nx=x+direction[i][0]
            ny=y+direction[i][1]
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) or maps[nx][ny]==0:
                continue
            if visit[nx][ny]==-1:
                visit[nx][ny]=1
                d.append([nx,ny,distance+1])
    answer = 0
    return -1