d=[]
def is_finished(board):
    for i in board:
        if i=='OOO':
            return True
        elif i=='XXX':
            return True
    for j in range(3):
        if board[0][j]+board[1][j]+board[2][j]=='OOO':
            return True
        if board[0][j]+board[1][j]+board[2][j]=='XXX':
            return True
    if board[0][0]+board[1][1]+board[2][2]=='OOO':
        return True
    if board[0][0]+board[1][1]+board[2][2]=='XXX':
        return True
    if board[2][0]+board[1][1]+board[0][2]=='OOO':
        return True
    if board[2][0]+board[1][1]+board[0][2]=='XXX':
        return True
    '''
    a=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='.':
                a=1
                break
    if a==0:
        return True'''
    return False
def dfs(board,turn):
    global d
    for i in range(3):
        origin_s=board[i]
        for j in range(3):
            if origin_s[j]!='.':
                continue
            s=list(origin_s)
            s[j]=turn
            s=''.join(s)
            board[i]=s
            d.append(board.copy())#=True
            if is_finished(board)!=True:
                #print(1)
                if turn=='O':
                    dfs(board,'X')
                else:
                    dfs(board,'O')
            s=list(origin_s)
            s[j]='.'
            s=''.join(s)
            board[i]=s
def is_same(b1,b2):
    for i in range(3):
        if b1[i]!=b2[i]:
            return False
    return True
def solution(board):
    global d
    d=[]
    
    tmp_board=['...' ,'...','...']
    dfs(tmp_board,'O')
    #print(d[:15])
    tmp_board=['...' ,'...','...']
    d.append(tmp_board)
    #print(d[-1])
    for bo in d:
        if is_same(bo,board):
            return 1
    return 0