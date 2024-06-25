import sys
import heapq


def can_get(n):
    result=0
    for i in arr:
        result+=i//n
    return result
end=2**31
k,n=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
start=0
while(end-start>1):
    mid=int(start/2.0+end/2.0)
    if can_get(mid)>=n:
        start=mid
    else:
        end=mid
print(start)