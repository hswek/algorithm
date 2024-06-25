import sys
import heapq

def can_get(mid,a):
    return arr2[mid]<=a
        
        
a=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(n):
    start=0
    end=len(arr2)-1
    while(end-start>1):
        mid=int(start/2.0+end/2.0)
        #print(mid,can_get(mid,n))
        if can_get(mid,n):
            start=mid
        else:
            end=mid
    return start
arr2=[0]
for i in arr:

    if arr2[-1]<i:
        arr2.append(i)
        continue
    where=binary_search(i)
    #print(where,arr2[where],i,arr2)
    if arr2[where]==i:
        continue
    #if arr2[where]==i:
    #where+=1
    arr2[where+1]=i
    #print(arr2)

print(len(arr2)-1)