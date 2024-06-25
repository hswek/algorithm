import sys
from collections import deque
import heapq
import bisect
n,c=map(int,sys.stdin.readline().rstrip().split())
origin_arr=list(map(int,sys.stdin.readline().rstrip().split()))
result=0

mid=n//2
arr_l=[]
arr_r=[]
def recursive(start,end,s,arr):
    if start==end:
        arr.append(s)
        return
    recursive(start+1,end,s,arr)
    if s+origin_arr[start]<=c:
        recursive(start+1,end,s+origin_arr[start],arr)
    
    
recursive(0,mid,0,arr_l)
recursive(mid,n,0,arr_r)

arr_r.sort()
for i in arr_l:
    remain=c-i
    result+=bisect.bisect_right(arr_r,remain)
print(result)
    