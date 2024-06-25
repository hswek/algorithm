import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
a,b,c=map(int,sys.stdin.readline().rstrip().split())
print(int(max(a/b*c,a*b/c)))