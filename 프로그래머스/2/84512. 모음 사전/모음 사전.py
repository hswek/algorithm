from bisect import bisect_left
import sys
def dfs(length,s):
    global arr
    if length==5:
        if s!='':
            arr.append(s)
        return
    for i in ['','A','E','I','O','U']:
        dfs(length+1,s+i)
def solution(word):
    sys.setrecursionlimit(10**6)
    answer = 0
    global arr
    arr=[]
    dfs(0,'')
    arr=set(arr)
    arr=list(arr)
    arr.sort()

    answer=bisect_left(arr,word)
    return answer+1