def dfs(x,y,can_not_go,m, n):
    #print(x,y)
    global cache,visit
    if cache[x][y]!=-1:
        return cache[x][y]
    if x==n-1 and y==m-1:
        return 1
    arr=[[1,0],[0,1]]
    result=0
    for dx,dy in arr:
        nx=x+dx
        ny=y+dy
        if nx>=n or ny>=m or nx<0 or ny<0 or nx*1000+ny in can_not_go:
            continue
        visit[nx][ny]=1
        result+=dfs(nx,ny,can_not_go,m, n)
        visit[nx][ny]=-1
    cache[x][y]=result%1000000007
    return result%1000000007
def solution(m, n, puddles):
    global cache,visit
    answer = 0
    can_not_go={}
    cache=[[-1]* m for i in range(n)]
    visit=[[-1]* m for i in range(n)]
    for x,y in puddles:
        x-=1
        y-=1
        can_not_go[y*1000+x]=1
    answer=dfs(0,0,can_not_go,m, n)
    print(cache)
    return answer