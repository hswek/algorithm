def solution(id_list, report, k):
    answer = []
    d={}
    d2={}
    d3={}
    for s in report:
        if s in d2:
            continue
        d2[s]=True
        a,b=s.split()
        if b not in d:
            d[b]=1
        else:
            d[b]+=1
        if a not in d3:
            d3[a]=[b]
        else:
            d3[a].append(b)
    who_reported={}
    for key,val in d.items():
        if val>=k:
            who_reported[key]=True
    print(who_reported)
    for idd in id_list:
        tmp=0
        if idd in d3:
            for i in d3[idd]:
                if i in who_reported:
                    tmp+=1
        answer.append(tmp)
    return answer