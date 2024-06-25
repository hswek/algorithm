import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n,m=map(int,sys.stdin.readline().rstrip().split())
#n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
arr=set(arr)
arr2=set(arr2)
a=arr-arr2
b=arr2-arr
print(len(a)+len(b))
