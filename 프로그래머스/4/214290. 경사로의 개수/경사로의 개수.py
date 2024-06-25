import sys
import copy

def get_length(arr,now,c,grid):
    if now==1:
        c[now]=arr
        return
    prev=c[now//2]
    tmp=mul(prev,prev,grid)
    c[now]=tmp
def get_num(tmp):
    result=0
    for e in tmp:
        result+=sum(e)
    return result
def mul(tmp1,tmp2,grid):
    n=len(grid[0])*len(grid)
    tmp=[[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp[i][j]+=tmp1[i][k]*tmp2[k][j]%(10**9 + 7)
    return tmp
def rec(idx,x,y,d,grid):
    global tmp
    if idx==len(d):
        return {(x,y):1}
    if cache[idx][x][y]!=-1:
        return cache[idx][x][y]
    arr=[[0,1],[0,-1],[1,0],[-1,0]]
    tmp2={}
    result=0
    for i in range(4):
        nx=x+arr[i][0]
        ny=y+arr[i][1]
        if nx<0 or ny<0 or nx>=len(grid) or ny>=len(grid[0]):
            continue
        if grid[nx][ny]-grid[x][y]!=d[idx]:
            continue
        for where,num in rec(idx+1,nx,ny,d,grid).items():
            if where not in tmp2:
                tmp2[where]=num
            else:
                tmp2[where]+=num
    cache[idx][x][y]=tmp2
    return tmp2
def solution(grid, d, k):
    global cache,tmp
    sys.setrecursionlimit(10**8)
    cache= [[[-1] * len(grid[0]) for i in range(len(grid))] for j in range(len(d))]
    answer = 0
    dic={}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dic[(i,j)]={}
            for i2 in range(len(grid)):
                for j2 in range(len(grid[0])):
                    dic[(i,j)][(i2,j2)]=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dest,num in rec(0,i,j,d,grid).items():
                dic[(i,j)][dest]+=num
    arr3=[[0] * (len(grid)*len(grid[0])) for i in range(len(grid)*len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for i2 in range(len(grid)):
                for j2 in range(len(grid[0])):
                    arr3[i*len(grid[0])+j][i2*len(grid[0])+j2]=dic[(i,j)][(i2,j2)]
    now=1
    result=1
    c={}
    idx=0
    kc=k
    while True:
        get_length(arr3,now,c,grid)
        now=now*2
        kc=kc//2
        if kc==0:
            break
    arr2=[]
    while True:
        if (k>>idx)%2==1:
            arr2.append(c[1<<idx])
        idx+=1
        if k<(1<<idx):
            break
    if len(arr2)==1:
        return get_num(arr2[0])
    tmp=arr2[0]
    for i in range(1,len(arr2)):
        tmp=mul(tmp,arr2[i],grid)
    return get_num(tmp)%(10**9+7)