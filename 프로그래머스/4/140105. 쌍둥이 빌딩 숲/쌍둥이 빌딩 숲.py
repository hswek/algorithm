from itertools import combinations
import sys; sys.setrecursionlimit(1000000)
        
def solution(n, count):
    d={}
    def rec(n,c):
        if n==1 and c==1:
            return 1
        if n==0:
            return 0
        if c==0:
            return 0
        s=str(n)+"_"+str(c)
        if s in d:
            return d[s]
        tmp=rec(n-1,c-1)+rec(n-1,c)*2*(n-1)%1000000007
        d[s]=tmp% 1000000007
        return tmp% 1000000007

    return rec(n,count)