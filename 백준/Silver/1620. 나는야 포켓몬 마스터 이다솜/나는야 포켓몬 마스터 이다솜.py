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
d2={}

for i in range(1,n+1):
    name=input()
    d[str(i)]=name
    d2[name]=str(i)

for i in range(m):
    a=input()
    if a in d:
        print(d[a])
    else:
        print(d2[a])