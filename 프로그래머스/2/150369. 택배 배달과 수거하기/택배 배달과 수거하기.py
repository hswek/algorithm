import heapq
def solution(cap, n, deliveries, pickups):
    answer = 0
    d=[]
    p=[]
    for i in range(len(deliveries)):
        if deliveries[i]!=0:
            heapq.heappush(d,[-i,deliveries[i]]) 
    for i in range(len(pickups)):
        if pickups[i]!=0:
            heapq.heappush(p,[-i,pickups[i]]) 
    while len(d) or len(p):
        now_weight=0
        a=-1
        if len(d)!=0:
            a=max(a,-d[0][0])
        if len(p)!=0:
            a=max(a,-p[0][0])   
        answer+=(a+1)
        while len(d):
            now_weight+=d[0][1]
            if now_weight>cap:
                d[0][1]-=cap-now_weight+d[0][1]
                break
            elif now_weight==cap:
                heapq.heappop(d)
                break
            else:
                heapq.heappop(d)
        
        now_weight=0
        while len(p):
            now_weight+=p[0][1]
            if now_weight>cap:
                now_weight-=p[0][1]
                p[0][1]-=cap-now_weight
                break
            elif now_weight==cap:
                heapq.heappop(p)
                break
            else:
                heapq.heappop(p)
    return answer*2