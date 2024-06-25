import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
a=int(input())

#a,b=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
result=0
e=-1

arr2=[]
while True:
    for i in range(2,a+1):
        #print(i)
        if a%i==0:
            arr2.append(i)
            a=a//i
            break
    #print(a)
    if a==1:
        #arr2.append(1)
        break
arr2.sort()
for i in arr2:
    print(i)