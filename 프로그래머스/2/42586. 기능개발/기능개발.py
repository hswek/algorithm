def solution(progresses, speeds):
    answer = []
    idx=0
    now=0
    tmp=0
    while len(speeds)>idx:
        if progresses[idx] + speeds[idx] * now < 100:
            now+=1
        else:
            while len(speeds)> idx:
                if progresses[idx] + speeds[idx] * now < 100:
                    break
                tmp+=1
                idx+=1

            now+=1
            answer.append(tmp)
            tmp=0
    return answer