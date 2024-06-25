import sys
from collections import deque
import heapq
import bisect
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
print_arr=[0]
print_arr[0]=arr[0]
mom_arr=[-1]*(n)
mom_arr[0]=0
for i in range(1,len(arr)):
    if print_arr[len(print_arr)-1]<arr[i]:
        print_arr.append(arr[i])
        mom_arr[i]=len(print_arr)-1
    else:
        tmp=bisect.bisect_left(print_arr,arr[i])
        print_arr[tmp]=arr[i]
        mom_arr[i]=tmp
print(len(print_arr))
start=len(print_arr)-1
p=[]
#print(mom_arr)
for i in range(n-1,-1,-1):
    if mom_arr[i]==start:
        p.append(arr[i])
        start-=1
for i in range(len(p)-1,-1,-1):
    print(p[i],end=' ')