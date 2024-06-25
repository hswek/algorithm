import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(3):
    arr=[]
    n=int(sys.stdin.readline().rstrip())
    for j in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))
    s=sum(arr)
    if s>0:
        print('+')
    if s<0:
        print('-')
    if s==0:
        print(0)