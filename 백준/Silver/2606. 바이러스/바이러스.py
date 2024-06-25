import sys
from collections import deque
sys.setrecursionlimit(10**5)
n=int(input())
m=int(input())
start=1
arr=[[] for i in range(n+1)]
for i in range(m):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append(j)
    arr[j].append(i)
for i in range(1,n+1):
    arr[i].sort(reverse=True)
visit=[0]*(n+1)
num=1
def bfs(start):
    global num
    visit[start]=num
    num+=1
    q=deque()
    q.append(start)
    while(len(q)!=0):
        #print(q)
        top=q.popleft()
        for i in arr[top]:
            #print(i)
            if visit[i]==0:
                visit[i]=num
                num+=1
                q.append(i)
            
bfs(start)
a=0
for i in range(1,n+1):
    #print(visit[i])
    if visit[i]!=0:
        a+=1
print(a-1)