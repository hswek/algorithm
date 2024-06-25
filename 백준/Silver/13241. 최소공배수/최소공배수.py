import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))


a,b=map(int,sys.stdin.readline().rstrip().split())
c=math.gcd(a,b)
print(a*b//c)