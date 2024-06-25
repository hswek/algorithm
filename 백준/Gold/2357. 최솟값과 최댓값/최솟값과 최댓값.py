import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(int(10**5))
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())

def max_merge(left,right):
    return max(left,right)
def min_merge(left,right):
    return min(left,right)
def build(left,right,idx):
    if left==right:
        seg_tree[idx]=[arr[left],arr[left]]
        return seg_tree[idx]
    mid=(left+right)//2
    
    left_val=build(left,mid,idx*2)
    right_val=build(mid+1,right,idx*2+1)
    seg_tree[idx]=[min_merge(left_val[0],right_val[0]),max_merge(left_val[1],right_val[1])]
    return seg_tree[idx]

def query(left,right,node_left,node_right,idx):
    if right<node_left or left>node_right:
        return [11191187654321,-11111987654321]
    if right>=node_right and left<=node_left:
        return seg_tree[idx]
    node_mid=(node_left+node_right)//2
    left_val=query(left,right,node_left,node_mid,idx*2)
    right_val=query(left,right,node_mid+1,node_right,idx*2+1)
    return [min_merge(left_val[0],right_val[0]),max_merge(left_val[1],right_val[1])]

def update(left,right,idx,want_to_idx,want_to_val):
    if want_to_idx< left or want_to_idx> right:
        return seg_tree[idx]
    if left==right:
        seg_tree[idx]=[want_to_val,want_to_val]
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=update(left,mid,idx*2,want_to_idx,want_to_val)
    right_val=update(mid+1,right,idx*2+1,want_to_idx,want_to_val)
    seg_tree[idx]=[min_merge(left_val[0],right_val[0]),max_merge(left_val[1],right_val[1])]
    return seg_tree[idx]

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
seg_tree=[0]*(n*4)
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
build(0,len(arr)-1,1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    result=query(a-1,b-1,0,n-1,1)
    print(result[0],result[1])