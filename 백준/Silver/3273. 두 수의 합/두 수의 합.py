import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
s=int(input())
arr.sort()
end=n-1
start=0
result=0
#print(arr)

while(end>start):
    #print(start,end)
    if arr[end]+arr[start]==s:
        result+=1
    if arr[end]+arr[start]<s:
        start+=1
    elif arr[end]+arr[start]>s:
        end-=1
    else:
        if arr[end]==arr[end-1]:
            end-=1
        else:
            start+=1
print(result)