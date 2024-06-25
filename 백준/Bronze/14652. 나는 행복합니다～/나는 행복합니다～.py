import sys
from collections import deque
import heapq
n,m,e=map(int,sys.stdin.readline().rstrip().split())
print(e//m,end=' ')
print(e%m)