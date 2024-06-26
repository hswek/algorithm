import heapq
import sys
from collections import deque
def bfs(cache,board):
    x=0
    y=0
    dire=4
    cost=0
    d=deque([[x,y,dire,cost]])
    answer=[]
    arr=[[1,0],[0,1],[-1,0],[0,-1],[-999999999999,-99999999999999]]
    while len(d):
        x,y,dire,cost=d.popleft()
        if cache[dire][x][y]<cost:
            continue
        if x==len(board)-1 and y==len(board)-1:
            answer.append(cost)
        for i in range(4):
            nx=x+arr[i][0]
            ny=y+arr[i][1]
            if dire==i or dire==4:
                next_cost=cost+100
            else:
                next_cost=cost+600
            if nx<0 or nx>=len(board) or ny<0 or ny>=len(board) or cache[i][nx][ny]<next_cost or board[nx][ny]==1:
                continue
            cache[i][nx][ny]=next_cost
            d.append([nx,ny,i,next_cost])    
    return min(answer)
        
def solution(board):
    answer = 0
    sys.setrecursionlimit(10**6)
    global cache
    cache=[[[9999999999999]* len(board[0]) for i in range(len(board))] for i in range(5)]

    cache[0][0]=0
    answer=bfs(cache,board)

    return answer