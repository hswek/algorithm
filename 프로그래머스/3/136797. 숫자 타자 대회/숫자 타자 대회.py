def go(hand,num):
    d={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    x,y=d[num]
    hx,hy=d[hand]
    if x==hx and hy==y:
        return 1
    if x==hx:
        return abs(hy-y)*2
    elif y==hy:
        return abs(hx-x)*2
    dx=abs(x-hx)
    dy=abs(y-hy)
    if dx>dy:
        return (dx-dy)*2 + dy*3
    else:
        return (dy-dx)*2 + dx*3
def rec(l,r,idx,numbers):
    global nn
    if idx>=nn:
        return 0
    if cache[l][r][idx]!=-1:
        return cache[l][r][idx]
    n=numbers[idx]
    n=int(n)
    result=99999999999999
    if r!=n:
        result=min(result,rec(n,r,idx+1,numbers)+arr[l][n])
    if l!=n:
        result=min(result,rec(l,n,idx+1,numbers)+arr[r][n])
    cache[l][r][idx]=result
    return result
import sys
def solution(numbers):
    sys.setrecursionlimit(10**6)
    global nn,arr,cache
    nn=len(numbers)
    answer = 0
    left=[1,0]
    right=[1,2]
    d={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    arr=[[0]*(10) for i in range(10)]
    for i in range(10):
        for j in range(10):
            arr[i][j]=go(i,j)
    cache=[[[-1] *( len(numbers)+1) for i in range(10)] for j in range(10)]
    answer=rec(4,6,0,numbers)
    return answer