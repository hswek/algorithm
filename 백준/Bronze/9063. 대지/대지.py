import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n=int(input())
min_x=987654321
max_x=-9999999
min_y=987654321
max_y=-9999999
for _ in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    min_x=min(min_x,a)
    max_x=max(max_x,a)
    min_y=min(min_y,b)
    max_y=max(max_y,b)
#print(max_x,min_x,max_y,min_y)
print((max_x-min_x)*(max_y-min_y))