import heapq
def solution(scores):
    answer = 1
    t=scores[0]
    t_s=sum(t)
    scores.sort(key=lambda x:[-x[0],x[1]])
    high=0
    for i,j in scores:
        if t[0]<i and t[1]<j:
            return -1
        if high <=j:
            if t_s < i+j:
                answer+=1
            high=j
    return answer