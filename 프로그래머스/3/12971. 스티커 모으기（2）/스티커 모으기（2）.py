def rec(now,final,sticker):
    global n
    if now==n-1 and final==True:
        return 0
    #print(now,final)
    if now>=n:
        return 0
    if cache[now][final]!=-1:
        return cache[now][final]
    if now==0:
        a=rec(now+2,True,sticker)+sticker[now]
    else:
        a=rec(now+2,final,sticker)+sticker[now]
    b=rec(now+1,final,sticker)
    cache[now][final]=max(a,b)
    return max(a,b)
import sys
def solution(sticker):
    global n,cache
    sys.setrecursionlimit(10**6)
    answer = 0
    n=len(sticker)
    cache=[[-1]*2 for i in range(len(sticker))]
    answer=rec(0,False,sticker)
    #print(cache)
    return answer