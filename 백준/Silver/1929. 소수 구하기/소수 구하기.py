import sys
from collections import deque
import heapq
import math
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[True]*(4000001)
for i in range(2,2001):
    if arr[i]==True:
        j=2
        while(i*j<4000001):
            arr[i*j]=False
            #print(i*j)
            j+=1
prime=[]
for i in range(2,4000001):
    if arr[i]==True:
        prime.append(i)
#print(prime[:20])
for i in range(n,m+1):
    if i>1 and arr[i]==True:
        print(i)
