def solution(num):
    answer = 0
    if num==1:
        return 0
    for i in range(500):
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
        if num==1:
            break
        answer=i
    answer+=2
    if answer>=501:
        return -1
    return answer