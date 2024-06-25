import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
s=set(arr)
s2=list(s)
s2.sort()
a={}
for i in range(len(s2)):
    a[s2[i]]=i
for i in range(len(arr)):
    arr[i]=a[arr[i]]
for i in arr:
    print(i,end=' ')
