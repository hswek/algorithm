import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(5):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
print(sum(arr)//5)
print(arr[2])
