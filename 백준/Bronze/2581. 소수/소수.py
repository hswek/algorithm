import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n=int(input())
m=int(input())
#a,b=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
result=0
e=-1
for a in range(n,m+1):
    arr2=[]
    for i in range(1,a+1):
        #print(i)
        if a%i==0:
            arr2.append(i)
    if len(arr2)==2:
        result+=a
        if e==-1:
            e=a
if e==-1:
    print(e)
else:
    print(result)
    print(e)