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
    arr.append(list(sys.stdin.readline().rstrip().split())+[i])

arr.sort(key=lambda x:[int(x[0]),x[2]])
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#arr.sort(reverse=True)

for i in arr:
    print(i[0],i[1])
