import sys
from collections import deque
import heapq
n,s=map(int,sys.stdin.readline().rstrip().split())

arr=list(map(int,sys.stdin.readline().rstrip().split()))
sum_arr=[0]*n
sum_arr[0]=arr[0]
here=-1
for i in range(1,n):
    sum_arr[i]=sum_arr[i-1]+arr[i]
    if here==-1 and sum_arr[i]>=s:
        here=i
if sum_arr[0]>=s:
    here=0
#print(sum_arr)
if here==-1:
    print(0)
else:
    start=0
    min_length=here+1
    #print(min_length)
    while(here!=n):
        
        if start==-1:
            start=0
        while(sum_arr[here]-sum_arr[start]>=s):
            start+=1
            if start>=n:
                break
        start-=1
        #print(here,start,sum_arr[here]-sum_arr[start])
        min_length=min(min_length,here-start)
        here+=1

        #print(start,here,here)
    print(min_length)