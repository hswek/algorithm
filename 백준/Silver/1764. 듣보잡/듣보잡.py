import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n,m=map(int,sys.stdin.readline().rstrip().split())
#n=int(input())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
d={}

for i in range(1,n+1):
    name=input()
    d[name]=str(i)
arr=[]
for i in range(m):
    a=input()
    if a in d:
        arr.append(a)
arr.sort()
print(len(arr))
for i in arr:
    print(i)
