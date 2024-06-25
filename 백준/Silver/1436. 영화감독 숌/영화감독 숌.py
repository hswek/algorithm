import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
a=665
while True:
    if n==0:
        break
    a+=1
    if '666' in str(a):
        n-=1
print(a)

        