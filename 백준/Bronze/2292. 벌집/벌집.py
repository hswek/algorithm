import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n=int(input())
o=n
n-=1
a=6
result=1
while True:
    if o==1:
        print(1)
        break
    if n>a:
        n-=a
        a+=6
        result+=1
        continue
    else:
        print(result+1)
        break
