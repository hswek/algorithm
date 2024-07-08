import sys
from collections import deque
sys.setrecursionlimit(10000)
n,k=map(int,sys.stdin.readline().rstrip().split())
l=list(map(int,sys.stdin.readline().rstrip().split()))
l.sort()
print(l[k-1])
