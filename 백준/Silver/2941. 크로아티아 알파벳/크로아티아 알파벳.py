import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#a,b=list(map(int,sys.stdin.readline().rstrip().split()))
n=input()
result=len(n)
for s in range(1,len(n)):
    if n[s]=='=':
        if n[s-1]=='c' or n[s-1]=='s':
            result-=1
        elif n[s-1]=='z':
            if s==1:
                result-=1
                continue
            if n[s-2]=='d':
                result-=2
            else:
                result-=1
    if n[s]=='j':
        if n[s-1]=='l' or n[s-1]=='n':
            result-=1
    if n[s]=='-':
        if n[s-1]=='c' or n[s-1]=='d':
            result-=1
print(result)
            