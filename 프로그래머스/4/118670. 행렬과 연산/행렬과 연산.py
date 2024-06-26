from collections import deque
def solution(rc, operations):
    answer = []
    r=len(rc); c=len(rc[0])
    row=[i for i in range(r)]
    for i in range(r):
        row[i]=deque(rc[i][1:-1])
    row=deque(row)
    col_left=deque([rc[i][0] for i in range(r)])
    col_right=deque([rc[i][-1] for i in range(r)])
    
    for op in operations:
        if op=="ShiftRow":
            row.appendleft(row.pop())
            col_left.appendleft(col_left.pop())
            col_right.appendleft(col_right.pop())
        else:
            
            row[-1].append(col_right.pop())
            row[0].appendleft(col_left.popleft())
            col_right.appendleft(row[0].pop())
            col_left.append(row[-1].popleft())
    for _ in range(r):
        tmp=[]
        tmp.append(col_left.popleft())
        tmp.extend(list(row.popleft()))
        tmp.append(col_right.popleft())
        answer.append(tmp)
    return answer