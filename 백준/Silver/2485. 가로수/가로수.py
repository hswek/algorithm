import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))

n=int(input())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr=[]
q=int(input())
for i in range(n-1):
    m=int(input())
    arr.append(m-q)
    q=m
    
c=arr[0]
for i in range(1,len(arr)):
    c=math.gcd(c,arr[i])
result=0
#print(arr)
for i in arr:
    result+=i//c-1
    
print(result)
