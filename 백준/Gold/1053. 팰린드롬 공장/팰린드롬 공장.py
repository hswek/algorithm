import sys
from collections import deque
import heapq
import math
from itertools import combinations
#sys.setrecursionlimit(10**5)
#n,l=map(int,sys.stdin.readline().rstrip().split())
s=sys.stdin.readline().rstrip()
def dp(start,end,s):
    #print(start,end)
    if cache[start][end]!=-1:
        return cache[start][end]
    if end-start==1:
        return 0
    elif end-start==2:
        if s[start]==s[start+1]:
            return 0
        else:
            return 1
    if s[start]==s[end-1]:
        r=dp(start+1,end-1,s)
    else:
        r1=dp(start,end-1,s)+1
        r2=dp(start+1,end,s)+1
        r3=dp(start+1,end-1,s)+1
        r=min(r1,r2,r3)
    cache[start][end]=r
    return r
ans=999999999999  
cache=[[-1]*(len(s)+1) for i in range(len(s)+1)]
ans=min(ans,dp(0,len(s),s))
for x,y in combinations(range(len(s)),2):
    next_s=list(s)
    next_s[x],next_s[y]=next_s[y],next_s[x]
    next_s="".join(next_s)
    cache=[[-1]*(len(s)+1) for i in range(len(s)+1)]
    now=dp(0,len(s),next_s)
    ans=min(ans,now+1)
print(ans)
    