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
result=1
n,m=map(int,sys.stdin.readline().rstrip().split())
parent_arr=[-1]*(n)

for i in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if union(a,b)==False:
        print(result)
        break
    result+=1
if result==1+m:
    print(0)


