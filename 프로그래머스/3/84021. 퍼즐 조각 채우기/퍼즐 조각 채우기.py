from collections import deque
def rotate(block):
    tmp=[[0] * len(block) for i in range(len(block[0]))]
    for i in range(len(block)):
        for j in range(len(block[0])):
            tmp[j][-1-i]=block[i][j]
    return tmp
def find_block(table):
    visit=[[-1] *len(table[0]) for i in range(len(table))]
    arr=[]
    dxdy=[[0,1],[-1,0],[0,-1],[1,0]]
    now=1
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j]==1 and visit[i][j]==-1:
                d=deque([[i,j]])
                visit[i][j]=now
                tmp=[[i,j]]
                while len(d):
                    x,y=d.popleft()
                    for z in range(4):
                        nx,ny=x+dxdy[z][0],y+dxdy[z][1]
                        if nx<0 or ny<0 or nx>=len(table) or ny>=len(table) or visit[nx][ny]!=-1 or table[nx][ny]==0:
                            continue
                        visit[nx][ny]=now
                        tmp.append([nx,ny])
                        d.append([nx,ny])
                now+=1
                arr.append(tmp)
    b_arr=[]
    for b in arr:
        tmp2=[]
        minx=min(b,key=lambda x:x[0])[0]
        miny=min(b,key=lambda x:x[1])[1]
        maxx=max(b,key=lambda x:x[0])[0]
        maxy=max(b,key=lambda x:x[1])[1]
        tmp=[[0] * (maxy-miny+1) for i in range(maxx-minx+1)]
        for x,y in b:
            tmp[x-minx][y-miny]=1
        tmp2.append(tmp)
        for i in range(3):
            tmp2.append(rotate(tmp2[-1]))
        b_arr.append(tmp2)
    return b_arr
def push(i,j,board,block):
    d=[[1,0],[0,-1],[-1,0],[0,1]]
    for ii in range(len(block)):
        for jj in range(len(block[0])):
            if block[ii][jj]==0:
                continue
            if board[i+ii][j+jj]!=0:
                return False
            for z in range(4):
                nx=i+ii+d[z][0]
                ny=j+jj+d[z][1]
                if nx<0 or ny<0 or nx>=len(board) or ny>=len(board[0]):
                    continue
                n1=ii+d[z][0] 
                n2=jj+d[z][1]
                if (n1>=len(block) or n2>=len(block[0]) or n1<0 or n2<0):
                    if board[nx][ny]==0:
                        return False
                else:
                    if block[n1][n2]==0 and board[nx][ny]==0:
                        return False
    s=0
    for ii in range(len(block)):
        for jj in range(len(block[0])):
            if block[ii][jj]==1:
                board[i+ii][j+jj]=1
                s+=1

    return s
def is_true(board,block):
    for i in range(len(board)-len(block)+1):
        for j in range(len(board[0])-len(block[0])+1):
            tmp=push(i,j,board,block)
            if tmp:
                return tmp
    return False
def solution(game_board, table):
    answer = 0
    b_arr=find_block(table)
    for rotate_block in b_arr:
        for block in rotate_block:
            tmp=is_true(game_board,block)
            if tmp:
                answer+=tmp
                break
    return answer