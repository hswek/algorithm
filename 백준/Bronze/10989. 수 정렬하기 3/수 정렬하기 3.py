import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=[0]*10001
for i in range(n):
    arr[int(sys.stdin.readline().rstrip())]+=1
for i in range(1,10001):
    for j in range(arr[i]):
        print(i)