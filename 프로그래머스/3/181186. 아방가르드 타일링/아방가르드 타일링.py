def rec(n,cache):
    if n==2:
        return 3
    if n==1:
        return 1
    if n==0:
        return 1
    if n<0:
        return 0
    if n==3:
        return 10
    if cache[n]!=-1:
        return cache[n]
    a=2
    if n%3==0:
        a=4
    result=(rec(n-1,cache)%1000000007+rec(n-2,cache)*2%1000000007+rec(n-3,cache)*6%1000000007+rec(n-4,cache)-rec(n-6,cache)+1000000007)%1000000007

    cache[n]=result%1000000007
    return result%1000000007
import sys
def solution(n):
    sys.setrecursionlimit(10**7)
    cache=[-1]*(n+111)
    answer = rec(n,cache)
    return answer%1000000007