import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n,m=map(int,sys.stdin.readline().rstrip().split())
parent_arr=[-1]*(n+1)
def find(element):
    if parent_arr[element]==-1:
        return element
    parent_arr[element]=find(parent_arr[element])
    return parent_arr[element]
def union(a,b):
    a_mom=find(a)
    b_mom=find(b)
    if b_mom==a_mom:
        return
    parent_arr[b_mom]=a_mom
    return
for i in range(m):
    cal,a,b=map(int,sys.stdin.readline().rstrip().split())
    if cal==1:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)
    #print(parent_arr)

    