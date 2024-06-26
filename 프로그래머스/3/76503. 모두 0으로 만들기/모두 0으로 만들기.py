from collections import deque
def dfs(now, a,arr,visit):
    global answer
    for i in arr[now]:
        if visit[i]==True:
            continue
        visit[i]=True
        result=dfs(i,a,arr,visit)
        answer+=abs(result)
        a[now]+=result
    return a[now]
import sys
def solution(a, edges):
    sys.setrecursionlimit(10**6)
    global answer
    answer = 0
    if sum(a)!=0:
        return -1
    n=len(a)
    arr=[[] for i in range(n)]
    visit=[-1] * n
    for i,j in edges:
        arr[i].append(j)
        arr[j].append(i)
    dfs(0,a,arr,visit)
    return answer