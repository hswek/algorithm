import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
while True:
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if a==0 and b==0:
        break
    if a>=b and a%b==0:
        print('multiple')
    elif b>=a and b%a==0:
        print('factor')
    else:
        print('neither')