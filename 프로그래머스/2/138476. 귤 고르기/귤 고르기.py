def solution(k, tangerine):
    answer = 0
    d={}
    for t in tangerine:
        if t not in d:
            d[t]=1
        else:
            d[t]+=1
    arr=list(d.items())
    arr.sort(key=lambda x:x[1])
    rest=len(tangerine)-k
    idx=0
    answer=len(arr)
    while rest>0:
        if rest-arr[idx][1]<0:
            break
        answer-=1
        rest=rest-arr[idx][1]
        #print(rest)
        idx+=1
    #print(arr)
    return answer