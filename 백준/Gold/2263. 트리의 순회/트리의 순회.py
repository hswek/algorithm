import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
in_order=list(map(int,sys.stdin.readline().rstrip().split()))
post_order=list(map(int,sys.stdin.readline().rstrip().split()))
root=post_order[-1]
def recursive(in_start,in_end,post_start,post_end,in_order,post_order):
    #print(in_start,in_end,post_start,post_end)
    if in_end<in_start or post_start>post_end:
        return
    root=post_order[post_end]
    print(root,end=' ')
    if in_end==in_start:
        return
    in_mid=-1
    for i in range(in_start,in_end+1):
        if in_order[i]==root:
            in_mid=i
            break
    left_length=in_mid-in_start
    right_length=in_end-in_mid
    recursive(in_start,in_mid-1,post_start,post_start+left_length-1,in_order,post_order)
    recursive(in_mid+1,in_end,post_start+left_length,post_end-1,in_order,post_order)
recursive(0,n-1,0,n-1,in_order,post_order)
    
    
    