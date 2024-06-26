import heapq
def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i]=-works[i]
    heapq.heapify(works)
    arr=works
    while n!=0 and len(arr):
        now=-heapq.heappop(arr)
        now-=1
        if now!=0:
            heapq.heappush(arr,-now)
        n-=1
    print(arr)
    for i in arr:
        answer+=i**2
    return answer