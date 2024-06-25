import sys
from collections import deque
import heapq
now=1
sys.setrecursionlimit(10**5)
v,e=map(int,sys.stdin.readline().rstrip().split())
start=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(v+1)]
for i in range(e):
    i,j,w=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append([j,w])

q=[]
distance=[987654321]*(v+1)
distance[start]=0
heapq.heappush(q,[0,start])
while(len(q)!=0):
    w,now=heapq.heappop(q)
    
    if distance[now]<w:
        continue
    for des,des_w in arr[now]:
        if distance[des]>w+des_w:
            heapq.heappush(q,[w+des_w,des])
            distance[des]=w+des_w
for i in range(1,v+1):
    if distance[i]==987654321:
        print('INF')
    else:
        print(distance[i])

