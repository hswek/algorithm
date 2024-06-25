import sys
from collections import deque
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[i for i in range(1,n+1)]
for _ in range(m):
    start,end,mid=map(int,sys.stdin.readline().rstrip().split())
    start-=1
    mid-=1
    end-=1
    tmp=deque(arr[start:end+1])
    for i in range(end-mid+1):
        t=tmp.pop()
        tmp.appendleft(t)
    for i in range(len(tmp)):
        arr[start+i]=tmp[i]
    #print(arr)
for i in arr:
    print(i,end=' ')
