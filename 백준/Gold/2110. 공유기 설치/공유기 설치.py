import sys
import heapq

def can_get(length,c,index):
    for i in range(index+1,n):
        if arr[i]-arr[index]>=length:
            index=i
            c=c-1
        if c==1:
            return True
    return False


n,c=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
start=0
end=1100000000//(c-1)+10000
while(end-start>1):
    mid=int(start/2.0+end/2.0)
    #print(mid,can_get(mid,c,0))
    if can_get(mid,c,0):
        start=mid
    else:
        end=mid
print(start)