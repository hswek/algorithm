import sys
import bisect
d={}

def rec(want):
    if want not in d:
        d[want]=want+1
        return want
    empt=rec(d[want])
    d[want]=empt+1
    return empt
def solution(k, room_number):
    sys.setrecursionlimit(10**8)
    answer = []
    for want in room_number:
        res=rec(want)
        answer.append(res)
        
    return answer