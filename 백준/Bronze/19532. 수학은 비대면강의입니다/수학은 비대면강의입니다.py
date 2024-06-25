import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
a,b,c,d,e,f=map(int,sys.stdin.readline().rstrip().split())
for i in range(-999,1000):
    for j in range(-999,1000):
        #print(i,j)
        if a*i+b*j==c and d*i+ e*j==f:
            print(i,j)
        