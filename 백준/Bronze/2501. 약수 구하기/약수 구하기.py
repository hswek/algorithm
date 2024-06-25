import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
a,b=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(1,a+1):
    if a%i==0:
        arr.append(i)
if len(arr)<b:
    print(0)
else:
    print(arr[b-1])