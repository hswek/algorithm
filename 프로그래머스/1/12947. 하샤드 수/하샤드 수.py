def solution(x):
    answer = True
    a=0
    for i in str(x):
        a+=int(i)
    if x%a==0:
        return True
    else:
        return False
    return answer