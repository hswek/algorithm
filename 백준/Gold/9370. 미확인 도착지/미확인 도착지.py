import sys
from collections import deque
import heapq
now=1
sys.setrecursionlimit(10**5)
T=int(input())
for _ in range(T):
    v,e,c=map(int,sys.stdin.readline().rstrip().split())
    start,g,h=map(int,sys.stdin.readline().rstrip().split())
    arr=[[] for i in range(v+1)]
    for i in range(e):
        s,e,w=map(int,sys.stdin.readline().rstrip().split())
        arr[s].append([e,w])
        arr[e].append([s,w])
    candidate=[]
    for i in range(c):
        inp=int(sys.stdin.readline().rstrip())
        candidate.append(inp)

    def dijkstra(start):
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
        return distance

    start_distance=dijkstra(start)
    h_distance=dijkstra(h)
    g_distance=dijkstra(g)
    print_arr=[]
    for i,j in arr[h]:
        if i==g:
            h_g=j
    for i,j in arr[g]:
        if i==h:
            g_h=j
    for end in candidate:
        if start_distance[end]==start_distance[h]+g_distance[end]+h_g or start_distance[end]==start_distance[g]+h_distance[end]+g_h:
            print_arr.append(int(end))
    print_arr.sort()
    for i in print_arr:
        print(i,end=' ')
    print()





