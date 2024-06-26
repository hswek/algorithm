import sys
def rec(num):
    global yy,cache,nn
    if num>yy:
        return 987654344
    if num==yy:
        return 0
    if cache[num]!=-1:
        return cache[num]
    a=rec(num+nn)+1
    b=rec(num*2)+1
    c=rec(num*3)+1
    cache[num]=min([a,b,c])
    return min([a,b,c])
def solution(x, y, n):
    sys.setrecursionlimit(10**7)
    answer = 0
    global yy,cache,nn
    nn=n
    cache=[-1]*(y+10)
    yy=y
    tmp=rec(x)
    if 9876534<=tmp :
        return -1
    else:
        return tmp