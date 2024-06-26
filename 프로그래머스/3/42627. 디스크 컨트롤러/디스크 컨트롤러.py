import heapq
def solution(jobs):
    answer = 0
    
    c=len(jobs)
    #print(jobs,c)
    heapq.heapify(jobs)
    time=0
    
    tmp=[]
    while len(jobs) or len(tmp):
        if len(tmp)==0:
            a,b=heapq.heappop(jobs)
            time=a
            heapq.heappush(tmp,[b,a])
        b,a=heapq.heappop(tmp)
        #print(time)
        answer+=(time-a)+b
        time=time+b
        while len(jobs) and jobs[0][0]<=time:
            a,b=heapq.heappop(jobs)
            heapq.heappush(tmp,[b,a])

    return answer//c