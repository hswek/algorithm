import heapq
def solution(food_times, k):
    answer = 0
    arr=[]
    time=0
    s=0
    for tim in food_times:
        arr.append(tim)
    heapq.heapify(arr)
    while True:
        if len(arr)==0:
            return -1
        min_time=(heapq.heappop(arr)-s)
        if time+min_time*(len(arr)+1)<k:
            time+=min_time*(len(arr)+1)
            s+=min_time
        elif time+min_time*(len(arr)+1)==k:
            s+=min_time
            for food in range(len(food_times)):
                if food_times[food]-s>0:
                    return food+1
        else:
            remain=len(arr)+1
            k=time+(k-time)%remain
            while True:
                answer=1
                for food in food_times:
                    if food-s<=0:
                        answer+=1
                        continue
                    if time==k:
                        return answer
                    time+=1
                    answer+=1
                    
    return answer