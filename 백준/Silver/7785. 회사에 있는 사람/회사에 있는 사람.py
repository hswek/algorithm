import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
d={}

for i in range(n):
    name,e=input().split()
    if e=='enter':
        d[name]=1
    else:
        d[name]=0
    

arr=[]
for a,b in d.items():
    if b==1:
        arr.append(a)
arr.sort(reverse=True)
for i in arr:
    print(i)
    