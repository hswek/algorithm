import heapq
def solution(n, k, enemy):
    answer = 0
    #enemy.sort()
    arr=[]  
    now=0
    for e in enemy:
        now+=e
        heapq.heappush(arr,-e)
        answer+=1
        if now>n:
            while k and now>n:
                k-=1
                top=heapq.heappop(arr)
                #print('pop',top)
                now+=top
            if now>n:
                return answer-1
        
    return answer