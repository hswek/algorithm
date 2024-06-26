from collections import deque
def bfs(maps,start,end):
    d=deque([[0,start]])
    #print(d)
    visit=[[-1] * len(maps[0]) for i in range(len(maps))]
    arr=[[1,0],[0,-1],[-1,0],[0,1]]
    while len(d):
        distance,where=d.popleft()
        x,y=where
        #print(distance,where)
        if where[0]==end[0] and where[1]==end[1]:
            return distance
        for i in range(4):
            nx=x+arr[i][0]
            ny=y+arr[i][1]
            if nx>=len(maps) or nx<0 or ny<0 or ny>=len(maps[0]) or maps[nx][ny]=='X' or visit[nx][ny]==1:
                continue
            d.append([distance+1,[nx,ny]])
            visit[nx][ny]=1
    return -1
def solution(maps):
    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start=[i,j]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='L':
                laber=[i,j]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='E':
                end=[i,j]
    d1=bfs(maps,start,laber)
    d2=bfs(maps,laber,end)
    #print(d1,d2)
    if d1==-1 or d2==-1:
        return -1
    return d1+d2
    return answer