import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
s,x,y=map(int,sys.stdin.readline().rstrip().split())
def find(graph,what,l):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==what and not [i,j] in virus_list[what-1]:
                l.append([i,j])
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def is_in(graph,i,j):
    if i>=n or j>=n or i<0 or j<0:
        return False
    return True
def infect(graph,i,j,what):
    for ii in range(4):
        nx=i+dx[ii]
        ny=j+dy[ii]
        if is_in(graph,nx,ny)==True and graph[nx][ny]==0:
            graph[nx][ny]=what
virus_list=[[] for i in range(k)]
for _ in range(s):
    re=1
    for j in range(1,k+1):
        tmp_arr=[]
        find(graph,j,tmp_arr)
        for z in tmp_arr:
            infect(graph,z[0],z[1],j)
        virus_list[j-1].extend(tmp_arr)
        if tmp_arr!=[]:
            re=0
    if re==1:
        break
print(graph[x-1][y-1])