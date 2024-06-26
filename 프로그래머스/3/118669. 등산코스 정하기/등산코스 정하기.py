import heapq
def solution(n, paths, gates, summits):
    answer = []
    arr=[[] for i in range(n)]
    for i,j,w in paths:
        i-=1
        j-=1
        arr[i].append([j,w])
        arr[j].append([i,w])
    visit=[99999999999]*n
    for g in gates:
        arr[gates[0]-1].append([g-1,0])
    h=[]
    d={}
    for s in summits:
        d[s-1]=True
    heapq.heappush(h,[0,gates[0]-1])
    while len(h):
        cost,where=heapq.heappop(h)
        if visit[where]<cost:
            continue
        for where2,cost2 in arr[where]:
            if max(cost,cost2)>=visit[where2]:
                continue
            visit[where2]=max(cost,cost2)
            if where2 not in d:
                heapq.heappush(h,[max(cost,cost2),where2])
    m=99999999999
    m2=-1
    for s in summits:
        s-=1
        if visit[s]<m or (visit[s]==m and m2>s):
            m=visit[s]
            m2=s
    return [m2+1,m]