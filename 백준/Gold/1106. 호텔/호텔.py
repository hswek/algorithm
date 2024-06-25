import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
c,n=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
cache=[-1]*(c+1)
def recursive(pos):
    global n
    if pos>=c:
        return 0
    if cache[pos]!=-1:
        return cache[pos]
    result=9877654321
    for i in arr:
        #print(i)
        result=min(result, recursive(pos+i[1])+i[0])
    cache[pos]=result
    return result
print(recursive(0))