import sys
import heapq

def can_get(a):
    global n,k
    result=0
    for i in range(1,n+1):
        result+=min(n,(a//i))
    #print(a,result,k)
    return result<=k
        
        
n=int(input())
k=int(input())
arr=[]
k=k-1
start=0
end=10000000001
while(end-start>1):
    mid=int(start/2.0+end/2.0)
    #print(mid,can_get(mid))
    if can_get(mid):
        start=mid
    else:
        end=mid
print(start+1)