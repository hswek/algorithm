def solution(routes):
    answer = 0
    routes.sort(key=lambda x:[x[1],x[0]])
    now=-999999
    for start,end in routes:
        if end<=now or start<=now:
            continue
        now=end
        answer+=1
    return answer