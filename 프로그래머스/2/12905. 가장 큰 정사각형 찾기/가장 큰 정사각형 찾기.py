import sys
def rec(board,x,y,l,l2):
    global cache
    if board[x][y]==0:
        cache[x][y]=0
        return 0
    if x!=0 and cache[x-1][y]==-1:
        #print('before',x,y,cache[x-1][y])
        rec(board,x-1,y,l,l2)
        #print('after',x,y,cache[x-1][y])
    if y!=0 and cache[x][y-1]==-1:
        rec(board,x,y-1,l,l2)
    if x!=0 and y!=0 and cache[x-1][y-1]==-1:
        rec(board,x-1,y-1,l,l2)
    if x!=0:
        a=cache[x-1][y]
        #print(a)
    else:
        a=0
    if y!=0:
        b=cache[x][y-1]
        #print(b)
    else:
        b=0
    if y!=0 and x!=0: 
        c=cache[x-1][y-1]
        #print(c)
    else:
        c=0
    cache[x][y]=min([a,b,c])+1
    return cache[x][y]
    
def solution(board):
    m=0
    sys.setrecursionlimit(10**6)
    global cache
    cache=[[-1] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                continue
            tmp=rec(board,i,j,len(board),len(board[0]))
            #print(i,j,tmp)
            m=max(tmp,m)
    return m**2