import sys
import heapq

n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
#print(arr)
def binary_search(what,start,end):
    #print(start,end)
    if start+1==end:
        return arr[start]==what
    mid=(start+end)//2
    if arr[mid]==what:
        return 1
    elif arr[mid]>what:
        return binary_search(what,start,mid)
    else:
        return binary_search(what,mid,end)
m=int(input())
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
for i in arr2:
    print(int(binary_search(i,0,n)))