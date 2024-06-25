import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
s2=set([])
a=[]
s=input()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        #print(s[i:j])
        a.append(s[i:j])
        #print(s2)
s2=set(a)
print(len(s2))
    