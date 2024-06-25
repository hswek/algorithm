import sys
from collections import deque
import heapq
now=1
sys.setrecursionlimit(10**5)
v,e=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for i in range(v+1)]
for i in range(e):
    s,e,w=map(int,sys.stdin.readline().rstrip().split())
    arr[s].append([e,w])
    arr[e].append([s,w])
mid1,mid2=map(int,sys.stdin.readline().rstrip().split())
q=[]

def dijkstra(start,end):
    q=[]
    distance=[987611121]*(v+1)
    heapq.heappush(q,[0,start])
    distance[start]=0
    while(len(q)!=0):
        dis,now=heapq.heappop(q)
        if distance[now]<dis:
            continue
        for now2,dis2 in arr[now]:
            if distance[now2]>dis+dis2:
                distance[now2]=dis+dis2
                heapq.heappush(q,[dis+dis2,now2])
    return distance[end]
        
        
        
def solve(start,mid1,mid2,end):
    result=dijkstra(start,mid1)+dijkstra(mid1,mid2)+dijkstra(mid2,end)
    result=min(result,dijkstra(start,mid2)+dijkstra(mid2,mid1)+dijkstra(mid1,end))
    if result>=98761121:
        print(-1)
    else:
        print(result)
    
solve(1,mid1,mid2,v)







