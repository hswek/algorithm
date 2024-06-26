import heapq
import sys
sys.setrecursionlimit(10**8)
def solution(land, height):
    answer = 0
    n=len(land)
    visit=[[-1] * n for _ in range(n)]
    def dfs(i,j,num):
        visit[i][j]=num
        dx=[1,0,-1,0]
        dy=[0,-1,0,1]
        for o in range(4):
            nx=i+dx[o]
            ny=j+dy[o]
            if nx>=n or ny>=n or nx<0 or ny<0 or visit[nx][ny]!=-1 or abs(land[nx][ny]-land[i][j])>height:
                continue
            dfs(nx,ny,num)
    num=1
    for i in range(n):
        for j in range(n):
            if visit[i][j]==-1:
                dfs(i,j,num)
                num+=1
    dis_arr=[{} for i in range(num)]
    def re_visit(i,j):
        dx=[1,0,-1,0]
        dy=[0,-1,0,1]
        for o in range(4):
            nx=i+dx[o]
            ny=j+dy[o]
            if nx>=n or ny>=n or nx<0 or ny<0:
                continue
            now_num=visit[i][j]
            next_num=visit[nx][ny]
            next_height=abs(land[nx][ny]-land[i][j])
            if next_num not in dis_arr[now_num]:
                dis_arr[now_num][next_num]=199999
            if now_num not in dis_arr[next_num]:
                dis_arr[next_num][now_num]=199999
            dis_arr[now_num][next_num]=min(dis_arr[now_num][next_num],next_height)
            dis_arr[next_num][now_num]=min(dis_arr[next_num][now_num],next_height)
            
    for i in range(n):
        for j in range(n):
            re_visit(i,j)
    parent=[i for i in range(num)]
    def find(i):
        if i==parent[i]:
            return i
        parent[i]=find(parent[i])
        return parent[i]
    def union(i,j):
        i_mom=find(i)
        j_mom=find(j)
        if i>j:
            parent[i_mom]=j_mom
        else:
            parent[j_mom]=i_mom
    h=[]
    for i in range(1,num):
        for j in dis_arr[i].keys():
            heapq.heappush(h,(dis_arr[i][j],i,j))
    while len(h):
        cost,i,j=heapq.heappop(h)
        if find(i)==find(j):
            continue
        answer+=cost
        union(i,j)
    return answer