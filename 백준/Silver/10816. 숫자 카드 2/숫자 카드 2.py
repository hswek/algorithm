import sys
import heapq
INT_MAX=500001
INT_MIN=-1
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

#print(arr)
def left_binary_search(what,start,end):
    #print(start,end)
    if start+1==end:
        return start if arr[start]==what else INT_MAX
    mid= (start+end)//2
    #print(mid,wha)
    if arr[mid]>=what:
        result=left_binary_search(what,start,mid)
        if arr[mid]==what and result==INT_MAX:
            return mid
    else:
        result=left_binary_search(what,mid,end)
    #result=min(result,r)
    return result

def right_binary_search(what,start,end):
    #print(start,end)
    if start+1==end:
        return start if arr[start]==what else INT_MIN
    mid= (start+end)//2
    if arr[mid]>what:
        result=right_binary_search(what,start,mid)
    else:

        result=right_binary_search(what,mid,end)
        if arr[mid]==what and result==INT_MIN:
            return mid
    return result

m=int(input())
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
#print(arr)
for i in arr2:
    l=left_binary_search(i,0,n)
    if l==INT_MAX:
        print(0)
    else:
        #print(l,right_binary_search(i,0,n))
        print(right_binary_search(i,0,n)-l+1)