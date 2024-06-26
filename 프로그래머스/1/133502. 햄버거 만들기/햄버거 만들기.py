from collections import deque
def solution(ingredient):
    answer = 0
    d=deque()
    for i in ingredient:
        d.appendleft(i)
        if len(d)>=4:
            if d[0]==1 and d[1]==3 and d[2]==2 and d[3]==1:
                for i in range(4):
                    d.popleft()
                answer+=1
    return answer