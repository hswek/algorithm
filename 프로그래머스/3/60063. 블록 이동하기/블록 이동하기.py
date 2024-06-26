from collections import deque
def solution(board):
    answer = 0
    n=len(board)
    d=deque([[0,0,0,0]])
    visit=[[[0]*2 for j in range(n)] for i in range(n)]
    arr=[[1,0],[0,-1],[-1,0],[0,1]]
    while len(d):
        x,y,di,cost=d.popleft()
        if di==0 and x==n-1 and y==n-2:
            return cost
        if di==1 and x==n-2 and y==n-1:
            return cost
        for i in range(4):
            nx=x+arr[i][0]
            ny=y+arr[i][1]
            if di==0:
                if nx<0 or ny<0 or nx>=n or ny>=n-1:
                    continue
                if board[nx][ny+1]==1 or board[nx][ny]==1:
                    continue
                if visit[nx][ny][di]==1:
                    continue
                d.append([nx,ny,di,cost+1])
                visit[nx][ny][di]=1
            if di==1:
                if nx<0 or ny<0 or nx>=n-1 or ny>=n:
                    continue
                if board[nx+1][ny]==1 or board[nx][ny]==1:
                    continue
                if visit[nx][ny][di]==1:
                    continue
                d.append([nx,ny,di,cost+1])
                visit[nx][ny][di]=1
        nx=x
        ny=y
        if di==0:
            if nx!=n-1 and board[nx+1][ny]==0 and board[nx+1][ny+1]==0:
                if visit[nx][ny+1][1]==0:
                    visit[nx][ny+1][1]=1
                    d.append([nx,ny+1,1,cost+1])
                if visit[nx][ny][1]==0:
                    visit[nx][ny][1]=1
                    d.append([nx,ny,1,cost+1])
            if nx!=0 and board[nx-1][ny]==0 and board[nx-1][ny+1]==0:
                if visit[nx-1][ny][1]==0:
                    visit[nx-1][ny][1]=1
                    d.append([nx-1,ny,1,cost+1])
                if visit[nx-1][ny+1][1]==0:
                    visit[nx-1][ny+1][1]=1
                    d.append([nx-1,ny+1,1,cost+1])
        if di==1:
            if ny!=0 and board[nx][ny-1]==0 and board[nx+1][ny-1]==0:
                if visit[nx][ny-1][0]==0:
                    visit[nx][ny-1][0]=1
                    d.append([nx,ny-1,0,cost+1])
                if visit[nx+1][ny-1][0]==0:
                    visit[nx+1][ny-1][0]=0
                    d.append([nx+1,ny-1,0,cost+1])
            if ny!=n-1 and board[nx][ny+1]==0 and board[nx+1][ny+1]==0:
                if visit[nx][ny][0]==0:
                    visit[nx][ny][0]=0
                    d.append([nx,ny,0,cost+1])
                if visit[nx+1][ny][0]==0:
                    visit[nx+1][ny][0]=0
                    d.append([nx+1,ny,0,cost+1])
    return answer