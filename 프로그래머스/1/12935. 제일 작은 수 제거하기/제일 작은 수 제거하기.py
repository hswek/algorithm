def solution(arr):
    answer = []
    a=min(arr)
    for i in arr:
        if i!=a:
            answer.append(i)
    if len(answer)==0:
        answer=[-1]
    return answer