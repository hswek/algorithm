import sys
from collections import deque
import heapq
#n,m,e=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
result=0
while True:
    if n<=5:
        print(result+1)
        break
    else:
        n=n-5
        result+=1