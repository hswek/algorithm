import sys
from collections import deque
import heapq
#a,b=map(int,sys.stdin.readline().rstrip().split())
a=input()
b=input()
if len(a)>=len(b):
    print('go')
else:
    print('no')
