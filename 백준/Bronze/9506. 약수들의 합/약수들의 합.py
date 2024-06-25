import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)

#a,b=map(int,sys.stdin.readline().rstrip().split())
while True:
    a=int(input())
    if a==-1:
        break
    arr=[]
    arr2=[]
    for i in range(1,a):
        if a%i==0:
            arr.append(str(i))
            arr2.append(i)
    if sum(arr2)==a:
        print(a,'= ',end='')
        s=' + '.join(arr)
        print(s)
    else:
        print(a,'is NOT perfect.')