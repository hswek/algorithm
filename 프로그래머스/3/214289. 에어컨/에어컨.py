import sys
def rec(idx,now,temp,t1,t2,a,b,onboard):
    if not(-10<=now<=40) :
        return 9999999999999
    if idx>=len(onboard):
        return 0
    if cache[idx][now+15]!=-1:
        return cache[idx][now+15]
    if onboard[idx]==1 and not (t1<=now<=t2): 
        return 9999999999999
    absnum=1
    if temp< now :
        absnum=-1
    if temp==now:
        absnum=0
    turn_maintain=rec(idx+1,now,temp,t1,t2,a,b,onboard)+b
    turn_up=rec(idx+1,now-1,temp,t1,t2,a,b,onboard)+a
    turn_down=rec(idx+1,now+1,temp,t1,t2,a,b,onboard)+a
    turn_off=rec(idx+1,now+absnum,temp,t1,t2,a,b,onboard)
    cache[idx][now+15]=min([turn_maintain,turn_up,turn_down,turn_off])
    return min([turn_maintain,turn_up,turn_down,turn_off])
def solution(temp, t1, t2, a, b, onboard):
    answer = 0
    sys.setrecursionlimit(10**6)
    global cache
    cache=[ [-1] * 60 for i in range(len(onboard)+10)]
    answer=rec(0,temp,temp,t1,t2,a,b,onboard)
    return answer