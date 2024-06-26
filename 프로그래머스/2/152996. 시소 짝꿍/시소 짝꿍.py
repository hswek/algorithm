def solution(weights):
    answer = 0
    d={}
    for w in weights:
        if w not in d:
            d[w]=1
        else:
            d[w]+=1
    for key,i in d.items():
        if i==1:
            continue
        else:
            #print(key,i)
            answer-=2*i*(i-1)//2
    d={}
    #weights=list(set(weights))
    for w in weights:
        for i in [2,3,4]:
            if w*i not in d:
                d[w*i]=1
            else:
                d[w*i]+=1
    for key,i in d.items():
        if i==1:
            continue
        else:
            #print(key,i)
            answer+=i*(i-1)//2
    return answer