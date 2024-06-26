import sys
def rec(idx,first,money):
    if idx>=len(money):
        return 0
    if idx==len(money)-1:
        if first==1 :
            return 0
        return money[idx]
    if cache[idx][first]!=-1:
        return cache[idx][first]
    arr=[0]
    arr.append(rec(idx+2,first,money)+money[idx])
    arr.append(rec(idx+1,first,money))
    cache[idx][first]=max(arr)
    #print(idx,prev,first,second,max(arr))
    return max(arr)
def solution(money):
    global cache
    sys.setrecursionlimit(10**6)
    cache=[[-1] * (2) for i in range(len(money)+5)]
    answer = 0
    answer=max(answer, rec(2,1,money)+money[0])
    answer=max(answer, rec(1,0,money) )
    return answer