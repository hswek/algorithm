def s(b,t,r1,c1,r2,c2,degree):
    if t==1:
        degree=-degree
    b[r1][c1]+=degree
    if c2+1<len(b[0]):
        b[r1][c2+1]-=degree
    if r2+1<len(b):
        b[r2+1][c1]-=degree
    if r2+1<len(b) and c2+1<len(b[0]):
        b[r2+1][c2+1]+=degree
def go_row(b):
    for i in range(len(b)):
        for j in range(1,len(b)):
            b[i][j]+=b[i][j-1]
def go_column(b):
    for i in range(1,len(b)):
        for j in range(len(b)):
            b[i][j]+=b[i-1][j]
import copy
def solution(board, skill):
    answer = 0
    tmp_board=copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp_board[i][j]=0
    for t,r1,c1,r2,c2,degree in skill:
        s(tmp_board,t,r1,c1,r2,c2,degree)
        
    go_row(tmp_board)
    go_column(tmp_board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            #print(i,j,board[i][j],tmp_board[i][j])
            if board[i][j]+tmp_board[i][j]>=1:
                answer+=1

    return answer