def solution(survey, choices):
    answer = ''
    d={'R':0,'T':1,'C':2,'F':3,'J':4,'M':5,'A':6,'N':7}
    d2={}
    for key,value in d.items():
        d2[value]=key
    arr=[0]*10
    for i in range(len(survey)):
        first=survey[i][0]
        second=survey[i][1]
        if choices[i]==1:
            arr[d[first]]+=3
        if choices[i]==2:
            arr[d[first]]+=2
        if choices[i]==3:
            arr[d[first]]+=1
        if choices[i]==5:
            arr[d[second]]+=1
        if choices[i]==6:
            arr[d[second]]+=2
        if choices[i]==7:
            arr[d[second]]+=3
    for i in range(0,8,2):
        if arr[i]>=arr[i+1]:
            answer+=d2[i]
        else:
            answer+=d2[i+1]
            
    return answer