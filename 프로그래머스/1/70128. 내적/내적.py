def solution(a, b):
    answer=0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    #answer = 1234567890
    return answer