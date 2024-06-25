import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#a,b=list(map(int,sys.stdin.readline().rstrip().split()))
e,s=0,0
for _ in range(20):
    a,b,c=sys.stdin.readline().rstrip().split()
    b=float(b)
    if c=='A+':
        c=4.5
    if c=='A0':
        c=4.0
    if c=='B+':
        c=3.5
    if c=='B0':
        c=3.0
    if c=='C+':
        c=2.5
    if c=='C0':
        c=2.0
    if c=='D+':
        c=1.5
    if c=='D0':
        c=1.0
    if c=='F':
        c=0.0
    if c=='P':
        continue
    s+=b
    #print(b,c)
    e+=b*c
print(e/s)