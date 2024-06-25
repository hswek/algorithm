import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))

n=int(input())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
for _ in range(n):
    a=int(input())
    while True:
        t=0
        if a<=1:
            a=2
            continue
        for i in range(2,int(math.sqrt(a))+1):
            if a%i==0:
                #print(a)
                t=1
                break
        if t==0:
            print(a)
            break
        a+=1
    