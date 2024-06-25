import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
subin,sister=map(int,sys.stdin.readline().rstrip().split())
visit=[0]*100010

d=[]
heapq.heappush(d,[0,subin])
while(len(d)!=0):
    a,now=heapq.heappop(d)
    visit[now]=1
    if now== sister:
        print(a)
        break
    pos=[1,-1]
    for i in pos:
        nx=now+i
        if nx>=100001 or nx<0 or visit[nx]==1:
            continue
        heapq.heappush(d,[a+1,nx])
    nx=now+now
    if nx>=100001 or nx<0 or visit[nx]==1:
        continue

    heapq.heappush(d,[a,nx])

    