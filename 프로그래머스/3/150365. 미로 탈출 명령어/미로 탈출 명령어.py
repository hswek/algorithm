from collections import deque
def dfs(nowx,nowy,cost,route):
    global arr,a1,a2,n,m,d,answer
    if answer!='z':
        return
    if k<abs((r2-1)-nowx)+cost+abs(nowy-(c2-1)):
        return
    if k==cost :
        if nowx==r2-1 and nowy==c2-1:
            answer=route
        return
    for i in range(4):
        nx,ny=nowx+a2[i][0],nowy+a2[i][1]
        if nx>=n or nx<0 or ny>=m or ny<0 :
            continue
        dfs(nx,ny,cost+1,route+a1[i])
import sys
def solution(nn, mm, x, y, r22, c22, kk):
    sys.setrecursionlimit(10**6)
    # d l r u
    global arr,a1,a2,n,m,j,r2,c2,k,d,answer
    answer = 'z'
    r2=r22
    c2=c22
    n=nn
    m=mm
    k=kk
    a1=['d','l','r','u']
    a2=[[1,0],[0,-1],[0,1],[-1,0]]
    tmp=k-(r2-x)-(c2-y)
    if tmp<0:
        return 'impossible'
    elif tmp%2==1:
        return 'impossible'
    dfs(x-1,y-1,0,'')
    if answer=='z':
        return 'impossible'
    return answer