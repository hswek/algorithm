import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
r=3
n=int(input())-1
while n!=0:
    r=2*r-1
    n-=1
print(r**2)