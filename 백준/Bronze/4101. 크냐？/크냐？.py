import sys
from collections import deque
import heapq
while True:
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if a==0 and b==0:
        break
    if a>b:
        print('Yes')
    else:
        print('No')
