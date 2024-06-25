import sys
from collections import deque
import heapq
import bisect
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
cache=[-1]*(n+1)
arr2=[-1]*(n+2)
def lis(start):
    global n
    if cache[start]!=-1:
        return cache[start]
    result=0
    tmp=-1
    for i in range(start+1,n):
        if start==-1 or arr[start]<arr[i]:
            if result<lis(i):
                tmp=i        
                result=lis(i)
    arr2[start+1]=tmp   
    cache[start]=1+result
    return cache[start]
print(lis(-1)-1)
start=0
while True:
    #print(arr2)
    #break
    if arr2[start]==-1:
        break
    print(arr[arr2[start]],end=' ')
    start=arr2[start]+1
    #print(start)
    