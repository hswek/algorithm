import sys
def recursive(n):
    if n==1:
        return 1
    if n==0:
        return 1
    if n<0:
        return 0
    if cache[n]!=-1:
        return cache[n]
    else:
        a=recursive(n-1)
        b=recursive(n-2)
        cache[n]=a+b
        return a+b
def solution(n):
    sys.setrecursionlimit(10**7)
    answer = 0
    global cache
    cache=[-1]*(n+1)
    answer=recursive(n)%1234567
    return answer