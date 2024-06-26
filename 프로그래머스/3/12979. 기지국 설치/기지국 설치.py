from collections import deque
def solution(n, stations, w):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    stations=deque(stations)
    now=0
    while now<n:
        if len(stations):
            if now<stations[0]-w-1:
                now+=2*w+1
                answer+=1
            else:
                now=max(stations[0]+w,now)
                stations.popleft()
        else:
            #print('now+w+1에 설치')
            answer+=1
            now+=2*w+1
    return answer