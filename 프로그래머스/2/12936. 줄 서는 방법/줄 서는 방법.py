from itertools import permutations
def fac(n):
    global cache
    if cache[n]!=-1:
        return cache[n]
    if n==1:
        return 1
    if n==0:
        return 1
    cache[n]=fac(n-1)*n
    return cache[n]
def solution(n, k):
    global cache
    cache=[-1]*21
    answer = []
    k=k-1
    arr=list(range(1,n+1))
    nn=n
    while len(arr):
        tmp=k//fac(nn-1)
        answer.append(arr[tmp])
        arr.pop(tmp)
        k=k%fac(nn-1)
        nn=nn-1
    return answer