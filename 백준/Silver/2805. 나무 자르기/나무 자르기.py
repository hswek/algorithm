import sys
import heapq


def can_get(h):
    result=0
    for i in arr:
        result+=i-h if i-h>=0 else 0
    return result
end=2**31
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
arr=list(map(int,sys.stdin.readline().rstrip().split()))
start=0
while(end-start>1):
    mid=int(start/2.0+end/2.0)
    if can_get(mid)>=m:
        start=mid
    else:
        end=mid
print(start)