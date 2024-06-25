import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
end=n-1
start=0
result=abs(arr[0]+arr[n-1])
what=[arr[0],arr[n-1]]


while(end>start):
    if end==start:
        break
    tmp=arr[end]+arr[start]
    if result>abs(tmp):
        result=abs(tmp)
        what=[arr[start],arr[end]]
    if arr[end]+arr[start]<0:
        start+=1
    elif arr[end]+arr[start]>=0:
        end-=1
print(what[0],what[1])