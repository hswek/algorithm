import sys
from collections import deque
import math
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
cache=[-1]* (1<<n+2) 
    
def recursive(i,j):
    global n
    if i==n:
        return 0
    if cache[j]!=-1:
        return cache[j]
    result=987654321
    for z in range(n):
        if 1<<z & j == 1<<z:
            continue
        #print(i,z)
        tmp= recursive( i + 1 , j |  1<<z) + arr[i][z]
        #print(tmp,i,z)
        result=min(result,tmp )
    cache[j]=result
    return result
print(recursive(0,0))
    