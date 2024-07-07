import sys
from collections import deque
r,c=map(int,sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(10000)
arr=[]
for i in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))
swan_map=[]
merge_list=set([])
melt_list={}
def v(i,j):
    d=deque([(i,j)])
    if arr[i][j]=='L':
        swan_map.append(count) 
    arr[i][j]=count  
    while len(d):
        x,y=d.popleft()
        dx=[1,0,-1,0]
        dy=[0,-1,0,1]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:
                continue
            if arr[nx][ny]=='X':
                melt_list[10000*nx+ny]=arr[x][y]
            if not arr[nx][ny] in ['L','.']:
                continue
            if arr[nx][ny]=='L':
                swan_map.append(count) 
            arr[nx][ny]=count  
            d.append((nx,ny))
count=0
for i in range(r):
    for j in range(c):
        if arr[i][j]=='.' or arr[i][j]=='L':
            v(i,j) 
            count+=1
day=1
def melt(x,y,cost):
    if arr[x][y]!='X' and arr[x][y]!=cost:
        merge_list.add(tuple(sorted([arr[x][y],cost])))
        return
    arr[x][y]=cost
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or ny<0 or nx>=r or ny>=c or arr[nx][ny]==arr[x][y]:
            continue
        if arr[nx][ny]!='X' and arr[nx][ny]!=cost and find(arr[nx][ny])!=find(arr[x][y]):
            merge_list.add((min(arr[x][y],arr[nx][ny]),max(arr[x][y],arr[nx][ny])))
        else:
            next_melt_list[10000*nx+ny]=arr[x][y]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
swan_map.sort()
parent=[i for i in range(count+2)]
def find(now):
    if parent[now]==now:
        return now
    parent[now]=find(parent[now])
    return parent[now]
def union(p1,p2):
    m1,m2=find(p1),find(p2)
    parent[m1]=parent[m2]
def merge(merge_list):
    for first,second in merge_list:
        union(first,second)
        if find(swan_map[0])==find(swan_map[1]):
            return "end"
new_arr={}
next_melt_list=[]
if swan_map[0]==swan_map[1]:
    print(0)
else:
    while day<1000:
        new_arr={}
        next_melt_list={}
        for i in melt_list.keys():
            i,j=i//10000,i%10000
            melt(i,j,melt_list[10000*i+j])
        merge_list=list(merge_list)
        if merge(merge_list)=="end":
            print(day)
            break
        day+=1
        melt_list=next_melt_list
        merge_list=set([])