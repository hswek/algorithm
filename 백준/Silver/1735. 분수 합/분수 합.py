import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))


a,b=map(int,sys.stdin.readline().rstrip().split())
c,d=map(int,sys.stdin.readline().rstrip().split())
up=a*d+b*c
down=b*d
#print(up,down)
c=math.gcd(up,down)
#print(c)
up=up//c
down=down//c
print(up,down)