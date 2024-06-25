import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
a,b=map(int,sys.stdin.readline().rstrip().split())
c=int(input())
d=int(input())
if a*d+b > c*d:
    print(0)
elif c-a<0:
    print(0)
else:
    print(1)