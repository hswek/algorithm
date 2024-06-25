import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
a=int(input())
b=int(input())
c=int(input())
if a==60 and b==60 and c==60:
    print('Equilateral')
elif a+b+c==180 and (a==b or a==c or b==c):
    print('Isosceles')
elif a+b+c==180:
    print('Scalene')
else:
    print('Error')