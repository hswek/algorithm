import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
v,e=map(int,sys.stdin.readline().rstrip().split())

arr=[[] for i in range(v)]
for _ in range(e):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    i-=1
    j-=1
    arr[i].append(j)
q=deque()
scc_id=[-1]*v
scc_counter=0
dfs_counter=0
visit=[-1]*v
def dfs(root):
    global dfs_counter,scc_counter,scc_id,q
    dfs_counter+=1
    visit[root]=dfs_counter
    q.append(root)
    m=dfs_counter
    for i in arr[root]:
        if visit[i]==-1:
            m=min(m,dfs(i))
        elif scc_id[i]==-1:
            m=min(m,visit[i])
    if m==visit[root]:
        while True:
            top=q.pop()
            scc_id[top]=scc_counter
            if top==root:
                break
        scc_counter+=1
    return m
for i in range(v):
    if visit[i]==-1:
        dfs(i)
arr3=[[] for i in range(scc_counter)]
for i in range(v):
    arr3[scc_id[i]].append(i)
arr3.sort()
print(len(arr3))
for i in arr3:
    for j in i:
        print(j+1,end=' ')
    print(-1)
        
        
        
        