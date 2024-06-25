import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
def find(element):
    if parent_arr[element]==-1:
        return element
    parent_arr[element]=find(parent_arr[element])
    return parent_arr[element]
def union(a,b):
    a_mom=find(a)
    b_mom=find(b)
    if b_mom==a_mom:
        return False
    if a_mom<b_mom:
        parent_arr[b_mom]=a_mom
    else:
        parent_arr[a_mom]=b_mom
    return True
t=int(input())
for _ in range(t):

    n,m=map(int,sys.stdin.readline().rstrip().split())
    arr=[[] for i in range(n+1)]
    q=[]
    parent=[-1]*(n+1)
    for i in range(m):
        i,j=map(int,sys.stdin.readline().rstrip().split())
        arr[i].append(j)
        heapq.heappush(q,[i,j])
    result=0
    #while len(q)!=0:
    #    i,j=heappop(q)
    #    if find(i)==find(j):
    #       continue
    #   else:
    #       union(i,j)
    print(n-1)
        
    
    



