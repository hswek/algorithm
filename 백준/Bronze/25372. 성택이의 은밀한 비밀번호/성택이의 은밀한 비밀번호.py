import sys
from collections import deque
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
for i in range(n):
    a=input()
    if len(a)>=6 and len(a)<=9:
        print('yes')
    else:
        print('no')
