import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(sys.stdin.readline().rstrip())
a=0
for i in range(n):
    
    arr=sys.stdin.readline().rstrip().split()
    #print(arr)
    #print(a)
    if arr[0]=='add':
        a=a|1<<int(arr[1])
    elif arr[0]=='remove':
        a=a & ~(1<<int(arr[1]))
    elif arr[0]=='check':
        print(a>>int(arr[1])&1)
    elif arr[0]=='toggle':
        a=  a ^ (1<<int(arr[1]))
    elif arr[0]=='all':
        a=(1<<21)-1
    elif arr[0]=='empty':
        a=0