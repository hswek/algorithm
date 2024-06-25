import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
while True:
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    if a==0 and b==0 and c==0:
        break
    arr=[a,b,c]
    arr.sort()
    a,b,c=arr
    #print(a,b,c)
    if c>=b+a:
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif a==b or b==c:
        print('Isosceles ')
    else:
        print('Scalene')
