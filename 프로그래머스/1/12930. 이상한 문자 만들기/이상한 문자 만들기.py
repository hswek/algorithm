def solution(s):
    answer = ''
    idx=1
    for i in s:
        if i==' ':
            idx=0
        if idx%2==1:
            answer+=i.upper()
        else:
            answer+=i.lower()
        idx+=1
    return answer