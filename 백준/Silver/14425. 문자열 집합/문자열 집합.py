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

for i in range(n):
    s=input()
    d[s]=1

result=0
for _ in range(m):
    i=input()
    if i in d:
        result+=1
print(result)
    