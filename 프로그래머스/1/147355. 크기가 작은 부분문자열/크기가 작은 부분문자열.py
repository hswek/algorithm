def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        new_t=int(t[i:i+len(p)])
        new_p=int(p)
        if new_t<=new_p:
            answer+=1
    return answer