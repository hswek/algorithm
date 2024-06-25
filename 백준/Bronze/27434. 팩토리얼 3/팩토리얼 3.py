import sys
from collections import deque
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
if n==0:
    print(1)
else:
    r=1
    for i in range(1,n+1):
        r=r*i 
    print(r)