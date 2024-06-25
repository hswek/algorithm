import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(5):
    arr.append(list(sys.stdin.readline().rstrip()))
for i in range(15):
    for j in range(5):
        if len(arr[j])>i:
            #print(j,i,len(arr[j]))
            print(arr[j][i],end='')