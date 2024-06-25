import sys
from collections import deque
import heapq
#a,b=map(int,sys.stdin.readline().rstrip().split())
while True:
    n=int(input())
    if n==0:
        break
    a=0
    for i in range(1,n+1):
        a+=i
    print(a)