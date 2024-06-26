def rec(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if cache[n]!=-1:
        return cache[n]
    ans=0
    for i in range(n):
        ans+=rec(n-1-i)* rec(i)
    cache[n]=ans
    return ans
def solution(n):
    answer = 0
    global cache
    cache=[-1]*(n+1)
    answer=rec(n)
    return answer