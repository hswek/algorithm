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

capacity=[[0] * v for i in range(v)]
flow=[[0] * v for i in range(v)]
arr=[[] for i in range(v)]

for _ in range(e):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    i-=1
    j-=1
    arr[i].append(j)
    arr[j].append(i)
    capacity[i][j]=1
sink=1
source=0
result=0
while True:
    q=deque()
    q.append(source)
    parent=[-1]*v
    while len(q):
        top=q.popleft()
        for i in arr[top]:
            if parent[i]==-1 and capacity[top][i]-flow[top][i]>0:
                parent[i]=top
                q.append(i)
                if i==sink: 
                    break
    if parent[sink]==-1:
        break
    m=987654321
    top=sink
    while True:
        m=min(m,capacity[parent[top]][top]-flow[parent[top]][top])
        top=parent[top]
        if top==source:
            break
    top=sink
    while True:
        flow[parent[top]][top]+=m
        flow[top][parent[top]]-=m
        top=parent[top]
        if top==source:
            break
    result+=m
print(result)
    
    
    