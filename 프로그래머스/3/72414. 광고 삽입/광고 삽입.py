def to_second(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:])
    return hour+minute+second
def from_second(time):
    hour = str(time // 3600).zfill(2)
    minute = str(time % 3600 // 60).zfill(2)
    second = str(time % 3600 % 60).zfill(2)
    return hour+":"+minute+":"+second

def solution(play_time, adv_time, logs):
    answer = ''
    play_time=to_second(play_time)
    adv_time=to_second(adv_time)
    arr=[0]*(play_time+1)
    for log in logs:
        start,end=log.split('-')
        start=to_second(start)
        end=to_second(end)
        arr[start]+=1
        arr[end]-=1
    for i in range(1,play_time+1):
        arr[i]=arr[i-1]+arr[i]
    s=arr[:adv_time]
    s=sum(s)
    answer=0
    max_s=s
    for i in range(1,play_time - adv_time+1):
        s=s-arr[i-1]+arr[adv_time+i-1]
        if s>max_s:
            max_s=s
            answer=i
    answer=from_second(answer)
    return answer