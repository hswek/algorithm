import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
x,y,w,h=map(int,sys.stdin.readline().rstrip().split())
print(min(w-x,x,h-y,y))