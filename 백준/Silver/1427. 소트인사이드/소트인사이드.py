import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=list(input())
n.sort(reverse=True)
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#arr.sort(reverse=True)
for i in n:
    print(i,end='')
