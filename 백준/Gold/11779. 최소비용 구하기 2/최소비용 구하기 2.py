import sys
from collections import deque
import heapq
#sys.setrecursionlimit(10**4)
v=int(sys.stdin.readline().rstrip())
e=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(v+1)]
for i in range(e):
    i,j,w=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append([j,w])
start,end=map(int,sys.stdin.readline().rstrip().split())  
distance=[987654321]*(v+1)
distance[start]=0
q=[]
q.append([0,start,-1])
parent_arr=[-1]*(v+1)
while(len(q)!=0):
    cost,where,parent=heapq.heappop(q)
    if distance[where]<cost:
        continue
    if parent !=-1:
        parent_arr[where]=parent
    for des,cost2 in arr[where]:
        if distance[des]<=cost+cost2:
            continue
        distance[des]=cost+cost2
        heapq.heappush(q,[cost+cost2,des,where])
print(distance[end])
print_arr=[]
while True:
    print_arr.append(end)
    if parent_arr[end]==-1:
        break
    end=parent_arr[end]
print(len(print_arr))
for i in range(len(print_arr)-1,-1,-1):
    print(print_arr[i],end=' ')
