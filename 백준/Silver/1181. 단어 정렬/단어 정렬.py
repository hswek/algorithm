import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

arr.sort(key=lambda x:[len(x),x])
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#arr.sort(reverse=True)
d={}
for i in arr:
    if i not in d:
        print(i)
        d[i]=0