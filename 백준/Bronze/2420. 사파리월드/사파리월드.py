import sys
from collections import deque
import heapq
n,m=map(int,sys.stdin.readline().rstrip().split())
print(abs(n-m))