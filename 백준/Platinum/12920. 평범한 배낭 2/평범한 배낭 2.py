import sys
from collections import deque
import math
sys.setrecursionlimit(10**4)

#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
arr3=[]
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().rstrip().split()))
    if tmp[2]!=0:
        num=tmp[2]
        num2=tmp[2]//2
        while True:
            
            p=num-num2
            arr3.append([p*tmp[0],p * tmp[1]])
            if num==1:
                break
            num=num//2
            num2=num2//2
#print(arr3)
n=len(arr3)
cache=[[-1]* (n+1) for i in range(k+10)]
def knap_sack(k,v):
    if cache[k][v]!=-1:
        return cache[k][v]
    result=0
    if v==n:
        return 0
    if arr3[v][0]<=k:
        result=max(result,arr3[v][1]+knap_sack(k-arr3[v][0],v+1))
    result=max(result,knap_sack(k,v+1))   
    cache[k][v]=result
    return result
print(knap_sack(k,0))
#print(cache)