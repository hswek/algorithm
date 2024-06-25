from itertools import combinations_with_replacement
import heapq
def get_time(arr,cache,k,reqs):
    d={}
    for i in range(1,k+1):
        d[i]=[]
    for a,b,c in reqs:
        d[c].append([a,b])
    result=0
    for i in range(1,k+1):
        num=arr[i]
        mento=[]
        d[i].sort()
        for a,b in d[i]:
            #print(i,mento)
            if num>0:
                num-=1
                heapq.heappush(mento,a+b)    
            else:
                finished_time=heapq.heappop(mento)
                if a>=finished_time:
                    heapq.heappush(mento,a+b)
                else:
                    #print(i,'인',a,b,'가', finished_time-a,'기다림')
                    result+=finished_time-a
                    heapq.heappush(mento,finished_time+b)
    return result
def solution(k, n, reqs):
    answer = 99999999999999999999
    cache=[[-1] *(k+1) for i in range(n)]
    arr=list(range(1,k+1))
    comb=list(combinations_with_replacement(arr,n-k))
    for c in comb:
        arr=[1]*(k+1)
        arr[0]=0
        for what in c:
            arr[what]+=1
        #print(arr,get_time(arr,cache,k,reqs))
        #print()
        answer=min(answer,get_time(arr,cache,k,reqs))
        #print()
    return answer