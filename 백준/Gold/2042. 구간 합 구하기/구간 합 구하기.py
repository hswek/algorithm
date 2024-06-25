import sys

sys.setrecursionlimit(10**5)
def merge(l,r):
    return l+r
def build(left,right,idx):
    if left==right:
        seg_tree[idx]=arr[left]
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=build(left,mid,idx*2)
    right_val=build(mid+1,right,idx*2+1)
    seg_tree[idx]=merge(left_val,right_val)
    return seg_tree[idx]
def query(left,right,want_left,want_right,idx):
    if want_left> right or want_right< left:
        return 0
    if want_left<=left and want_right>= right:
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=query(left,mid,want_left,want_right,idx*2)
    right_val=query(mid+1,right,want_left,want_right,idx*2+1)
    return merge(left_val,right_val)
def update(left,right,idx,want_idx,want_val):
    if left >want_idx or right< want_idx: 
        return seg_tree[idx]
    if left==right:
        seg_tree[idx]=want_val
        return seg_tree[idx]
    mid=(left+right)//2
    left_val=update(left,mid,idx*2,want_idx,want_val)
    right_val=update(mid+1,right,idx*2+1,want_idx,want_val)
    seg_tree[idx]=merge(left_val,right_val)
    return seg_tree[idx]
n,m,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
seg_tree=[0]*(4*n)
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
build(0,n-1,1)
for j in range(m+k):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    if a==1:
        update(0,n-1,1,b-1,c)
    else:
        print(query(0,n-1,b-1,c-1,1))