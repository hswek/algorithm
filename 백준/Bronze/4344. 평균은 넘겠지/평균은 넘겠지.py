import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#a,b=list(map(int,sys.stdin.readline().rstrip().split()))
c=int(input())
for _ in range(c):
    
    arr=list(map(int,sys.stdin.readline().rstrip().split()))
    arr2=[]
    for i in range(1,arr[0]+1):
        arr2.append(arr[i])
    s=sum(arr2)
    m=s/len(arr2)
    r=0
    for i in arr2:
        if i>m:
            r+=1
    #print(m)
    print('%.3f'%(r/len(arr2)*100)+'%')
