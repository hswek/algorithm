import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(int(10**5))
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
def build(left,right,idx):
    if left==right:
        seg_tree[idx]=arr[left]
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=build(left,mid,2*idx)
    right_val=build(mid+1,right,2*idx+1)
    seg_tree[idx]=left_val+right_val
    return seg_tree[idx]
def update(left,right,idx,want_to_idx):
    if want_to_idx< left or want_to_idx> right:
        return seg_tree[idx]
    if left==right:
        seg_tree[idx]=seg_tree[idx]+1
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=update(left,mid,idx*2,want_to_idx)
    right_val=update(mid+1,right,idx*2+1,want_to_idx)
    seg_tree[idx]=left_val+right_val
    return seg_tree[idx]
def delete(left,right,idx,want_to_rank):
    #global result
    if left==right:
        seg_tree[idx]=seg_tree[idx]-1
        return left
    mid=(left+right)//2
    if seg_tree[2*idx]>=want_to_rank:
        l=delete(left,mid,idx*2,want_to_rank)
    else:
        l=delete(mid+1,right,idx*2+1,want_to_rank-seg_tree[2*idx])
    seg_tree[idx]=seg_tree[2*idx]+seg_tree[2*idx+1]
    return l

n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr=[1]*n*2
seg_tree=[0]*(n*5)
build(0,n-1,1)
next_per=k
remain=n
print('<',end='')
for i in range(n-1):
    #print(seg_tree[1])
    result=delete(0,n-1,1,next_per)
    print(result+1,end='')
    print(',',end=' ')
    next_per=(next_per+k-2)%(n-i-1)+1

result=delete(0,n-1,1,next_per)     
print(result+1,end='')
print('>')