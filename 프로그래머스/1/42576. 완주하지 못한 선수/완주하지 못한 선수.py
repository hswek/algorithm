def solution(participant, completion):
    answer = ''
    p={}
    p2={}
    for i in completion:
        if i not in p:
            p[i]=1
        else:
            p[i]+=1
    for i in participant:
        if i not in p2:
            p2[i]=1
        else:
            p2[i]+=1
    
    for i in participant:
        if i not in p or p[i]!=p2[i]:
            return i
    return answer