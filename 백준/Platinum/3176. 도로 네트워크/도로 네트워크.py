import sys
import math
n=int(sys.stdin.readline())
sys.setrecursionlimit(10**5)
arr=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

head=1
parent=[[(0,0,0)]*(int(math.log2(n+1))+1) for _ in range(n+1)]
depth=[0]*(n+1)
visit=[-1]*(n+1)

def dfs(now,now_depth):
    depth[now]=now_depth
    for next_node,cost in arr[now]:
        if visit[next_node]==True:
            continue
        parent[next_node][0]=(now,cost,cost)
        visit[next_node]=True
        dfs(next_node,now_depth+1)
        visit[next_node]=False
visit[head]=True
dfs(head,0)
    

for i in range(1,int(math.log2(n+1))+1):
    for now_node in range(1,n+1):
        grand_node=parent[parent[now_node][i-1][0]][i-1][0]
        max_edge=max(parent[now_node][i-1][1],parent[parent[now_node][i-1][0]][i-1][1])
        min_edge=min(parent[now_node][i-1][2],parent[parent[now_node][i-1][0]][i-1][2])
        parent[now_node][i]=(grand_node,max_edge,min_edge)
def get_answer(n1,n2):
    max_edge=-1
    min_edge=99999999999
    if depth[n1]>depth[n2]:
        n1,n2=n2,n1
    depth_diff=depth[n2]-depth[n1]
    #print(parent)
    #print(n1,n2,depth[n1],depth[n2])
    for i in range(int(math.log2(n+1))+1):
        if (depth_diff & 1<<i)==1<<i:
            #print(i)
            max_edge=max(max_edge,parent[n2][i][1])
            min_edge=min(min_edge,parent[n2][i][2])
            n2=parent[n2][i][0]
    if n1==n2:
        return (max_edge,min_edge)
    #print(n1,n2,depth[n1],depth[n2])
    for i in range(int(math.log2(n+1)),-1,-1):
        if parent[n1][i][0]!=0 and parent[n2][i][0]!=0 and parent[n1][i][0]!=parent[n2][i][0]:
            max_edge=max(max_edge,parent[n1][i][1])
            max_edge=max(max_edge,parent[n2][i][1])
            min_edge=min(min_edge,parent[n1][i][2])
            min_edge=min(min_edge,parent[n2][i][2])
            n1=parent[n1][i][0]
            n2=parent[n2][i][0]
    i=0
    max_edge=max(max_edge,parent[n1][i][1])
    max_edge=max(max_edge,parent[n2][i][1])
    min_edge=min(min_edge,parent[n1][i][2])
    min_edge=min(min_edge,parent[n2][i][2])
    #print(n1,n2,depth[n1],depth[n2])
    return (max_edge,min_edge)
k=int(sys.stdin.readline())  
for _ in range(k):
    d,e=map(int,sys.stdin.readline().split())
    m1,m2=get_answer(d,e)
    print(m2,m1)
        
            