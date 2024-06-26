from collections import deque
def solution(order):
    answer = 0
    d=deque()
    box=[-1]*len(order)
    for i in range(len(order)):
        box[order[i]-1]=i+1
    now=1
    for b in box:
        if now==b:
            now+=1
            answer+=1
        else:
            while len(d):
                if d[0]!=now:
                    break
                if d[0]==now:
                    now+=1
                    answer+=1
                    d.popleft()
            if b==now:
                now+=1
                answer+=1
            else:
                d.appendleft(b)
    while len(d):
        if d[0]!=now:
            break
        if d[0]==now:
            now+=1
            answer+=1
            d.popleft()

    return answer