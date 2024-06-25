import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n=int(input())
a=1
while True:
    if n>a:
        n-=a
        a+=1
        continue
    else:
        b=1
        #print(a,n)
        origin_a=a
        for i in range(n-1):
            b+=1
            a-=1
        if origin_a%2==0:
            print(b,'/',a,sep='')
        else:
            print(a,'/',b,sep='')
        break
            