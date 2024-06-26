def solution(clothes):
    answer = 1
    d={}
    for i,j in clothes:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
    for e in d.values():
        answer*=(e+1)
    answer-=1
    return answer