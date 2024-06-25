import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
def find(element):
    if parent_arr[element]==-1:
        return element
    parent_arr[element]=find(parent_arr[element])
    return parent_arr[element]
def union(a,b):
    a_mom=find(a)
    b_mom=find(b)
    if b_mom==a_mom:
        return False
    if a_mom<b_mom:
        parent_arr[b_mom]=a_mom
    else:
        parent_arr[a_mom]=b_mom
    return True
def dfs(x,y,num):
    global n
    visit[x][y]=num
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0 or visit[nx][ny]!=-1 or arr[nx][ny]==0:
            continue
        dfs(nx,ny,num)
    return
        

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

q=[]
visit=[[-1]*(m) for i in range(n)]
num=1
for i in range(n):
    for j in range(m):
        if visit[i][j]==-1 and arr[i][j]==1:
            dfs(i,j,num)
            num+=1
length_arr=[[987654321] * (num) for i in range(num)]

def go(x,y,n1):
    global num
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        l=0
        nx,ny=x,y

        while True:
            nx,ny=nx+dx[i],ny+dy[i]
            l+=1

            if nx>=n or nx<0 or ny>=m or ny<0:
                break
            if visit[nx][ny]==n1:
                break
            if visit[nx][ny]!=-1 and visit[nx][ny]!=n1:
                if l-1==1:
                    break
                tmp=visit[nx][ny]
                length_arr[n1][tmp]=min(length_arr[n1][tmp],l-1)
                length_arr[tmp][n1]=min(length_arr[tmp][n1],l-1)
                break
    

for i in range(n):
    for j in range(m):
        if visit[i][j]!=-1:
            go(i,j,visit[i][j])

q=[]
for i in range(num):
    for j in  range(num):
        if length_arr[i][j]!=987654321  :
            heapq.heappush(q,[length_arr[i][j],i,j])
#print(q)
parent_arr=[-1]*(num)
result=0
while len(q)!=0:
    w,i,j=heapq.heappop(q)
    if find(i)==find(j):
        continue
    else:
        #print(w,i,j)
        union(i,j)
        result+=w
for i in range(1,num):
    if find(1)!=find(i):
        print(-1)
        break
else:
    
    print(result)






