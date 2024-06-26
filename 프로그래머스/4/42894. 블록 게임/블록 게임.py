blocks=(
    ((1,0,0),(1,1,1)),
    ((0,1),(0,1),(1,1)),
    ((1,0),(1,0),(1,1)),
    ((0,0,1),(1,1,1)),
    ((0,1,0),(1,1,1)),
)
result=0
def upper_not(board,what,max_y,max_x,min_x,b,min_y):
    d={}
    for y in range(len(b)):
        for x in range(len(b[0])):
            if b[y][x]==0:
                d[min_y+x]=True
    
    for x in range(min_y,max_y+1):
        if x in d:
            for y in range(0,max_x):
                if board[y][x]!=0 and board[y][x]!=what:
                    return False
  
    return True
def is_same_block(tmp,b):
    if len(b)!= len(tmp) or len(b[0])!=len(tmp[0]):
        return False
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]!=tmp[i][j]:
                return False
    return True
def find_block(board,x,y):
    what=board[x][y]
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    stack=[[x,y]]
    visit={}
    block=[]
    min_x=999
    min_y=999
    max_x=-1
    max_y=-1
    while len(stack):
        x,y=stack.pop()
        if (x,y) in visit:
            continue
        visit[(x,y)]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or board[nx][ny]!=what:
                continue
            stack.append([nx,ny])
            block.append([nx,ny])
            min_x=min(min_x,nx); min_y=min(min_y,ny)
            max_x=max(max_x,nx); max_y=max(max_y,ny)
    x_len=max_x-min_x+1
    y_len=max_y-min_y+1
    tmp=[[0]*y_len for __ in range(x_len)]
    for nx,ny in block:
    	tmp[nx-min_x][ny-min_y]=1
    for b in blocks:
        if is_same_block(tmp,b):
            print(tmp)
            if upper_not(board,what,max_y,max_x,min_x,b,min_y):
                for nx,ny in block:
                    board[nx][ny]=0
                return 1
    return 0
def solution(board):
    global n
    ans=0
    n=len(board)

    is_blocked=[False]*n
    for i in range(n):
        for j in range(n):
            if board[i][j]!=0:
                ans+=find_block(board,i,j)
    return ans