import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(int(10**5))
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
def merge(left_val,right_val):
    return left_val+right_val
def build(left,right,idx):
    if left==right:
        seg_tree[idx]=arr[left]
        return seg_tree[idx]
    mid=(left+right)//2
    
    left_val=build(left,mid,idx*2)
    right_val=build(mid+1,right,idx*2+1)
    seg_tree[idx]=merge(left_val,right_val)
    return seg_tree[idx]

def query(left,right,node_left,node_right,idx):
    if right<node_left or left>node_right:
        return 0
    if right>=node_right and left<=node_left:
        return seg_tree[idx]
    node_mid=(node_left+node_right)//2
    left_val=query(left,right,node_left,node_mid,idx*2)
    right_val=query(left,right,node_mid+1,node_right,idx*2+1)
    return merge(left_val,right_val)

def update(left,right,idx,want_to_idx,want_to_val):
    if want_to_idx< left or want_to_idx> right:
        return seg_tree[idx]
    if left==right:
        seg_tree[idx]=seg_tree[idx]+1
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=update(left,mid,idx*2,want_to_idx,want_to_val)
    right_val=update(mid+1,right,idx*2+1,want_to_idx,want_to_val)
    seg_tree[idx]=merge(left_val,right_val)
    return seg_tree[idx]

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
seg_tree=[0]*(n*4)
arr2=arr.copy()
arr2.sort()
d={}
result=0
for i in range(n):
    d[arr2[i]]=i
for i in range(n):
    result+=query(d[arr[i]]+1,1000000000,0,n-1,1)
    update(0,n-1,1,d[arr[i]],0)
print(result)