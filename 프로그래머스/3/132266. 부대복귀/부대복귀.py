from collections import deque
import heapq
def solution(n, roads, sources, destination):
    answer = []
    arr=[[] for i in range(1,n+2)]
    for i,j in roads:
        arr[i].append(j)
        arr[j].append(i)
    q=[[0,destination]]
    visit=[-1]*(n+1)
    while len(q):
        cost,where=heapq.heappop(q)
        #print(cost,where)
        if visit[where]!=-1:
            continue
        visit[where]=cost
        for i in arr[where]:
            #print(i)
            if visit[i]!=-1:
                continue
            heapq.heappush(q,[cost+1,i])
    answer=[ visit[i] for i in sources]
    return answer