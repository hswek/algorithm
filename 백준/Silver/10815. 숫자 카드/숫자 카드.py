import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
n2=int(input())
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
d={}
for i in arr:
    d[i]=1
for i in arr2:
    if i in d:
        print(1,end=' ')
    else:
        print(0,end=' ')
    