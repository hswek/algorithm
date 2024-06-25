import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
a,b,c=map(int,sys.stdin.readline().rstrip().split())
arr=[a,b,c]
arr.sort()
a=arr[2]
b=arr[1]
c=arr[0]
while True:
    if a<b+c:
        print(a+b+c)
        break
    else:
        a-=1