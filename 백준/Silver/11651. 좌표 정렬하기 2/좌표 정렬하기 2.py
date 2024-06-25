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
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x:[x[1],x[0]])
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#arr.sort(reverse=True)
for i in arr:
    print(i[0],i[1])
