import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))

#n=int(input())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
while True:
    a=int(input())
    result=0
    if a==0:
        break
    if a==1:
        print(1)
        continue
    for i in range(a+1,2*a+1):
        #print(i)
        t=0
        if i<=1:
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                #print(a)
                t=1
                break
        if t==0:
            result+=1
    print(result)
    