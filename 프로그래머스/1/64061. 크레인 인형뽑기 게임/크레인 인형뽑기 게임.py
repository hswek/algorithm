from collections import deque
def solution(board, moves):
    s=deque()
    answer = 0
    for move in moves:
        tmp=-1
        for i in range(len(board)):
            if board[i][move-1]!=0:
                tmp=board[i][move-1]
                board[i][move-1]=0
                break
        
        if tmp==-1:
            continue
        else:
            if len(s)==0:
                s.append(tmp)
            elif s[-1]!=tmp:
                s.append(tmp)
            else:
                answer+=1
                s.pop()
        
    return answer*2