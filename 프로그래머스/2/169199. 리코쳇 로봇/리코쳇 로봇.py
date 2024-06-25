from collections import deque
def get_next(x,y,board):
    #print(x,y)
    arr=[[1,0],[0,-1],[-1,0],[0,1]]
    result=[]
    for dx,dy in arr:
        nx=x
        ny=y
        while nx>=0 and ny>=0 and nx<len(board) and ny<len(board[0]) and board[nx][ny]!='D':
            nx+=dx
            ny+=dy
        nx-=dx
        ny-=dy
        if nx==x and ny==y:
            continue
        result.append([nx,ny])
    return result
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='R':
                x=i
                y=j
            if board[i][j]=='G':
                gx=i
                gy=j
    d=deque([[x,y,0]])
    visit=[[-1]*len(board[0]) for i in range(len(board))]
    while len(d):
        x,y,dis=d.popleft()

        if gx==x and gy==y:
            return dis
        arr=get_next(x,y,board)
        for nx,ny in arr:
            #print(nx,ny)
            if visit[nx][ny]!=-1:
                continue
            d.append([nx,ny,dis+1])
            visit[nx][ny]=1
    return -1