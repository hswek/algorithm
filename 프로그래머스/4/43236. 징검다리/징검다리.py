import heapq
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks=rocks+[distance] 
    start=0
    end=distance
    while start<=end:
        result=0
        mid=(start+end)//2
        standard=0
        for i in range(len(rocks)):
            if rocks[i]-standard<mid:
                result+=1
            else:
                standard=rocks[i]
        if result<=n:
            answer=mid
            start=mid+1
        else:
            
            end=mid-1
    return answer