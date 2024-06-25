import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
c=int(input())
for _ in range(c):
    n=int(input())
    for i in [25,10,5,1]:
        print(n//i,end=' ')
        n=n%i
    print()