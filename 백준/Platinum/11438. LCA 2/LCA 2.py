import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
arr=[[] for _ in range(n+1)]
for _ in range(n-1):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append(j)
    arr[j].append(i)
n2=int(sys.stdin.readline().rstrip())
head=1
depth=[0]*(n+1)
visit=[False]*(n+1)
parent = [ [-1] *(n+1) for _ in range(int(math.log2(n)+2))]
def dfs(node,now_dth):
    depth[node]=now_dth
    visit[node]=True
    for next_node in arr[node]:
        if visit[next_node]==False:
            parent[0][next_node]=node
            dfs(next_node,now_dth+1)
            
dfs(head,0)
for i in range(1,int(math.log2(n))+1):
    for node in range(1,n+1):
        parent[i][node]=parent[i-1][parent[i-1][node]]

def get_same_parent(i,j):
    if depth[i]>depth[j]:
        i,j=j,i
    for z in range(int(math.log2(n))+1,-1,-1):
        if depth[j]-depth[i]>=2**z:
            j=parent[z][j]
    if i==j:
        return i
    for z in range(int(math.log2(n))+1,-1,-1):
        if parent[z][i]!=parent[z][j]:
            i=parent[z][i]
            j=parent[z][j]
    return parent[0][i]
        

        
for _ in range(n2):
    i2,j2=map(int,sys.stdin.readline().rstrip().split())
    result=get_same_parent(i2,j2) 
    print(result)
