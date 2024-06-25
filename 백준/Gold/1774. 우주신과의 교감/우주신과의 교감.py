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

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
edges=[]
result=0
parent_arr=[-1]*(n+1)
for i in range(n):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    for j in range(len(arr)):
        heapq.heappush(edges,[math.sqrt((arr[j][0]-x)**2+(arr[j][1]-y)**2),i,j])
    arr.append([x,y])
for _ in range(m):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    i-=1
    j-=1
    x,y=arr[i]
    x2,y2=arr[j]
    #print(x,y,x2,y2)
    if find(i)!=find(j):
        union(i,j)
    #result+=math.sqrt((x2-x)**2+(y2-y)**2)
    #print(result)
while(len(edges)!=0):
    length,i,j=heapq.heappop(edges)
    if find(i)==find(j):
        continue
    else:
        union(i,j)
        result+=length
print('%.2f'%result)
    



