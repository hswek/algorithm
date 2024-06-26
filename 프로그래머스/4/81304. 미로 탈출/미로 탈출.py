import heapq
def solution(n, start, end, roads, traps):
    answer = 0
    arr=[{} for i in range(n+1)]
    rev_arr=[{} for i in range(n+1)]
    visit={}
    is_rev=["0"]*(n+1)
    t={}
    for trap in traps:
        t[trap]="1"
    for s,e,cost in roads:
        if e not in arr[s]:
            arr[s][e]=cost
        else:
            arr[s][e]=min(arr[s][e],cost)
        if s not in rev_arr[e]:
            rev_arr[e][s]=cost
        else:
            rev_arr[e][s]=min(rev_arr[e][s],cost)
    h=[[0,start,is_rev]]
    ans=[]
    while len(h):
        cost,where,is_rev=heapq.heappop(h)
        ss=".".join(is_rev)+"_"
        if ss+str(where) in visit:
            continue
        visit[ss+str(where)]="1"
        if where==end:
            return cost
        for e,c in arr[where].items():
            if (is_rev[where]=="1" and is_rev[e]=="1")\
            or (is_rev[where]=="0" and is_rev[e]=="0"):
                new_is_rev=is_rev.copy()
                if e in t:
                    if new_is_rev[e]=="1":
                        new_is_rev[e]="0"
                    else:
                        new_is_rev[e]="1"
                heapq.heappush(h,[cost+c,e,new_is_rev])
                
        for e,c in rev_arr[where].items():
            if (is_rev[where]=="1" and is_rev[e]=="0")\
            or (is_rev[where]=="0" and is_rev[e]=="1"):
                new_is_rev=is_rev.copy()
                if e in t:
                    if new_is_rev[e]=="1":
                        new_is_rev[e]="0"
                    else:
                        new_is_rev[e]="1"
                heapq.heappush(h,[cost+c,e,new_is_rev])
    return min(ans)