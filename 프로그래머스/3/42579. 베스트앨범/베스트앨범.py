def solution(genres, plays):
    answer = []
    d={}
    for i in range(len(plays)):
        if genres[i] not in d:
            d[genres[i]]=[plays[i],[[plays[i],i]]]
        else:
            d[genres[i]][0]+=plays[i]
            d[genres[i]][1].append([plays[i],i])
    arr=list(d.values())
    arr.sort(key=lambda x:-x[0])
    for val in arr:
        val=val[1]
        val.sort(key=lambda x:[-x[0],x[1]])
        for j in range(min(len(val),2)):
            answer.append(val[j][1])
    return answer