import sys
from collections import deque
import heapq
#a,b=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(3):
    arr.append(int(input()))
arr.sort()
print(arr[1])