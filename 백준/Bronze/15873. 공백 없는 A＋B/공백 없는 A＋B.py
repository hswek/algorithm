import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
a=int(input())
if a%10==0:
    print(a//100+a%100)
else:
    print(a//10+a%10)