import sys
def rec(n):
    global cache
    if cache[n]!=-1:
        return cache[n]
    if n==1:
        return 0
    if n==0:
        return 1
    if n==2:
        return 3
    if n==3:
        return 0
    #if n==4:
    #    return 11
    tmp=rec(n-2)*3
    for i in range(4,n+1,2):
        tmp=tmp+rec(n-i)*2
    cache[n]=tmp%1000000007
    return cache[n]
def solution(n):
    sys.setrecursionlimit(10**6)
    answer = 0
    global cache
    cache=[-1]*(n+10)
    return rec(n)%1000000007