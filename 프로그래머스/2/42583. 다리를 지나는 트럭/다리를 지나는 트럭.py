from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_weight=0
    time=0
    d=deque()
    idx=0
    while idx<len(truck_weights):
        time+=1
        
        if len(d)>0 and (time-d[0][1])==bridge_length:
            #print(time,d[0][0],'가 내림')
            now_weight-=d[0][0]
            d.popleft()
        if len(d)==0 or now_weight+ truck_weights[idx]<= weight:
            #print(time,truck_weights[idx],'가 탐')
            d.append([truck_weights[idx],time])
            idx+=1
            now_weight+=d[-1][0]
        #if idx<len(truck_weights):
            #3#print(time,now_weight,truck_weights[idx],bridge_length)
    return time+bridge_length