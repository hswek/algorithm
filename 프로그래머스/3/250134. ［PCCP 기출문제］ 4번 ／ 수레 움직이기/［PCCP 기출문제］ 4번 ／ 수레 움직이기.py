dx=[1,0,-1,0]
dy=[0,-1,0,1]
import copy

def find_where(maze,what):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==what:
                return (i,j)
ans=99987654321
def dfs(maze,red_visit,blue_visit,red,blue,result):
    global ans
    if red==red_goal and blue==blue_goal:
        ans=min(ans,result)
        return
    red_cand=[]
    blue_cand=[]
    if red!=red_goal:
        x,y=red[0],red[1]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or nx>=mx or ny>=my\
            or maze[nx][ny]==5 or red_visit[nx][ny]==1:
                continue
            red_cand.append((nx,ny))
    else:
        red_cand=[red_goal]
    if blue!=blue_goal:
        x,y=blue[0],blue[1]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or nx>=mx or ny>=my\
            or maze[nx][ny]==5 or blue_visit[nx][ny]==1 :
                continue
            blue_cand.append((nx,ny))
    else:
        blue_cand=[blue_goal]
    for next_red in red_cand:
        for next_blue in blue_cand:
            if next_red==next_blue:
                continue
            if next_blue==red and next_red==blue:
                continue
            red_visit[next_red[0]][next_red[1]]=1
            blue_visit[next_blue[0]][next_blue[1]]=1
            dfs(maze,red_visit,blue_visit,next_red,next_blue,result+1)
            red_visit[next_red[0]][next_red[1]]=0
            blue_visit[next_blue[0]][next_blue[1]]=0
def solution(maze):
    global mx,my,red_goal,blue_goal
    mx=len(maze)
    my=len(maze[0])
    answer = 0
    red=find_where(maze,1)
    blue=find_where(maze,2)
    red_goal=find_where(maze,3)
    blue_goal=find_where(maze,4)
    red_visit=[[0]*my for i in range(mx)]
    blue_visit=[[0]*my for i in range(mx)]
    red_visit[red[0]][red[1]]=1
    blue_visit[blue[0]][blue[1]]=1
    dfs(maze,red_visit,blue_visit,red,blue,0)
    if ans!=99987654321:
        return ans
    return 0