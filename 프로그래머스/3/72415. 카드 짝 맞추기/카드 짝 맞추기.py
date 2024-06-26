import copy
from itertools import permutations
from collections import deque
def po(r,c,gx,gy,board,cache):
    e=[]
    for i in board:
        e.extend(i)
    e=tuple(e)
    if e in cache:
        if gy+gx*4+c*16+r*64 in cache[e]:
            return cache[e][gy+gx*4+c*16+r*64]
    else:
        cache[e]={}
    d=deque([[r,c,0]])
    visit=[[0]*4 for i in range(4)]
    visit[r][c]=1
    a=[[0,1],[-1,0],[0,-1],[1,0]]
    while len(d):
        x,y,cost=d.popleft()
        if x==gx and y==gy:
            cache[e][gy+gx*4+c*16+r*64]=cost
            return cost
        for i in range(4):
            nx=x+a[i][0]
            ny=y+a[i][1]
            if nx<0 or ny<0 or nx>=len(board) or ny>=len(board[0]) or visit[nx][ny]==1:
                continue
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
        nx,ny=x,y+1
        while ny<len(board[0]) and board[nx][ny]==0:
            ny+=1
        if ny==len(board[0]):
            ny-=1
        if visit[nx][ny]==0:
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
        nx,ny=x,y-1
        while ny>=0 and board[nx][ny]==0:
            ny-=1
        if ny==-1:
            ny=0
        if visit[nx][ny]==0:
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
        nx,ny=x+1,y
        while nx<len(board) and board[nx][ny]==0:
            nx+=1
        if nx==len(board):
            nx-=1
        if visit[nx][ny]==0:
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
        nx,ny=x-1,y
        while nx>=0 and board[nx][ny]==0:
            nx-=1
        if nx==-1:
            nx=0
        if visit[nx][ny]==0:
            visit[nx][ny]=1
            d.append([nx,ny,cost+1])
    return -1
def get_distance(r,c,board,candidate,cache):
    result=0
    for nx,ny in candidate:
        tmp=po(r,c,nx,ny,board,cache)
        result+=tmp

        board[nx][ny]=0
        r,c=nx,ny
    return result

def get_arr(arr,origin,d):
    global aa
    if len(origin)==0:
        aa.append(arr)
        return 
    tmp=copy.deepcopy(arr)
    tmp.append(d[origin[0]][0])
    tmp.append(d[origin[0]][1])
    get_arr(tmp,origin[1:],d)
    tmp=copy.deepcopy(arr)
    tmp.append(d[origin[0]][1])
    tmp.append(d[origin[0]][0])
    get_arr(tmp,origin[1:],d)
def solution(board, r, c):
    global answer
    answer = 9999999999
    tmp=[]
    d={}
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0 and board[i][j] not in tmp:
                d[board[i][j]]=[(i,j)]
                tmp.append(board[i][j])
            elif board[i][j]!=0:
                d[board[i][j]].append((i,j))   
    #print(d)
    arr=list(permutations(tmp,len(tmp)))
    global aa
    aa=[]
    cache={}
    for a in arr:
        get_arr([],a,d)
        #print(len(aa))
    for candidate in aa:
        answer=min(answer,get_distance(r,c,copy.deepcopy(board),candidate,cache)+len(candidate))
    return answer