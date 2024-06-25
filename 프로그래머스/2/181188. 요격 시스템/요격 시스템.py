def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1] )
    idx=0
    while idx<len(targets):
        now=targets[idx][1]
        idx+=1
        while idx<len(targets):
            if targets[idx][0]>=now:
                break
            idx+=1
        answer+=1
    return answer