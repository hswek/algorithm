import sys
from collections import deque
import heapq
import math
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

n=int(input())
arr=[]
edges=[]
result=0
parent_arr=[-1]*(n+1)
for i in range(n):
    x,y=map(float,sys.stdin.readline().rstrip().split())
    for j in range(len(arr)):
        heapq.heappush(edges,[math.sqrt((arr[j][0]-x)**2+(arr[j][1]-y)**2),i,j])
    arr.append([x,y])
while(len(edges)!=0):
    length,i,j=heapq.heappop(edges)
    if find(i)==find(j):
        continue
    else:
        union(i,j)
        result+=length
print(result)
    



