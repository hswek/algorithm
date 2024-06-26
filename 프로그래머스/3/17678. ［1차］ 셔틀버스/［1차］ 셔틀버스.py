def to_minute(t):
    h,m=map(int,t.split(':'))
    return h*60+m
def from_minute(t):
    h=t//60
    m=t%60
    return str(h).zfill(2)+':'+str(m).zfill(2)
import heapq
def solution(n, t, m, timetable):
    answer = ''
    arr=[]
    for tt in timetable:
        arr.append(to_minute(tt))
    heapq.heapify(arr)
    now=to_minute('09:00')
    while n:
        tmp=[]
        tmp_m=m
        while len(arr) and tmp_m:
            if arr[0]>now:
                break
            tmp_m-=1
            tmp.append(heapq.heappop(arr))
        if n==1:
            if tmp_m:
                return from_minute(now)
            else:
                last=tmp[-1]
                return from_minute(last-1)
                if tmp[0]==last:
                    return from_minute(last-1)
                for a in range(len(tmp)):
                    if tmp[a]==last:
                        return from_minute(tmp[a-1])
        now+=t
        n-=1
    return answer