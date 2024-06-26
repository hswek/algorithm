import sys
def recursive(n):
    global cache
    if n==1:
        return 1
    if n==2:
        return 2
    if n==0:
        return 1
    if cache[n]!=-1:
        return cache[n]
    
    tmp=recursive(n-2)% 1000000007+recursive(n-1)% 1000000007
    cache[n]=tmp
    return tmp% 1000000007
def solution(n):
    sys.setrecursionlimit(10**5)
    answer = 0
    global cache
    cache=[-1]*(n+20)
    answer=recursive(n)
    return answer% 1000000007