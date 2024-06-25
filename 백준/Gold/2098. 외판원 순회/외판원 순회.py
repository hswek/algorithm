import sys
from collections import deque
import math
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
#cache=[[-1]* (1<<n+2) for i in range(17)]
    
def recursive(i,j,start,how):
    global n
    #print(i,j,start,how)
    if cache[i][j]!=-1:
        return cache[i][j]
    if how==n-1:
        if arr[i][start]==0:
            return 987654111
        else:
            return arr[i][start]
    result=987654111
    for z in range(n):
        if z==start or arr[i][z]==0 or (1<<z) & j == 1<<z:
            continue
        #print(i,z)
        tmp= recursive( z , j |  1<<z,start,how+1) + arr[i][z]
        #print(tmp,i,z)
        result=min(result,tmp )
    cache[i][j]=result
    return result
r=987654111
for i in range(n):
    cache=[[-1]* (1<<n+2) for i in range(17)]
    
    r=min(r, recursive(i,0,i,0))
    #print(r,i)
print(r)
    