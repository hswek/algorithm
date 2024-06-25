import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(9):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
max_num=-1
max_i=-1
max_j=-1
for i in range(9):
    for j in range(9):
        if arr[i][j]>=max_num:
            max_i=i
            max_j=j
            max_num=arr[i][j]
print(max_num)
print(max_i+1,max_j+1)