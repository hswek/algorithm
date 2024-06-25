import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
arr1=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
print(max(sum(arr1),sum(arr2)))