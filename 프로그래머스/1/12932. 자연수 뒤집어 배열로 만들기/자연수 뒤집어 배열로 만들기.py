def solution(n):
    answer = []
    n=str(n)
    n=list(n)
    n.reverse()
    for i in n:
        i=int(i)
        answer.append(i)
    return answer