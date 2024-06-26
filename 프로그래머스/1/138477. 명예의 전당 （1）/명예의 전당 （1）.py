from collections import deque
import bisect
def solution(k, score):
    answer = []
    o=deque()
    for i in score:
        where=bisect.bisect_right(o,i)
        o.insert(where,i)
        if len(o)>k:
            o.popleft()
        answer.append(o[0])
    return answer