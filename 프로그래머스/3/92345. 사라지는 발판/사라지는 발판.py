def rec(board,aloc,bloc,turn):
    n=len(board)
    m=len(board[0])
    arr=[[1,0],[0,-1],[-1,0],[0,1]]
    if turn == 0:
        x,y=aloc
    else:
        x,y=bloc
    can_go=False
    for i in range(4):
        nx=x+arr[i][0]
        ny=y+arr[i][1]
        if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny]==0:
            continue
        can_go=True
    if can_go==False:
        return [0,1-turn]
    if aloc[0]==bloc[0] and aloc[1]==bloc[1]:
        return [1,turn]
    can_not_win=0
    can_win=9999999999999
    is_win=False
    for i in range(4):
        nx=x+arr[i][0]
        ny=y+arr[i][1]
        if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny]==0:
            continue
        board[x][y]=0
        if turn==0:
            what,who=rec(board,[nx,ny],bloc,1)
            what+=1
            can_not_win=max(can_not_win,what)
            if who==turn:
                is_win=True
                can_win=min(can_win,what)
        else:
            what,who=rec(board,aloc,[nx,ny],0)
            what+=1
            can_not_win=max(can_not_win,what)
            if who==turn:
                is_win=True
                can_win=min(can_win,what)
        board[x][y]=1
    if is_win==True:
        return [can_win,turn]
    return [can_not_win,1-turn]
def solution(board, aloc, bloc):
    answer = rec(board,aloc,bloc,0)[0]
    return answer