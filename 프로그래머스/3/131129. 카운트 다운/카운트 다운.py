def rec(n,d,cache):
    if n==0:
        return [0,0]
    if n<0:
        return [99999999999,9999999999999]
    if cache[n]!=-1:
        return cache[n]
    if 1<=n<=20 or n==50:
        return [1,1]
    elif n in d:
        return [1,0]
    a=[99999999,99999999]
    what=-1
    for i in list(range(1,21))+[50]:
        if n-i>=0:
            tmp=rec(n-i,d,cache).copy()
            tmp[0]+=1
            tmp[1]+=1
            if tmp[0]<a[0]:
                a=tmp
                what=i
            elif tmp[0]==a[0] and tmp[1]>a[1]:
                a=tmp
                what=i
    for i in d.keys():
        if n-i>=0:
            tmp=rec(n-i,d,cache).copy()
            tmp[0]+=1
            if tmp[0]<a[0]:
                a=tmp
                what=i
            elif tmp[0]==a[0] and tmp[1]>a[1]:
                a=tmp
                what=i

    #print(n,what,a)
    cache[n]=a
    return a
import sys
def solution(target):
    sys.setrecursionlimit(10**6)
    answer = []
    d={}
    for i in range(1,21):
        d[2*i]=1
        d[3*i]=1
    cache=[-1]*(target+1)
    answer=rec(target,d,cache)
    return answer