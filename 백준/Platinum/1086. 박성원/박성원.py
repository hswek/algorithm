import sys
from collections import deque
import math
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
k=int(sys.stdin.readline().rstrip())
cache=[[-1] * (k) for _ in range(1<<n)]
cache2=[[-1] * (n) for _ in range(k)]
r=0
def recursive(  a , b   ):
    global k
    if cache[a][b]!=-1:
        return cache[a][b]
    if a==(1<<n)-1:
        if b==0:
            return 1
        else:
            return 0
    #print(a,b)

    result=0
    for i in range(n):
        if 1<<i & a == 1<<i:
            continue
        else:
            if cache2[b][i]!=-1:
                c=cache2[b][i]
            else:
                c=(b*(10 ** len(arr[i]))  + int(arr[i]) )% k
                cache2[b][i]=c
            d=recursive(a | 1<<i, c )
            result+=d

    cache[a][b]=result
    return result
a=recursive(0,0)
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

c=fact(n)
e=math.gcd(a,c)
a_t=a//e
c_t=c//e
print(a_t,'/',c_t,sep='')
