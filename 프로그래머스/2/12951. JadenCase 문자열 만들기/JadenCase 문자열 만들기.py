def solution(s):
    answer = ''
    answer2=''
    arr=s.split()
    for s2 in arr:
        s2=s2[0].upper()+s2[1:].lower()
        answer2+=s2
    idx=0
    for i in s:
        if i==' ':
            answer+=' '
        else:
            answer+=answer2[idx]
            idx+=1
    return answer