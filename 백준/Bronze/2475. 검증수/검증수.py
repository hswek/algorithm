import sys
from collections import deque
import heapq
a,b,c,d,e=map(int,sys.stdin.readline().rstrip().split())
print((a**2+b**2+c**2+d**2+e**2)%10)