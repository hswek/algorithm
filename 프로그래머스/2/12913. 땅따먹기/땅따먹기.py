def rec(idx,prev,land):
    global cache
    if idx==m:
        return 0
    else:
        if cache[idx][prev]!=-1:
            return cache[idx][prev]
        a=-1
        for i in range(4):
            if i==prev:
                continue
            a=max(a,land[idx][i]+rec(idx+1,i,land))
        cache[idx][prev]=a
        return a
import sys
def solution(land):
    sys.setrecursionlimit(10**6)
    answer = 0
    global m
    m=len(land)
    global cache
    cache=[[-1]*10 for i in range(len(land)+10)]
    return rec(0,-1,land)

