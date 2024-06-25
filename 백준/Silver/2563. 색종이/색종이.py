import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[0]*101 for i in range(101)]
n=int(input())
for _ in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j]=1
result=0
for i in range(1,101):
    for j in range(1,101):
        if arr[i][j]==1:
            result+=1
print(result)