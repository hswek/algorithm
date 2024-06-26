def rec(now):
    if cache[now]!=-1:
        return cache[now]
    if len(arr[now])==0:
        return [0,False]
    result2=0
    a=False
    for i in arr[now]:
        num,what=rec(i)
        if what==False:
            a=True
        result2+=num
    if a==True:
        result2+=1
    cache[now]=[result2,a]
    return [result2,a]
from collections import deque
import sys
def solution(n, lighthouse):
    sys.setrecursionlimit(10**6)
    answer = 0
    global arr
    arr=[[] for i in range(n+1)]
    for i,j in lighthouse:
        arr[i].append(j)
        arr[j].append(i)
    rarr=[[] for i in range(n+1)]
    root=1
    d=deque([root])
    visit=[False]*(n+1)
    visit[1]=True
    while len(d):
        root=d.popleft()
        for i in arr[root]:
            if visit[i]==False:
                rarr[root].append(i)
                visit[i]=True
                d.append(i)
    arr=rarr
    global cache
    cache=[-1]*(n+1)
    answer=rec(1)[0]
    #print(cache)
    return answer