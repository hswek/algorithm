import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
v,e=map(int,sys.stdin.readline().rstrip().split())
edge=[]
for i in range(e):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    edge.append([a,b,c])
distance=[987650411]*(v+1)
distance[1]=0
    
def bellmon_ford(start):
    for i in range(v+1):
        for s,e,w in edge:
            #print(s,distance[s])
            if distance[s]==987650411:
                continue
            #print(distance[s])
            if distance[e]>distance[s]+w:
                if i==v:
                    return False
                distance[e]=distance[s]+w
    return True
            
if False==bellmon_ford(1):
    print(-1)
else:
    for i in range(2,v+1):
        if distance[i]==987650411:
            print(-1)
        else:
            print(distance[i])