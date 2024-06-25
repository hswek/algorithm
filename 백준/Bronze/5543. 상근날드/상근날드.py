import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
a=min([a,b,c])
print(min(a+d,a+e)-50)