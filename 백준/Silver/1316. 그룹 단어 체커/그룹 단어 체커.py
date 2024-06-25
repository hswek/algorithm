import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#a,b=list(map(int,sys.stdin.readline().rstrip().split()))
n=int(input())
r=0
for _ in range(n):
    s=input()
    d={}
    p=0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=0
        else:
            if s[i]==s[i-1]:
                continue
            else:
                p=1
                break
    if p!=1:
        r+=1
print(r)