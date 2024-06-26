def erase(m,n,board):
    result=0
    visit=[]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]!=-1 and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j+1] and board[i][j]==board[i+1][j]:
                visit.append(i*100+j)
                visit.append((i+1)*100+j)
                visit.append(i*100+j+1)
                visit.append((i+1)*100+j+1)
    for i in visit:
        board[i//100][i%100]=-1
    return len(set(visit))
def block_down(m,n,board):
    for j in range(n):
        while True:
            is_go_down=False
            for i in range(m-2,-1,-1):
                if board[i][j]!=-1 and board[i+1][j]==-1:
                    board[i+1][j]=board[i][j]
                    board[i][j]=-1
                    is_go_down=True
            if is_go_down==False:
                break
    
def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i]=list(board[i])
    while True:
        tmp=erase(m,n,board)
        if tmp==0:
            ##for i in board:
            #    print(i)
            return answer
        else:
            answer+=tmp
            block_down(m,n,board)

    return answer