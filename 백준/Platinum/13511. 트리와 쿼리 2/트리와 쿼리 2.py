import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
arr=[[] for _ in range(n+1)]
for _ in range(n-1):
    i,j,w=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append((j,w))
    arr[j].append((i,w))
n2=int(sys.stdin.readline().rstrip())
same_parent={}
head=1
depth=[-1]*(n+1)
visit=[False]*(n+1)
parent = [ [[-1,-1] for __ in range(n+1)] for _ in range(int(math.log2(n)+3))]
def dfs(node,now_dth):
    depth[node]=now_dth
    visit[node]=True
    for next_node,cost in arr[node]:
        if visit[next_node]==False:
            parent[0][next_node]=[node,cost]
            dfs(next_node,now_dth+1)
            
dfs(head,0)
for i in range(1,int(math.log2(n))+1):
    for node in range(1,n+1):
        next_node=parent[i-1][node][0]
        if next_node!=-1:
            parent[i][node][0]=parent[i-1][next_node][0]
            parent[i][node][1]=parent[i-1][next_node][1]+parent[i-1][node][1]
def get_min_cost(i,j):
    oi,oj=i,j
    if depth[i]>depth[j]:
        i,j=j,i
    all_cost=0

    depth_diff=depth[j]-depth[i]
    for z in range(int(math.log2(n))+1,-1,-1):
        if depth_diff & 1<<z:
            all_cost+=parent[z][j][1]
            j=parent[z][j][0]
    if i==j:
        same_parent[str(oi)+"_"+str(oj)]=i
        same_parent[str(oj)+"_"+str(oi)]=i
        return all_cost
    for z in range(int(math.log2(n))+1,-1,-1):
        if parent[z][i][0]!=parent[z][j][0]:
            all_cost+=parent[z][j][1]
            all_cost+=parent[z][i][1]
            i=parent[z][i][0]
            j=parent[z][j][0]
    all_cost+=parent[0][j][1]
    all_cost+=parent[0][i][1]
    
    same_parent[str(oi)+"_"+str(oj)]=parent[0][j][0]
    same_parent[str(oj)+"_"+str(oi)]=parent[0][j][0]
    return all_cost
        
def get_up(node,how):
    idx=0

    while how:
        if how%2==1:
            node=parent[idx][node][0]
        how=how>>1
        idx+=1
        
    return node
def get_nst_node(i,j,o):
    if i==j:
        return i
    get_min_cost(i,j)
    same_node=same_parent[str(i)+"_"+str(j)]

    i_to_same=depth[i]-depth[same_node]
    j_to_same=depth[j]-depth[same_node]
    nn=j_to_same - (o - i_to_same)
    
    if i_to_same>=o+1:
        return get_up(i,o)
    else:
        
        return get_up(j,nn)

for _ in range(n2):
    a=list(map(int,sys.stdin.readline().rstrip().split()))
    if a[0]==1:
        r=get_min_cost(a[1],a[2])
    else:
        u,v,k = a[1],a[2],a[3]-1
        r=get_nst_node(u,v,k)
    print(r)
    
