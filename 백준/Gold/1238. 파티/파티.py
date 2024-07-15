import sys
from collections import deque
import heapq
import math
#sys.setrecursionlimit(10**5)
n,m,x=map(int,sys.stdin.readline().rstrip().split())
linked_list=[[] for _ in range(n+1)]
linked_list2=[[] for _ in range(n+1)]
for _ in range(m):
    i,j,cost=map(int,sys.stdin.readline().rstrip().split())

    linked_list[i].append((j,cost))
    linked_list2[j].append((i,cost))
'''
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
'''

visit=[-1]*(n+1)
q=[(0,x)]
while len(q):
    cost,now=heapq.heappop(q)
    if visit[now]!=-1:
        continue
    visit[now]=cost
    for next,next_cost in linked_list[now]:
        if visit[next]!=-1:
            continue
        heapq.heappush(q,(cost+next_cost,next))
visit2=[-1]*(n+1)
q=[(0,x)]
while len(q):
    cost,now=heapq.heappop(q)
    if visit2[now]!=-1:
        continue
    visit2[now]=cost
    for next,next_cost in linked_list2[now]:
        if visit2[next]!=-1:
            continue
        heapq.heappush(q,(cost+next_cost,next))
result=0
#print(visit2)
for i in range(1,n+1):
    result=max(result,visit2[i]+visit[i])
print(result)