def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    num=len(score)//m
    for i in range(num):
        #print(score[(i+1)*m-1]*m )
        answer+=(score[(i+1)*m-1]*m)
    return answer