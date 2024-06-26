import bisect
from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a=deque(A)
    b=deque(B)
    while len(a):
        #if a[0]>b[-1]:
        #    a.popleft()
        #    b.pop()
        #   continue
        tmp=a.popleft()
        where=bisect.bisect_right(b,tmp)
        if where==len(b):
            b.popleft()
            continue
        if b[where]>tmp:
            b.remove(b[where])
            answer+=1
        elif b[where]==tmp:
            b.popleft()
        
    return answer