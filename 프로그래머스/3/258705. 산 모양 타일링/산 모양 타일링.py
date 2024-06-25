import sys
sys.setrecursionlimit(10**6)
mem=[[-1]*2 for _ in range(100011)]
def rec(n,tops,plus):
    if mem[n][plus]!=-1:
        return mem[n][plus]
    if n==0:
        return 1
    tmp=0
    if plus==True:
        tmp+=rec(n,tops,False)%10007
        tmp+=rec(n-1,tops,True)%10007
    if plus==False:
        tmp+=rec(n-1,tops,True)%10007
        tmp+=rec(n-1,tops,False)%10007
        if tops[n-1]==1:
            tmp+=rec(n-1,tops,True)%10007
    mem[n][plus]=tmp
    return tmp
def solution(n, tops):
    answer = 0
    return rec(n,tops,True)%10007