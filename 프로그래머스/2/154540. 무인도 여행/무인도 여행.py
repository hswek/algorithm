import sys
def dfs(visit,maps,x,y):
    direc=[[1,0],[0,-1],[-1,0],[0,1]]
    nx=x
    ny=y
    visit[x][y]=1
    if maps[x][y]!='X':
        tmp=int(maps[x][y])
    for i in range(4):
        nx=x+direc[i][0]
        ny=y+direc[i][1]
        if nx>=len(maps) or ny>=len(maps[0]) or nx<0 or ny<0 or visit[nx][ny]==1 or maps[nx][ny]=='X':
            continue
        tmp+=dfs(visit,maps,nx,ny)
    return tmp
def solution(maps):
    sys.setrecursionlimit(10**6)
    answer = []
    visit= [[0]*len(maps[0]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visit[i][j]==0 and maps[i][j]!='X':
                answer.append(dfs(visit,maps,i,j))
    answer.sort()
    if len(answer)==0:
        return [-1]
    return answer