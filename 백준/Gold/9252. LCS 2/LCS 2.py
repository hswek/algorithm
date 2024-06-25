import sys
from collections import deque
import heapq
import bisect
sys.setrecursionlimit(10**5)
a=input()
b=input()
cache=[[-1]*(len(b)+1) for i in range(len(a)+1)]
def recursive(a_start,b_start):
    global a,b
    if cache[a_start][b_start]!=-1:
        return cache[a_start][b_start]
    if a_start==len(a) or b_start==len(b):
        return 0
    if a[a_start]==b[b_start]:
        cache[a_start][b_start]=1+recursive(a_start+1,b_start+1)
        return cache[a_start][b_start]
    else:
        cache[a_start][b_start]=max(recursive(a_start+1,b_start),recursive(a_start,b_start+1))
        return cache[a_start][b_start]
s=recursive(0,0)
print(s)
n=0
m=0
result=''
#print(cache)

while(n<len(a) and m<len(b)):
    #print(n,m)
    if cache[n][m]==cache[n][m+1]:
        m+=1
    elif cache[n][m]==cache[n+1][m]:
        n+=1
    else:
        if cache[n][m]==0:
            break
        result=result+a[n]
        n+=1
        m+=1
        

print(result)
        