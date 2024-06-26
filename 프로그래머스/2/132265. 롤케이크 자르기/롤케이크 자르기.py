def solution(topping):
    answer = 0
    d={}
    for top in topping:
        if top not in d:
            d[top]=1
        else:
            d[top]+=1
    d2={}
    for top in topping:
        if d[top]==1:
            del(d[top])
        else:
            d[top]-=1
        if top not in d2:
            d2[top]=1
        if len(d)==len(d2):
            answer+=1
    return answer